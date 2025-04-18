import sys
from setuptools import setup, find_packages

NAME = "discovery_finder"
VERSION = "1.0.0"

# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = [
    "connexion>=2.0.2",
    "swagger-ui-bundle>=0.0.2",
    "python_dateutil>=2.6.0"
]

setup(
    name=NAME,
    version=VERSION,
    description="icds",
    author_email="",
    url="",
    keywords=["OpenAPI", "icds"],
    install_requires=REQUIRES,
    packages=find_packages(),
    package_data={'': ['openapi/openapi.yaml']},
    include_package_data=True,
    entry_points={
        'console_scripts': ['discovery_finder=discovery_finder.__main__:main']},
    long_description="""\
     Industrial Corridors Discovery Finder &amp; Discovery Service. This service provides APIs to discover and manage industrial corridors and drone ports. It includes features for authentication, data management, and health checks. 
    """
)

