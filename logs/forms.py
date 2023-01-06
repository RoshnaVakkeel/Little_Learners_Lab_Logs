from django import forms
from django.forms import ModelForm
from django_summernote.widgets import SummernoteWidget
from .models import Post

class PostForm(forms.ModelForm):
    ''' Django form to add lab_log posts '''
    class Meta:
        '''Get post model and choose which fields to display '''
        model = Post
        fields = ('title', 'author', 'description', 'items_required', 'steps_to_perform', 'image',)

        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Title'}),
            'author': forms.TextInput(attrs={
                'class': 'form-control',
                'value': '',
                'id': 'author_field',
                'type': 'hidden'}),
            'description': SummernoteWidget(attrs={
                'class': 'form-control',
                'placeholder': 'Add a description about the experiment'}),
            'items_required': SummernoteWidget(attrs={
                'class': 'form-control',
                'placeholder': 'Add list of items required to perform the experiment'}),
            'steps_to_perform': SummernoteWidget(attrs={
                'class': 'form-control',
                'placeholder': 'Please enter steo by step procedure of how the experiment was performed'}),
            
        }