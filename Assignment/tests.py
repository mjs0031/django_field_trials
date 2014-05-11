""" Python Package Support """
import calendar
from datetime import date, datetime, time, timedelta
from decimal import Decimal

""" Django Package Support """
from django.test import TestCase
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError, PermissionDenied

""" Internal Package Support """
#from Assignment.models import Test


"""
 Assignment/tests.py
 Author:      Matthew J Swann
 Version:     1.0
 Last Update: 2014-05-11
 Update By:   Matthew J Swann
 
 Test harness for Assignment Package.
 
     All tests being with 'test' and are followed by table name.
     
     First number section is for function block tagging.
     Second number section is for test number within block.
     Third number is for happy/sad path testing.
     
     All tests end explicitly with block tag name matching function. 
 """



class Test(TestCase):
         
    def test_general_package_40_01_00_cancel_assignment(self):
        pass
        