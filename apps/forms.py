from django import forms
from django.utils import timezone
from django.forms import ModelForm, Textarea
from .models import *
from submissions_app import validate
from django.core.validators import URLValidator

"""
The different types of applications
"""
app_type_choices = [(1,"Esports"),
                    (2,"Community Related (ie: stats)"),
                    (3,"For laughs and giggles")]

class SubmitAppForm(forms.ModelForm):

    first_name = forms.CharField(label="first_name", required=True)
    last_name = forms.CharField(label="last_name", required=True)

    name = forms.CharField(label="name", required=True)
    code_url = forms.CharField(label="code_url", required=True, validators=[URLValidator()])
    app_url = forms.CharField(label="app_url", required=True, validators=[URLValidator()])
    thumbnail_url = forms.CharField(label="thumbnail_url", required=False, validators=[URLValidator()])

    description = forms.CharField(label="description", required=True, widget=forms.Textarea)
    comments = forms.CharField(label="comments", widget=forms.Textarea, required=False)

    email_address = forms.CharField(label="email_address", required=True, validators = [validate.validate_form_email])
    member1 = forms.CharField(label="member1", required=False, validators = [validate.validate_form_email])
    member2 = forms.CharField(label="member2", required=False, validators = [validate.validate_form_email])
    member3 = forms.CharField(label="member3", required=False, validators = [validate.validate_form_email])
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
			        'member3',
                    'comments'
			    ]

        widgets = {
            'description': Textarea(attrs={'cols': 5, 'rows': 5}),
        }

    def __init__(self, *args, **kwargs):
        super(SubmitAppForm, self).__init__(*args, **kwargs)
        self.fields['first_name'].error_messages['required'] = '* First name is required!'
        self.fields['last_name'].error_messages['required'] = '* Last name is required!'
        self.fields['email_address'].error_messages['required'] = '* Email address is required!'
        self.fields['name'].error_messages['required'] = '* Application name is required!'
        self.fields['description'].error_messages['required'] = '* Application description is required!'
        self.fields['code_url'].error_messages['required'] = '* Github url is required!'

    def save(self, commit=True):

        app = super(SubmitAppForm, self).save(commit=False)

        app.date_created = timezone.now()
        app.last_update = timezone.now()

        if commit:
            app.save()
        return app
