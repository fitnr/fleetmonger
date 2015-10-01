#!/usr/bin/env python

from setuptools import setup

def read_md(f):
    try:
        try:
            from pypandoc import convert
            return convert(f, 'rst')

        except ImportError:
            print("pypandoc not found, could not convert Markdown to RST")
            return open(f, 'r').read()

    except (IOError, RuntimeError):
        print("Could not read readme.md")
        return ''

setup(
    name='fleetmonger',

    version='0.0.3',

    description='Fleetmon API wrapper for ship data',

    long_description=read_md('readme.md'),

    author='Neil Freeman',

    author_email='contact@fakeisthenewreal.org',

    url='https://github.com/fitnr/fleetmonger',

    packages=['fleetmonger'],

    license='MIT',

    install_requires=[
        'requests >=2.4.1, <3',
        'pytz==2014.10'
    ],

    test_suite='tests',

    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.7',
        'Intended Audience :: Science/Research',
    ],
)
