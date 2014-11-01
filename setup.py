#!/usr/bin/env python

from setuptools import setup

setup(
    name='fleetmonger',

    version='1.0',

    description='Fleetmon API',

    author='Neil Freeman',

    author_email='contact@fakeisthenewreal.org',

    url='',

    packages=['fleetmonger'],

    install_requires=[
        'requests',
        'pytz'
    ],
)
