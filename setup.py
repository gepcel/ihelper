# -*- coding: utf-8 -*-
# ----------------------------------------------------------------------------
# Copyright © 2021, gepcel
#
# Licensed under the terms of the MIT license
# ----------------------------------------------------------------------------
"""
ihelper: A spyder plugin to get help information from ipython console in editor.
"""
from setuptools import find_packages
from setuptools import setup
import os

def get_version():
    with open("ihelper/__init__.py", encoding='utf-8') as f:
        lines = [l for l in f.readl().splitlines() if "__version__" in l]
        if lines:
            version = lines[0].split("=")[1].strip()
            version = version.replace("'", '').replace('"', '')
            return version

setup(
    # See: https://setuptools.readthedocs.io/en/latest/setuptools.html
    name="ihelper",
    version=get_version(),
    author="gepcel",
    author_email="gepcelway@gmail.com",
    description="A spyder plugin to get help information from ipython console in editor.",
    license="MIT license",
    url="https://github.com/gepcel/ihelper",
    python_requires='>= 3.7',
    install_requires=[
        "qtpy",
        "qtawesome",
    ],
    packages=find_packages(),
    entry_points={
        "spyder.plugins": [
            "ihelper = ihelper.spyder.plugin:IHelper"
        ],
    },
    classifiers=[
        "Operating System :: MacOS",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Education",
        "Intended Audience :: Science/Research",
        "Intended Audience :: Developers",
        "Topic :: Scientific/Engineering",
    ],
)
