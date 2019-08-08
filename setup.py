from os.path import join, dirname
from setuptools import setup, find_packages
import importlib

fakepypiproject = importlib.import_module("fake-pypi-project")

setup(
    name='fake-pypi-project',
    version=fakepypiproject.__version__,
    packages=find_packages(),
    long_description=open(join(dirname(__file__), 'README.txt')).read(),

    entry_points={
       'console_scripts': [
           'fake-pypi-project = fakepypiproject.core:print_message',
           'serve = fakepypiproject.web:run_server',
           ]
    },

    install_requires=[
        'Flask>=0.12.2',
        'nose>=1.3.7',
        'coverage>=4.5.3'
    ],

    include_package_data=True,

    test_suite='tests',
    )