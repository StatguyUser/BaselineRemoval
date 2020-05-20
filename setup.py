from setuptools import setup

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
