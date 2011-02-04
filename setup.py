#!/usr/bin/env python
from distutils.core import setup
<<<<<<< HEAD
from content_base import VERSION
=======
from content_base import import VERSION
>>>>>>> 525c1831fead9fb18081770c785f7d6dd383b357
path='content_base'

setup(name=path,
      version=VERSION,
      description='content abstract class',
      long_description = open('README.txt').read(),
      author='NORD',
      author_email='nordmenss@gmail.com',
      url='https://github.com/nordmenss/django-content-base',
      packages=[ path, ],

      classifiers=(
          'Development Status :: 2 - Pre-Alpha',
          'Environment :: Console',
          'License :: OSI Approved :: GNU General Public License (GPL)',
          'Operating System :: POSIX',
          'Operating System :: Unix',
          'Programming Language :: Python',
        ),
      license="GPL"
     )