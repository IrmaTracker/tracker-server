from django import forms
from tracker.models import Person


class PersonForm(forms.ModelForm):
    age = forms.IntegerField(required=False)
    district = forms.CharField(required=False, help_text="I.e. Cupecoy, Cayhill, etc.,")
    extra_info = forms.CharField(widget=forms.Textarea, required=False)
    requester_name = forms.CharField(required=True, label="Your name")
    requester_email = forms.EmailField(required=False, label="Your email")
    requester_fb = forms.URLField(required=False, label="Your Facebook Profile")
    requester_number = forms.CharField(required=False, label="Your number")
    missing_since = forms.CharField(required=False)

    def validate_marked_safe_by_presence(self):
        if self.cleaned_data['safe'] and not self.cleaned_data['marked_safe_by']:
            self.add_error('marked_safe_by', 'Please provide your name.')

    def clean(self):
        super(PersonForm, self).clean()
        self.validate_marked_safe_by_presence()

    class Meta:
        model = Person
        fields = (
                'name',
                'age',
                'missing_since',
                'district',
                'address',
                'phonenumber',
                'safe',
                'marked_safe_by',
                'extra_info',
                'requester_name',
                'requester_email',
                'requester_fb',
                'requester_number'
        )


class MarkSafePersonForm(forms.ModelForm):
    name = forms.CharField(disabled=True)
    age = forms.IntegerField(disabled=True)
    missing_since = forms.CharField(disabled=True)
    address = forms.CharField(disabled=True)
    district = forms.CharField(disabled=True)
    phonenumber = forms.CharField(disabled=True)
    extra_info = forms.CharField(widget=forms.Textarea(), disabled=True)
    requester_name = forms.CharField(disabled=True)
    requester_email = forms.CharField(disabled=True)
    requester_fb = forms.CharField(disabled=True)
    requester_number = forms.CharField(disabled=True)

    class Meta:
        model = Person
        fields = (
            'name',
            'age',
            'missing_since',
            'district',
            'address',
            'phonenumber',
            'safe',
            'marked_safe_by',
            'extra_info',
            'requester_name',
            'requester_email',
            'requester_fb',
            'requester_number'
        )
