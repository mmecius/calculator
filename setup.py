from setuptools import setup
import pathlib
import pkg_resources

with pathlib.Path('requirements.txt').open() as requirements_txt:
    install_requires = [
        str(requirement)
        for requirement
        in pkg_resources.parse_requirements(requirements_txt)
    ]

setup(name='Calculator',
version='0.1',
description='calculator with basic operations',
url='https://github.com/mmecius/calculator',
author='Tomas',
author_email='tmecius@gmail.com',
license='MIT',
install_requires=install_requires,
packages=['calculator'],
zip_safe=False)