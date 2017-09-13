from django import forms
from tracker.models import SupplyRequest


class SupplyRequestForm(forms.ModelForm):

    class Meta:
        model = SupplyRequest
        fields = (
            'full_name',
            'address',
            'district',
            'contact_numbers',
            'supplies',
            'quantity',
            'dropoff_instructions'
        )

        widgets = {
            'supplies': forms.CheckboxSelectMultiple
        }