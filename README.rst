============
Country List
============

.. image:: https://github.com/bulv1ne/country_list/actions/workflows/python-app.yml/badge.svg
        :target: https://github.com/bulv1ne/country_list/actions/workflows/python-app.yml

.. image:: https://img.shields.io/pypi/v/country_list.svg
        :target: https://pypi.python.org/pypi/country_list

.. image:: https://pyup.io/repos/github/bulv1ne/country_list/shield.svg
        :target: https://pyup.io/repos/github/bulv1ne/country_list/
        :alt: Updates

.. image:: https://coveralls.io/repos/github/bulv1ne/country_list/badge.svg?branch=master
        :target: https://coveralls.io/github/bulv1ne/country_list?branch=master

.. image:: https://img.shields.io/badge/code%20style-black-000000.svg
        :target: https://github.com/psf/black

.. image:: https://sonarcloud.io/api/project_badges/measure?project=bulv1ne_country_list&metric=alert_status
        :target: https://sonarcloud.io/summary/new_code?id=bulv1ne_country_list
        :alt: Quality Gate Status


Features
--------

- List of all countries with names and ISO 3166-1 codes in all languages and all data formats.


Installation
------------

Install country_list by running:

.. code-block:: sh

    pip install country_list

Usage
-----

Get all available languages:

.. code-block:: python

    from country_list import available_languages

    for language in available_languages():
        print(language)

Get country names in english and swedish:

.. code-block:: python

    >>> from country_list import countries_for_language
    >>> # countries_for_language returns a list of tuples now, might be changed to an OrderedDict
    >>> countries = dict(countries_for_language('en'))
    >>> print(countries['GB'])
    'United Kingdom'
    >>> print(countries['SE'])
    'Sweden'
    >>> countries = dict(countries_for_language('sv'))
    >>> print(countries['GB'])
    'Storbritannien'
    >>> print(countries['SE'])
    'Sverige'

Get country codes from country name:

.. code-block:: python

    >>> from country_list import countries_for_language
    >>> # countries_for_language returns a list of tuples now, might be changed to an OrderedDict
    >>> country_names = {name: code for code, name in countries_for_language('en')}
    >>> print(country_names['United Kingdom'])
    'GB'
    >>> print(country_names['Sweden'])
    'SE'
    >>> country_names = {name: code for code, name in countries_for_language('sv')}
    >>> print(country_names['Storbritannien'])
    'GB'
    >>> print(country_names['Sverige'])
    'SE'

Credits
-------

This package contains the data files from `umpirsky/country-list`_.

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _`umpirsky/country-list`: https://github.com/umpirsky/country-list
.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage

License
-------

The project is licensed under the MIT license.
