from django import forms
from .models import WorkSheet

class DateInput(forms.DateInput):
    input_type = 'date'

class WorkSheetForm(forms.ModelForm):
    class Meta:
        model = WorkSheet
        fields = ['site','oppera','cs_date','cs_comments','cs_pics_link',]
        widgets = {'cs_date':DateInput}

class UpdateWorkForm(forms.ModelForm):
    class Meta:
        model = WorkSheet
        fields = [
            'pendings_date',
            'pend_type',
            'claim_date',
            'asp',
            'claim_pending_comments',
            'ca_date',
            'ca_comments',
            'ca_pics_link',
            'closed',
        ]
        widgets = {'pendings_date':DateInput,'claim_date':DateInput,'ca_date':DateInput,}







'''class UpdateWorkForm(forms.ModelForm):
    class Meta:
        model = WorkSheet
        fields = [
            'pendings_date','pend_type','claim_date','asp','claim_pending_comments','ca_date','ca_comments','ca_pics_link','closed',
        ]
        pendings_date = forms.DateField(
            widget = forms.DateInput(format='%m/%d/%Y', attrs={'class':'datepicker'}),
            input_formats = ('%m/%d/%Y')
        )
        claim_date = forms.DateField(
            widget = forms.DateInput(format='%m/%d/%Y', attrs={'class':'datepicker'}),
            input_formats = ('%m/%d/%Y')
        )'''