#!/usr/bin/env python

from os.path import abspath, dirname, join
from setuptools import setup, find_packages
from sys import path

path.append(abspath(join(dirname(__file__), 'src')))

from switchboard import __VERSION__


def read(fname):
    return open(join(dirname(__file__), fname)).read()

# Installation Dependencies
install_dependencies = [
    'Django==1.6.5',
    'MySQL-python==1.2.5',
    'South==0.8.4',
    'requests==2.1.0',
    'Pillow==2.4.0',
    'twilio==3.6.6',
    'boto==2.29.1',
]

# Test Dependencies
test_dependencies = [
    'coverage == 3.6',
    'django-nose == 1.1',
    'nose-cover3 == 0.1.0',
    'nose == 1.2.1'
]

# Development Dependencies
development_dependencies = test_dependencies + [
    'ipdb == 0.7',
    'ipython == 0.13.1'
]

setup(
    name='switchboard',
    version=__VERSION__,
    author='Jamie Ingram',
    author_email='jamie.ingram@gmail.com',
    description='',
    long_description=read('README.rst'),
    zip_safe=False,
    package_dir={'': 'src'},
    packages=find_packages('src'),
    install_requires=install_dependencies,
    include_package_data=True,
    extras_require={
        'develop': development_dependencies,
        'test': test_dependencies,
    },
    classifiers=[
    ]
)
