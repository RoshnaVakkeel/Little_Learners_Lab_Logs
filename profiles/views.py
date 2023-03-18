from django.shortcuts import render, redirect, HttpResponseRedirect, get_object_or_404  # NOQA
from django.urls import reverse_lazy
from django.views import View
from django.utils.decorators import method_decorator
from django.template import RequestContext
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import ProfileForm
from .models import Profile


class ProfileAccount(View):
    """
    User profile and account view.
    Redirects to login page if user not authenticated.
    Credits for the code:
    https://github.com/Code-Institute-Submissions/andy-guttridge-song-mates
    """
    @method_decorator(login_required)
    def get(self, request, *args, **kwargs):
        if not Profile.objects.filter(user=request.user).exists():
            profile = Profile(user=request.user)
            profile.save()
        # Retrieve profile from database, create form from it and
        # render
        profile_queryset = Profile.objects.filter(user=request.user)
        get_object_or_404(profile_queryset)
        profile = profile_queryset.first()
        profile_form = ProfileForm(instance=profile)
        return render(
            request,
            'edit_profile.html',
            {
                'profile': profile,
                'form': profile_form
            }
        )


class UpdateProfile(View):
    """
    To handle updates of user profile.
    Redirects to login page if user not authenticated.
    """
    @method_decorator(login_required)
    def post(self, request, *args, **kwargs):
        # Find user profile in database, associate with form
        # and populate form using POST request data

        profile_queryset = Profile.objects.filter(user=request.user)
        get_object_or_404(profile_queryset)
        profile = profile_queryset.first()
        profile_form = ProfileForm(request.POST, request.FILES,
                                   instance=profile)
        # Check if user hit submit button and form is valid. Save if true.
        # Otherwise reload page using existing data
        if profile_form.is_valid() and 'profile-form-submit' in request.POST:
            profile_form.clean()
            try:
                profile_form.save()
                messages.info(
                    request,
                    'The changes to your profile have been saved.'
                )
            except Error:
                messages.error(request, "Error in form submission. Did you\
                                try to upload a file that isn't an image?")
            return HttpResponseRedirect(reverse_lazy('edit_profile'))
        else:
            profile_form = ProfileForm(instance=profile)
            return HttpResponseRedirect(reverse_lazy('edit_profile'))


class UserDelete(View):
    """
    To delete the user's profile and account
    Makes the user account inactive
    """
    # Approach to making a user account inactive adapated from
    # https://stackoverflow.com/questions/38047408/how-to-allow-user-to-delete-account-in-django-allauth
    @method_decorator(login_required)
    def post(self, request, *args, **kwargs):
        # Check there is a profile for the user and delete if so
        if Profile.objects.filter(user=request.user).exists():
            profile = Profile.objects.filter(user=request.user)
            profile.delete()
        # Make user account inactive
        request.user.is_active = False
        request.user.save()
        messages.info(
                request,
                'Your profile has been deleted.'
            )
        return HttpResponseRedirect(reverse_lazy('account_logout'))
