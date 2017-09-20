###############################################################################
# -*- coding: utf-8 -*-
# Order: A tool to characterize the local structure of liquid water 
#        by geometric order parameters
# 
# Authors: Pu Du
# 
# Released under the MIT MIT License
###############################################################################

from setuptools import setup, find_packages
import order
import os

def readme():
    with open('README.rst') as f:
        return f.read()

setup(
    name='iOrder',
    version='0.0.2',
    description='A tool to characterize the local structure of liquid water by geometric order parameters',
    long_description=readme(),
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Environment :: Console",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Topic :: Scientific/Engineering :: Chemistry",
        "Topic :: Scientific/Engineering :: Physics",
    ],
    keywords=['order parameter', 'water structure'],
    author='Pu Du',
    author_email='pudugg@gmail.com',
    maintainer='Pu Du',
    maintainer_email='pudugg@gmail.com',
    url='https://github.com/ipudu/order',
    license='MIT',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'order = order.order:command_line_runner',
        ]
    },
    install_requires=[
        'numpy',
        'six',
        'progress',
        'scipy',
        'matplotlib',
    ],
)
