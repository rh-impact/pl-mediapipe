from os import path
from setuptools import setup

with open(path.join(path.dirname(path.abspath(__file__)), 'README.rst')) as f:
    readme = f.read()

setup(
    name             = 'mediapipe',
    version          = '0.1',
    description      = 'An app to track brain scans with most movement',
    long_description = readme,
    author           = 'olivelakra',
    author_email     = 'olakra@redhat.com',
    url              = 'http://wiki',
    packages         = ['mediapipe'],
    install_requires = ['chrisapp'],
    test_suite       = 'nose.collector',
    tests_require    = ['nose'],
    license          = 'MIT',
    zip_safe         = False,
    python_requires  = '>=3.6',
    entry_points     = {
        'console_scripts': [
            'mediapipe = mediapipe.__main__:main'
            ]
        }
)
