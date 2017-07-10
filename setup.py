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

setup(
    name='Order',
    version='0.1',
    description='',
    long_description='',
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Topic :: Documentation",
    ],
    keywords='Order',
    author='Pu Du',
    author_email='pudugg@gmail.com',
    maintainer='Pu Du',
    maintainer_email='pudugg@gmail.com',
    url='',
    license='MIT',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'order = order.order:command_line_runner',
        ]
    },
    install_requires=[
        'numpy',
    ],
)