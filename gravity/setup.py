# -*- coding: utf-8 -*-
"""
Created on Wed Oct 13 22:50:12 2021

@author: Emmett
"""

from setuptools import setup
from Cython.Build import cythonize

setup(
    ext_modules=cythonize("gradient.pyx"),
    zip_safe=False,
)