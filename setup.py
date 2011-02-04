#!/usr/bin/env python
from distutils.core import setup
import os
from content_base import VERSION
path='content_base'

long_description = open('README.txt').read()
packages, data_files = [], []

setup(
    name='django-content-base',
    version='0.0',
    description='content abstract class',
    long_description=long_description,
    author='NORD',
    author_email='nordmenss@gmail.com',
    url='https://github.com/nordmenss/django-content-base',
    package_dir={path: path},
    package_data={path: data_files},
    classifiers=[
        'Development Status :: 0 - Alpha',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Framework :: Django',
    ],
    install_requires=[],
    zip_safe=False,
)
