import os

from setuptools import find_packages, setup


def read(filename):
    path = os.path.join(os.path.dirname(__file__), filename)
    with open(path, 'r') as f:
        return f.read()


setup(
    name="stere",
    version="0.31.0",
    description="A nice way of implementing the Page Object pattern.",
    long_description=read('README.rst'),
    author="Joshua Fehler",
    author_email="jsfehler@gmail.com",
    license="MIT",
    url="https://github.com/jsfehler/stere",
    package_data={'stere': ['py.typed']},
    zip_safe=False,
    packages=find_packages(),
    install_requires=[
        'py-moneyed==1.0',
    ],
    extras_require={
        'splinter': ['splinter==0.18.0'],
    },
    classifiers=(
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Development Status :: 4 - Beta",
    ),
)
