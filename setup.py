#!/usr/bin/env python
from distutils.core import setup
import os
from content_base import VERSION
path='content_base'

long_description = open('README.txt').read()
packages, data_files = [], []
root_dir = os.path.dirname(__file__)
if root_dir:
    os.chdir(root_dir)

for dirpath, dirnames, filenames in os.walk(path):
    # Ignore dirnames that start with '.'
    for i, dirname in enumerate(dirnames):
        if dirname.startswith('.'): del dirnames[i]
    if '__init__.py' in filenames:
        pkg = dirpath.replace(os.path.sep, '.')
        if os.path.altsep:
            pkg = pkg.replace(os.path.altsep, '.')
        packages.append(pkg)
    elif filenames:
        prefix = dirpath[(len(path)+1):] # Strip "admin_tools/" or "admin_tools\"
        for f in filenames:
            data_files.append(os.path.join(prefix, f))

setup(
    name='django-content-base',
    version='0.0',
    description='content abstract class',
    long_description=long_description,
    author='NORD',
    author_email='nordmenss@gmail.com',
    url='https://github.com/nordmenss/django-content-base',
    package_dir={path: path},
    packages=packages,
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
