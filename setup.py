#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" The setup and build script for the library. """

from setuptools import setup, find_packages

CLASSIFIERS = [
    'Programming Language :: Python',
    'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    'Topic :: Multimedia :: Sound/Audio',
    'Topic :: Multimedia :: Sound/Audio :: Players'
]

setup(
    name="Youtube Audio Streamer",
    url="https://github.com/akhilrs/youtube-audio-streamer.git",
    description="Stream audio from a youtube url",
    long_description=open('README.md').read(),
    author="0x1235c0d3r",
    version="0.0.1",
    install_requires=[
        'setuptools',
        'pafy',
        'python-vlc'
    ],
    platforms=['OS Independent'],
    license='GPL v2',
    scripts=['scripts/streamer'],
    classifiers=CLASSIFIERS,
    packages=find_packages(),
    include_package_data=True,
    zip_safe=True

)