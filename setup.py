#!/usr/bin/env python
from setuptools import setup, find_packages
from content_base import VERSION
long_description = open('README.txt').read()

setup(
    name='django-content-base',
    version=VERSION,
    description='content abstract class',
    long_description=long_description,
    author='NORD',
    author_email='nordmenss@gmail.com',
    url='https://github.com/nordmenss/django-content-base',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
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
)
