from .models import Posts
from django import forms


class PostsForm(forms.ModelForm):
    class Meta:
        model=Posts
        fields=['title', 'text', 'image', 'draft', 'publish']
