#!/usr/bin/env python

import os
import sys

sys.path.append(os.path.join(os.environ['OPENSHIFT_REPO_DIR'], 'sample_project'))

os.environ['DJANGO_SETTINGS_MODULE'] = 'sample_project.settings'

virtenv = os.environ['OPENSHIFT_PYTHON_DIR'] + '/virtenv/'
virtualenv = os.path.join(virtenv, 'bin/activate_this.py')
try:
    execfile(virtualenv, dict(__file__=virtualenv))
except IOError:
    pass

#
# IMPORTANT: Put any additional includes below this line.  If placed above this
# line, it's possible required libraries won't be in your searchable path
# 

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()
