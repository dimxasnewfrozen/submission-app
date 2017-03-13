from django import forms
from django.utils import timezone
from django.forms import ModelForm, Textarea
from .models import *
from submissions_app import validate

class SubmitAppForm(forms.ModelForm):

    email_address = forms.CharField(label="email_address", required=False, validators = [validate.validate_form_email])

    class Meta:
        model = Submission
        
        fields = [
        			'name', 
			        'app_url',
			        'description',
			        'code_url',
			        'thumbnail_url',
			        'first_name',
			        'last_name',
			        'email_address',
			        'member1',
			        'member2',
			        'member3',
			        'member4',
			        'member5'
			    ]

        widgets = {
            'description': Textarea(attrs={'cols': 5, 'rows': 5}),
        }

    def __init__(self, *args, **kwargs):
        super(SubmitAppForm, self).__init__(*args, **kwargs)

    def save(self, commit=True):

        app = super(SubmitAppForm, self).save(commit=False)

        app.date_created = timezone.now()
        app.last_update = timezone.now()

        if commit:
            app.save()
        return app
