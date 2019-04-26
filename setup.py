#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import find_packages, setup

with open("README.rst") as readme_file:
    readme = readme_file.read()

setup(
    author="Niels Lemmens",
    author_email="draso.odin@gmail.com",
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
    ],
    description="List of all countries with names and ISO 3166-1 codes "
    "in all languages",
    license="MIT license",
    long_description=readme,
    include_package_data=True,
    keywords="country_list",
    name="country_list",
    packages=find_packages(include=["country_list"]),
    url="https://github.com/bulv1ne/country_list",
    version="0.1.2",
    zip_safe=False,
)
