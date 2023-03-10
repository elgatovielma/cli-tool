from setuptools import find_packages
from setuptools import setup

REQUIRED_PACKAGES = [
    'click==7.1.2',
    'prettytable',
    'lorem'
]
 
setup(
    name='cli_todo', 
    version='0.1', 
    install_requires=REQUIRED_PACKAGES,
    packages=find_packages(), # Automatically find packages within this directory or below.
    include_package_data=True, # if packages include any data files, those will be packed together.
    description='CLI tool to communicate with the TODO app',
    entry_points='''
        [console_scripts]
        todo=cli_todo.cli:cli
    ''' 
)