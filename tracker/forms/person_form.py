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
