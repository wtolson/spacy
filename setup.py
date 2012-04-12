#!/usr/bin/env python
# -*- coding: utf-8 -*-

from distutils.core import setup

setup(
    name='spacy',
    version='1.0.0',
    author='William Trevor Olson',
    author_email='wtolson@gmail.com',
    py_modules=[
        'spacy'
    ],
    scripts=[],
    url='https://github.com/wtolson/spacy',
    license='LICENSE.txt',
    description='A utility for reading in plain text data files with attached dtypes to numpy.',
    long_description=open('README.md').read(),
    install_requires=[
        'PyYAML',
        'numpy'
    ]
)
