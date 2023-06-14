from setuptools import setup, find_packages
import codecs
import os

VERSION = '1.0.0'
DESCRIPTION = "It's a hello world library"

# Setting up
setup(
    name="hellopkg",
    version=VERSION,
    author="the_programmer2009 (Moataz MDALLAH)",
    author_email="<mdallahmoataz@gmail.com>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    packages=find_packages(),
    install_requires=[],
    keywords=['python', 'video', 'stream', 'video stream', 'camera stream', 'sockets'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)