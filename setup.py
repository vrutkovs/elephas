#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages
from pip.req import parse_requirements
from pip.download import PipSession


with open('README.rst') as readme_file:
    readme = readme_file.read()

pip_session = PipSession()
parsed_reqs = parse_requirements('requirements.txt', session=pip_session)
parsed_reqs_dev = parse_requirements('requirements_dev.txt', session=pip_session)
requirements = [str(x.req) for x in parsed_reqs]
test_requirements = [str(x.req) for x in parsed_reqs_dev]

setup(
    name='elephas',
    version='0.1.0',
    description="Elephas is a GTK+ client for Mastodon",
    long_description=readme,
    author="Vadim Rutkovsky",
    author_email='vrutkovs@redhat.com',
    url='https://github.com/vrutkovs/elephas',
    packages=find_packages(exclude=["*.tests", "*.tests.*", "tests.*", "tests"]),
    entry_points={
        'console_scripts': ['elephas=elephas.main:main'],
    },
    install_requires=requirements,
    license="GNU General Public License v3",
    keywords='elephas',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    zip_safe=False,
    test_suite='tests',
    tests_require=test_requirements
)
