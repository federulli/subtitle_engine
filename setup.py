import os
from setuptools import setup

# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name="subtitle_engine",
    version="1.0.0",
    author="Federico Rulli",
    author_email="fede.rulli@gmail.com",
    description="Subtitle Downloader",
    packages=['subtitle-engine'],
    long_description=read('README.md')
)