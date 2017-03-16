from django import forms
from django.utils import timezone
from django.forms import ModelForm, Textarea
from .models import *
from submissions_app import validate

"""
The different types of applications
"""
app_type_choices = [(1,"Esports"),
                    (2,"Community Related (ie: stats)"),
                    (3,"For laughs and giggles")]

class SubmitAppForm(forms.ModelForm):

    email_address = forms.CharField(label="email_address", required=False, validators = [validate.validate_form_email])
    member1 = forms.CharField(label="member1", required=False, validators = [validate.validate_non_required_form_email])
    member2 = forms.CharField(label="member2", required=False, validators = [validate.validate_non_required_form_email])
    member3 = forms.CharField(label="member3", required=False, validators = [validate.validate_non_required_form_email])
    app_type = forms.ChoiceField(choices=app_type_choices, widget=forms.Select(attrs={'class': "form-control"}))

    class Meta:
        model = Submission
        
        fields = [
        			'name', 
			        'app_url',
                    'app_type',
			        'description',
			        'code_url',
			        'thumbnail_url',
			        'first_name',
			        'last_name',
			        'email_address',
			        'member1',
			        'member2',
			        'member3'
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
