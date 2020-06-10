# -*- coding: utf-8 -*-

from setuptools import setup, find_packages


with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='Cryptography',
    version='0.0.1',
    description='Cryptography project for Codenation Challenge',
    long_description=readme,
    author='Jonatas Junior',
    author_email='junior.jonatas@gmail.com',
    url='https://github.com/juniorjonatas/cryptography',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)