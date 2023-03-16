from django import forms
from django.contrib.auth.models import User
from .models import Profile


class UpdateUserForm(forms.ModelForm):
    '''
    To create User Update form
    '''
    username = forms.CharField(max_length=100,
                               required=True,
                               widget=forms.TextInput(attrs={
                                'class': 'form-control'}))
    email = forms.EmailField(required=True,
                             widget=forms.TextInput(attrs={
                                'class': 'form-control'}))

    class Meta:
        model = User
        fields = ['username', 'email']


class UpdateProfileForm(forms.ModelForm):
    '''
    To Update existing/automatically created Profile of the user
    '''
    brief_bio = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'form-control',
        'rows': 4}))

    class Meta:
        model = Profile
        fields = ['brief_bio', 'profile_image']
