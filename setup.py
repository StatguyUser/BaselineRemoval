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
    name='BaselineRemoval',
    version='0.0.2',
    description='Implementation of Modified polyfit method and IModPoly method for baseline BaselineRemoval',
    long_description=long_description,
    long_description_content_type='text/markdown',  # This is important!
    author='StatguyUser',
    url='https://github.com/StatguyUser/BaselineRemoval',
    install_requires=['numpy','sklearn'],
    download_url='https://github.com/StatguyUser/BaselineRemoval.git',
    py_modules=["BaselineRemoval"],
    package_dir={'':'src'},
)
