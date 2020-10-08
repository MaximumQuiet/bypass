#  Copyright 2020, Maxim Kuznetsov.
#  License: Apache License 2.0 (see LICENSE for details).

from setuptools import setup, find_packages

import bypass

setup(
    name="bypass",
    version=bypass.__version__,
    description="A convenience wrapper around most known captcha solver services.",
    author=bypass.__author__,
    author_email="maximumquiet@gmail.com",
    url="https://github.com/MaximumQuiet/bypass",
    packages=find_packages(),
    license=bypass.__licence__,
    platforms="any",
    classifiers=[
        "Development Status :: 1 - Planning",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Topic :: Software Development :: Libraries",
    ],
)
