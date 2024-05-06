from django import forms

from .models import Commission, Job, JobApplication

class CommissionForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(CommissionForm, self).__init__(*args, **kwargs)
        self.fields["author"].disabled = True
    class Meta:
        model = Commission
        fields = "__all__"

class JobApplicationForm(forms.ModelForm):
    class Meta:
        model = JobApplication
        fields = []