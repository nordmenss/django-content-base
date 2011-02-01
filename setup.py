# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

long_description = open('README.txt').read()

setup(
    name='django-content-base',
    version='0.0',
    description='content abstract class',
    long_description=long_description,
    author='NORD',
    author_email='nordmenss@gmail.com',
    url='https://github.com/nordmenss/django-content-base',
    packages=find_packages(),
    classifiers=[
        'Development Status :: 0 - Alpha',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Framework :: Django',
    ],
    zip_safe=False,
)
