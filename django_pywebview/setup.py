# -*- coding: utf-8 -*-

import os
from setuptools import setup
import sys
import subprocess

def tree(src):
    return [(root, map(lambda f: os.path.join(root, f), files)) for (root, dirs, files) in os.walk(os.path.normpath(src))]

# Get Python path - works in virtualenv, too
python_path = subprocess.Popen([
    "which",
    "python"],
    stdout=subprocess.PIPE,
    stderr=subprocess.STDOUT,
    close_fds=True).communicate()[0].rstrip().decode("utf-8")
# print(python_path)
python_path = os.path.dirname(os.path.dirname(python_path))
django_admin_path = os.path.join(python_path, 'lib', 'python3.6',
                                 'site-packages', 'django', 'contrib', 'admin')

APP = ['start_django_and_cherrypy.py']
DATA_FILES = ['static', 'mediafiles', 'db.sqlite3',
              os.path.join(django_admin_path, 'templates'),
              os.path.join(django_admin_path, 'static'),
              ]
OPTIONS = {'argv_emulation': False,
           'strip': True,
           'iconfile': '../PyBrowse.icns',
           'packages':["django", "django_pywebview", "main", "cherrypy"],
           'includes': ['WebKit', 'Foundation', 'webview', 'cherrypy',
                        'packaging', 'six', 'packaging.version',
                        'packaging.specifiers', 'packaging.requirements',
                        'paste', 'requests'],
           'plist': {
               'CFBundleIdentifier': "com.moosystems.pybrowse",
               'CFBundleName': "PyBrowse",
               'CFBundleVersion': '1001',
               'CFBundleShortVersionString': '1.0',
               'NSHumanReadableCopyright': 'Copyright 2016 moosystems'}
           }

setup(
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)
