# -*- coding: utf-8 -*-
"""
Created on Tue Mar 30 14:36:44 2021

@author: Emmett
"""
# import setuptools
from distutils.core import setup
from Cython.Build import cythonize

setup(ext_modules= cythonize('example.pyx'))