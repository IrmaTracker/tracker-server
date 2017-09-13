from django import forms
from tracker.models import Area


class AreaForm(forms.ModelForm):

    class Meta:
        model = Area
        fields = ('name',)