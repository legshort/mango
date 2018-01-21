import os
import sys

from setuptools import setup, find_packages

setup(
    name='mango',
    version='0.0.1',
    url='https://github.com/legshort/mango/',
    license='MIT',
    author='Jun Young Lee',
    author_email='legshort@gmail.com',
    description='Light wieght BDD Pattern',
    classifiers=[
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: BSD License',
    ],
    packages=find_packages(exclude=['tests']),
    long_description=open('README.md').read(),
)
