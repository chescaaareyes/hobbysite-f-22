from django import forms

from .models import Comment, Thread


class ThreadForm(forms.ModelForm):

    class Meta:
        model = Thread
        fields = "__all__"


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = "__all__"
