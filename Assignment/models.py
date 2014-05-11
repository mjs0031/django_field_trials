""" Python Package Support """
from itertools import chain
from operator import attrgetter
from datetime import date, datetime, time, timedelta
from decimal import Decimal
from pytz import timezone
import calendar

""" Django Package Support """
from django.db import models
from django.core.exceptions import ValidationError, PermissionDenied
from django.core.validators import RegexValidator
from django.utils.timezone import utc

""" Internal Package Support """
# not applicable


"""
Assignment/models.py

Author:      Matthew J Swann
Version:     1.0
Last Update: 2014-05-11
Update By:   Matthew J Swann 

"""

class Event(models.Model):
    pass
    
