from django import forms
from tracker.models import SupplySharing
from tracker.constants import SHAREABLE_SUPPLIES_TF


class SupplySharingForm(forms.ModelForm):
    shareable_supplies = forms.CharField(widget=forms.Textarea, label="Supplies you want to share", help_text=SHAREABLE_SUPPLIES_TF)

    class Meta:
        model = SupplySharing
        fields = (
            'full_name',
            'address',
            'district',
            'contact_numbers',
            'shareable_supplies',
            'pickup_instructions'
        )