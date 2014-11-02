#!/usr/bin/env python

from setuptools import setup

setup(
    name='fleetmonger',

    version='0.0.1',

    description='Fleetmon API wrapper',

    author='Neil Freeman',

    author_email='contact@fakeisthenewreal.org',

    url='https://github.com/fitnr/fleetmonger',

    packages=['fleetmonger'],

    install_requires=[
        'requests',
        'pytz'
    ],
)
