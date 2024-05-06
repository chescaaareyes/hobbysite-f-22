from django import forms

from .models import Comment, Thread, ThreadCategory


class ThreadForm(forms.ModelForm):

    class Meta:
        model = Thread
        fields = "__all__"
