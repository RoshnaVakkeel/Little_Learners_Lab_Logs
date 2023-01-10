from django import forms
from django_summernote.widgets import SummernoteWidget
from .models import Post, Comment


class UploadFileForm(forms.Form):
    title = forms.CharField(max_length=100)
    file = forms.FileField()

    class Meta:
        model = Post
        fields = ['image']


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
            'description': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Add a description about the experiment'}),
            'items_required': SummernoteWidget(attrs={
                'class': 'form-control',
                'placeholder': 'Add list of items required'}),
            'steps_to_perform': SummernoteWidget(attrs={
                'class': 'form-control',
                'placeholder': 'Please enter step by step procedure'}),
        }



class CommentForm(forms.ModelForm):
    ''' Comment form '''
    body = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'md-textarea form-control',
        'placeholder': 'Please enter your comment here..',
        'rows': '6',
    }))
    
    class Meta:
        ''' From comment model  choose which fields to display '''
        model = Comment
        fields = ('body',)
 
