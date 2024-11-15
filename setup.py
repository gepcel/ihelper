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

# from ihelper import __version__


setup(
    # See: https://setuptools.readthedocs.io/en/latest/setuptools.html
    name="ihelper",
    version=0.1,
    author="gepcel",
    author_email="gepcelway@gmail.com",
    description="A spyder plugin to get help information from ipython console in editor.",
    license="MIT license",
    url="",
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
