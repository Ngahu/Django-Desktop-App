from setuptools import setup
import os

try:
    from cheroot.wsgi import Server as WSGIServer
except ImportError:
    from cherrypy.wsgiserver import CherryPyWSGIServer as WSGIServer


APP = ['main.py']

def tree(src):
    return [(root, map(lambda f: os.path.join(root, f), files)) for (root, dirs, files) in os.walk(os.path.normpath(src))]

DATA_FILES = tree('public')

OPTIONS = {'argv_emulation': True,
           'iconfile': './PyBrowse.icns',
           'packages': ['cherrypy'],
           'includes': ['six', 'packaging', 'packaging.version',
                        'packaging.specifiers', 'packaging.requirements'],
           'plist': {
                'CFBundleIdentifier': "Desktop App",
                'CFBundleName': "PyBrowse",
                'CFBundleVersion': '1001',
                'CFBundleShortVersionString': '1.0',
               'NSHumanReadableCopyright': 'Copyright 2019 Ngahu'
            }}

setup(
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app', ]
)