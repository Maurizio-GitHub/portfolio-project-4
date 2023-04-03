from .models import Comment
from django import forms


class CommentForm(forms.ModelForm):
    # Telling our form what model to use and which fields to display
    class Meta:
        model = Comment
        fields = ('body',)
