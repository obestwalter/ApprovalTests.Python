import os
import re

from setuptools import setup, find_packages


def read_text(*path_parts):
    here = os.path.dirname(__file__)
    with open(os.path.join(here, *path_parts)) as f:
        return f.read()


VERSION = re.search(r'"(.*)"', read_text("approvaltests", "version.py")).group(1)


setup(
    name='approvaltests',
    version=VERSION,
    description='Assertion/verification library to aid testing',
    author='ApprovalTests Contributors',
    author_email='jamesrcounts@outlook.com',
    url='https://github.com/approvals/ApprovalTests.Python',
    packages=find_packages(exclude=['tests*']),
    package_data={'approvaltests': ['reporters/reporters.json']},
    install_requires=['pyperclip==1.5.27', 'pathlib2', 'pytest'],
    long_description=read_text('README.md'),
    long_description_content_type='text/markdown',
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: POSIX",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: MacOS :: MacOS X",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Topic :: Software Development :: Libraries",
        "Topic :: Software Development :: Testing",
        "Topic :: Utilities",
    ],
)
