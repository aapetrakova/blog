from django import forms
from .models import Comment


class CommentForm(forms.ModelForm):
    """Form for creating a comment"""
    class Meta:
        model = Comment
        fields = ('text',)
        widgets = {
            'text': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3
            }),
        }