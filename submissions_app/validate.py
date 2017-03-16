from email_validator import validate_email, EmailNotValidError
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
from django.utils.translation import gettext as _

"""
Make sure the email address is valid
"""
def validate_form_email(value):
	try:
		v = validate_email(value) # validate and get info
		email = v["email"] # replace with normalized form
	except EmailNotValidError as e:
		raise ValidationError(_('* %(value)s is not a valid email address'),
			params={'value' : value}
			)

def validate_non_required_form_email(value):
	if value:
		try:
			v = validate_email(value) # validate and get info
			email = v["email"] # replace with normalized form
		except EmailNotValidError as e:
			raise ValidationError(_('* %(value)s is not a valid email address'),
				params={'value' : value}
				)

def validate_non_empty(value):
	if value:
		return True
	else:
		raise ValidationError(_('* field is required!'), params={'value' : value})