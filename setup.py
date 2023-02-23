# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in blocos_dop/__init__.py
from blocos_dop import __version__ as version

setup(
	name="blocos_dop",
	version=version,
	description="Blocos BOP Checklist",
	author="Helkyd",
	author_email="hcesar@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
