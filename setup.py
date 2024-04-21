#!/usr/bin/env python3

from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="glow",
    author="Joerg Mechnich",
    author_email="joerg.mechnich@gmail.com",
    license="MIT",
    description="Control your LED strip via the network.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/jmechnich/glow",
    use_scm_version={"local_scheme": "no-local-version"},
    setup_requires=["setuptools_scm"],
    packages=["glow"],
    scripts=["glowd"],
    data_files=[
        (
            "share/glow",
            ["misc/glowd.service", "misc/glowd.init", "misc/glowd.conf"],
        )
    ],
    python_requires=">=3.6",
)
