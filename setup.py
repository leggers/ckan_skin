from setuptools import setup, find_packages
import sys, os

version = '0.1'

setup(
    name='ckanext-turing_theme',
    version=version,
    description="Turing's theme.",
    long_description='''
    ''',
    classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
    keywords='',
    author='Lucas S Eggers',
    author_email='l.eggers91@gmail.com',
    url='',
    license='',
    packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
    namespace_packages=['ckanext', 'ckanext.turing_theme'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        # -*- Extra requirements: -*-
    ],
    entry_points='''
        [ckan.plugins]
        # Add plugins here, e.g.
        turing_theme=ckanext.turing_theme.plugin:TuringThemePlugin
    ''',
)
