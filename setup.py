from setuptools import setup
import os
import sys

if sys.version_info[0] < 3:
    with open('README.rst') as f:
        long_description = f.read()
else:
    with open('README.rst', encoding='utf-8') as f:
        long_description = f.read()


setup(
    name='BaselineCorrection',
    version='0.0.1',
    description='Implementation of Modified polyfit method and IModPoly method for baseline correction',
    author='StatguyUser',
    url='https://github.com/StatguyUser/BaselineCorrection',
    install_requires=['numpy','sklearn'],
    download_url='https://github.com/StatguyUser/BaselineCorrection.git',
    py_modules=["BaselineCorrection"],
    package_dir={'':'src'},
)
