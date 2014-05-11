""" Python Package Support """
# Not Applicable

""" Django Package Support """
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

""" Internal Package Support """
#from Control.decorators import active_knoll_required

""" Allow templates to request current URL """
from django.shortcuts import render_to_response
from django.template import RequestContext

"""
Assignment/models.py
Author:      Steven Motes
Version:     1.0
Last Update: 2014-05-11
Update By:   Peter Snelgrove

"""

