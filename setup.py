#!/usr/bin/env python3

from setuptools import setup
from fastlog.version import __version__


setup(
    name="fastlog",
    version=__version__,
    description="A simple CLI timer to calculate fasting zones.",
    long_description=open('README.md', encoding="utf-8-sig").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/vkostyanetsky/Fastlog",
    license="MIT",
    python_requires=">=3.7",
    packages=["fastlog"],
    install_requires=["ConsoleMenu~=1.0.1", "PyYAML~=6.0"],
    entry_points={"console_scripts": [
        "fastlog=fastlog.fastlog:main"
    ]},
    author="Vlad Kostyanetsky",
    author_email="vlad@kostyanetsky.me",
    # https://pypi.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Console",
        "Intended Audience :: End Users/Desktop",
        "License :: OSI Approved :: MIT License",
        "Operating System :: POSIX",
        "Programming Language :: Python :: 3.7",
        "Topic :: Utilities"
    ],
    keywords="fasting fast"
)
