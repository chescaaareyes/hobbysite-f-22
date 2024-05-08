from django import forms

from .models import Commission, Job, JobApplication

from django.forms import modelformset_factory, BaseFormSet


class CommissionForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(CommissionForm, self).__init__(*args, **kwargs)
        self.fields["author"].disabled = True

    class Meta:
        model = Commission
        fields = "__all__"
        

class RequiredFormSet(BaseFormSet):
    def __init__(self, *args, **kwargs):
        super(RequiredFormSet, self).__init__(*args, **kwargs)
        for form in self.forms:
            form.empty_permitted = False


JobFormSet = modelformset_factory(Job, fields=("role", "manpower", "status"), extra=1, formset=RequiredFormSet)


class JobApplicationForm(forms.ModelForm):
    class Meta:
        model = JobApplication
        fields = []
