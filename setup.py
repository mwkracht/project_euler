from setuptools import setup, find_packages
from setuptools.command.test import test as TestCommand

import os
import sys


PKG_NAME = 'project_euler'


def get_init_variable(pkg_name, variable_name):
    """
    Grab variable values from __init__.py.
    This avoids an import of pkg_name which may break installation if pacakges from
    install_requires have not yet been installed.
    """
    init = os.path.join(os.path.dirname(__file__), pkg_name, '__init__.py')
    version_line = list(filter(lambda l: l.startswith(variable_name), open(init)))[0]
    return eval(version_line.split('=')[-1])


def get_install_requirements(requirements_file):
    """Return list of requirements from provided requirements file."""
    with open(os.path.join(os.path.dirname(__file__), requirements_file)) as req_fd:
        return [
            requirement
            for requirement in req_fd.readlines()
            if requirement and not requirement.startswith('#')
        ]


setup(
    name=PKG_NAME,
    version=get_init_variable(PKG_NAME, '__version__'),
    author=get_init_variable(PKG_NAME, '__author__'),
    author_email=get_init_variable(PKG_NAME, '__email__'),
    url='https://github.com/mwkracht/project_euler',
    description='Python solutions to Project Euler Problems.',
    packages=find_packages(exclude=['tests*']),
    install_requires=get_install_requirements('requirements.txt'),
    scripts=['bin/project_euler'],
)