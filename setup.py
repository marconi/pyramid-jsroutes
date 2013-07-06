#!/usr/bin/env python

import os
import sys
import jsroutes

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist register upload')
    sys.exit()

packages = ['jsroutes']
requires = ['Pyramid']

setup(
    name='pyramid-jsroutes',
    version=jsroutes.__version__,
    packages=packages,
    license=open('LICENSE.txt').read(),
    description='A pyramid routes composer for javascript.',
    long_description=open('README.md').read() + '\n\n' +
                     open('HISTORY.rst').read(),
    author='Marconi Moreto',
    author_email='caketoad@gmail.com',
    url='https://github.com/marconi/pyramid-jsroutes',
    zip_safe=False,
    package_data={'': ['LICENSE.txt']},
    install_requires=requires
)
