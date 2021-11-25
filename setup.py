#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import find_packages, setup  # type: ignore

with open("README.rst") as readme_file:
    readme = readme_file.read()

setup(
    author="Niels Lemmens",
    author_email="draso.odin@gmail.com",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
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
    version="1.0.0",
    zip_safe=False,
)
