from django import forms
from django.forms import ModelForm, FileInput
from django.contrib.auth.models import User
from .models import Profile
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Field, Button, Submit, HTML
from crispy_forms.bootstrap import FormActions


class ProfileForm(ModelForm):
    """
    Create form class based on Profile model
    Reference for the code in the link below:
    https://github.com/Code-Institute-Submissions/andy-guttridge-song-mates
    """
    def __init__(self, *args, **kwargs):
        """
        Init form using crispy forms FormHelper for form layout
        """
        super(ProfileForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_tag = False
        self.helper.form_class = 'form-horizontal'
        self.helper.field_class = 'col-md-12'
        self.helper.layout = Layout(
            HTML('<div class = "text-start">'),
            Field('brief_bio', css_class='bkgnd-color-1 txt-color-2'),
            Field('profile_image', css_class='bkgnd-color-1 txt-color-2'),
            # Approach to using a HTML helper class to display an image from
            # the data base in the form from
            # https://stackoverflow.com/questions/21076248/imagefield-preview-in-crispy-forms-layout

            HTML('</div>'),
            FormActions(
                Submit('profile-form-cancel', 'Cancel',
                       css_class='btn btn-primary'),
                Submit('profile-form-submit', 'Submit',
                       css_class='btn btn-warning')
            )
        )

    class Meta:
        model = Profile
        fields = ['brief_bio', 'profile_image']
        labels = {
            'brief_bio': 'Brief Bio',
            'profile_image': 'Profile Image',
        }
        # Specify help text for form fields
        help_texts = {
            'brief_bio': 'Maximum 500 characters',
        }

        # Specify a custom widget for the image field
        widgets = {
            'image': FileInput
        }
