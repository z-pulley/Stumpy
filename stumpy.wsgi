#!/usr/bin/env python
import os
import os.path
import sys
parent_dir=os.path.normpath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(parent_dir)
this_dir=os.path.normpath(os.path.join(os.path.dirname(__file__), '.'))
sys.path.append(this_dir)
os.environ['DJANGO_SETTINGS_MODULE'] = 'Stumpy.settings'
import django.core.handlers.wsgi
application=django.core.handlers.wsgi.WSGIHandler()
