# -*- coding: utf-8 -*-

import os
from setuptools import setup, Command


DESCRIPTION = 'Highlight Python tracebacks in standard input.'


def get_version():
    with open('tracey/__init__.py') as f:
        for line in f:
            if line.startswith('__version__'):
                return eval(line.split('=')[-1])


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name='tracey',
    version=get_version(),
    author='Kirill Borisov',
    author_email='lensvol@gmail.com',
    description=DESCRIPTION,
    license='MIT',
    keywords='tracey traceback pygments',
    url='https://github.com/lensvol/tracey',
    packages=['tracey'],
    long_description=DESCRIPTION,
    install_requires=[
        'Pygments==2.1.3',
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Topic :: Utilities',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Operating System :: POSIX',
    ],
    entry_points={
        'console_scripts': [
            'tracey = tracey.main:processor',
        ],
    },
)
