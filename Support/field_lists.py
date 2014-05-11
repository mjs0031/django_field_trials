""" Python Package Support """
import re

""" Django Package Support """
from django.core.validators import EMPTY_VALUES
from django.forms import ValidationError
from django.forms.fields import Field, RegexField, Select, CharField
from django.utils.encoding import smart_text
from django.utils.translation import ugettext_lazy as _

""" Internal Package Support """
# Not Applicable


"""
 Support/field_lists.py
 Author:      Matthew J Swann
 Version:     1.0
 Last Update: 2014-05-11
 Update by:   Matthew J Swann
 
 This file contains the set of field lists for Project Knollgrass.
 
 These lists are organized alphabetically by name, not package.
 """

phone_digits_re = re.compile(r'^(?:1-?)?(\d{3})[-\.]?(\d{3})[-\.]?(\d{4})$')
ssn_re          = re.compile(r"^(?P<area>\d{3})[-\ ]?(?P<group>\d{2})[-\ ]?(?P<serial>\d{4})$")


class USZipCodeField(RegexField):
    """"
    A form field that validates input as a U.S. ZIP code. Valid formats are
    XXXXX or XXXXX-XXXX.

    .. versionadded:: 1.1

    Whitespace around the ZIP code is accepted and automatically trimmed.
    """
    default_error_messages = {
        'invalid': _('Enter a zip code in the format XXXXX or XXXXX-XXXX.'),
    }

    def __init__(self, max_length=None, min_length=None, *args, **kwargs):
        super(USZipCodeField, self).__init__(r'^\d{5}(?:-\d{4})?$',
                                             max_length, min_length, *args, **kwargs)

    def to_python(self, value):
        value = super(USZipCodeField, self).to_python(value)
        return value.strip()


class USPhoneNumberField(CharField):
    """
    A form field that validates input as a U.S. phone number.
    """
    default_error_messages = {
        'invalid': _('Phone numbers must be in XXX-XXX-XXXX format.'),
    }

    def clean(self, value):
        super(USPhoneNumberField, self).clean(value)
        if value in EMPTY_VALUES:
            return ''
        value = re.sub('(\(|\)|\s+)', '', smart_text(value))
        m = phone_digits_re.search(value)
        if m:
            return '%s-%s-%s' % (m.group(1), m.group(2), m.group(3))
        raise ValidationError(self.error_messages['invalid'])
    