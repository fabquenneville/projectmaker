#!/usr/bin/env python3

import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="projectmaker",
    version="0.0.3",
    author="Fabrice Quenneville",
    author_email="fabquenneville@gmail.com",
    url="https://fabquenneville.github.io/projectmaker/",
    download_url="https://pypi.org/project/projectmaker/",
    project_urls={
        "Bug Tracker": "https://github.com/fabquenneville/projectmaker/issues",
        "Documentation": "https://fabquenneville.github.io/projectmaker/",
        "Source Code": "https://github.com/fabquenneville/projectmaker",
    },
    description="projectmaker can make the basic initial file structure for various programing languages and link interesting submodules.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    classifiers=[
        "Development Status :: 1 - Planning",
        "Natural Language :: English",
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
        "Environment :: Console",
    ],
    entry_points = {
        'console_scripts': [''],
    },
    keywords=[],
    install_requires=[],
    license='',
    python_requires='>=3.6',
    test_suite='nose.collector',
    tests_require=['nose'],
    zip_safe=True,
)