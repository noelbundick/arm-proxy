#!/usr/bin/env python

from codecs import open
from setuptools import setup, find_packages

try:
    from azure_bdist_wheel import cmdclass
except ImportError:
    from distutils import log as logger

    logger.warn("Wheel is not available, disabling bdist_wheel hook")

VERSION = "0.0.1"

# The full list of classifiers is available at
# https://pypi.python.org/pypi?%3Aaction=list_classifiers
CLASSIFIERS = [
    "Development Status :: 2 - Pre-Alpha",
    "Intended Audience :: Developers",
    "Intended Audience :: System Administrators",
    "Programming Language :: Python",
    "Programming Language :: Python :: 3",
    "Programming Language :: Python :: 3.6",
    "Programming Language :: Python :: 3.7",
    "Programming Language :: Python :: 3.8",
    "License :: OSI Approved :: MIT License",
]

DEPENDENCIES = ["azure-cli-core", "pyngrok"]

with open("../../README.md", "r", encoding="utf-8") as f:
    README = f.read()

setup(
    name="arm-proxy",
    version=VERSION,
    description="Microsoft Azure Command-Line Tools ARM Proxy Extension",
    author="Noel Bundick",
    author_email="noelbundick@gmail.com",
    url="https://github.com/noelbundick/arm-proxy",
    long_description=README,
    license="MIT",
    classifiers=CLASSIFIERS,
    packages=find_packages(),
    install_requires=DEPENDENCIES,
    package_data={"azext_arm_proxy": ["azext_metadata.json"]},
)
