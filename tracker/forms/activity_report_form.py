from django import forms
from tracker.models import ActivityReport


class ActivityReportForm(forms.ModelForm):
    reporter_number = forms.CharField(max_length=75, required=True)

    class Meta:
        model = ActivityReport
        fields = (
            'type',
            'district',
            'address',
            'content',
            'reporter_name',
            'reporter_email',
            'reporter_number'
        )