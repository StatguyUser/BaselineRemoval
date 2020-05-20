from distutils.core import setup

setup(
    name='Baseline',
    version='0.0.1',
    description='Implementation of Modified polyfit method and IModPoly method for baseline correction',
    author='StatguyUser',
    url='https://github.com/StatguyUser/Baseline',
    install_requires=['numpy','sklearn'],
    download_url='',
    py_modules=["Baseline"],
    package_dir={'':'src'},
)
