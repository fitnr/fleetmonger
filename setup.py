#!/usr/bin/env python

from setuptools import setup

setup(
    name='fleetmonger',

    version='0.0.2',

    description='Fleetmon API wrapper',

    author='Neil Freeman',

    author_email='contact@fakeisthenewreal.org',

    url='https://github.com/fitnr/fleetmonger',

    packages=['fleetmonger'],

    license='MIT',

    install_requires=[
        'requests==2.5.1',
        'pytz==2014.10'
    ],
)
