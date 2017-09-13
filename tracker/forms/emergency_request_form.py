from django import forms
from tracker.models import EmergencyRequest
from tracker.constants import ADDITIONAL_PERSONS_TF


class EmergencyRequestForm(forms.ModelForm):
    additional_persons = forms.CharField(widget=forms.Textarea, label="Is there anyone else with you?", help_text=ADDITIONAL_PERSONS_TF, required=False)

    class Meta:
        model = EmergencyRequest
        fields = (
            'full_name',
            'address',
            'district',
            'contact_numbers',
            'additional_persons',
            'has_lod_situation',
            'has_24_hours',
            'has_injuries',
            'requires_medical_supplies',
            'medical_supplies',
            'days_of_water',
            'days_of_food',
            'has_rain_shelter',
            'request',
        )