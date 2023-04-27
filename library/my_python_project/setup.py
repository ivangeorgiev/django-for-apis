#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = ['Click>=7.0', ]

test_requirements = ['pytest>=3', ]

setup(
    author="Ivan Georgiev",
    author_email='ivan.georgiev@example.com',
    python_requires='>=3.6',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    description="My Python Project is created with cookiecutter from pypackage",
    entry_points={
        'console_scripts': [
            'my_python_project=my_python_project.cli:main',
        ],
    },
    install_requires=requirements,
    license="BSD license",
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='my_python_project',
    name='my_python_project',
    packages=find_packages(include=['my_python_project', 'my_python_project.*']),
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/ivangeorgiev/my_python_project',
    version='0.1.0',
    zip_safe=False,
)
