from django import forms

from .models import Commission, Job, JobApplication

from django.forms import formset_factory, modelformset_factory


class CommissionForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(CommissionForm, self).__init__(*args, **kwargs)
        self.fields["author"].disabled = True

    class Meta:
        model = Commission
        fields = "__all__"


class JobForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = ["role", "manpower", "status"]


JobFormSet = modelformset_factory(
    Job, fields=("role", "manpower", "status"), extra=1
)


class JobApplicationForm(forms.ModelForm):
    class Meta:
        model = JobApplication
        fields = []
