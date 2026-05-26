# Import setup tools

from setuptools import setup, find_packages


# Package configuration
setup(

    # Library name on PyPI
    name="expense-tracker",

    # Package version
    version="1.0.0",

    # Author name
    author="Gurung Dipen",

    # Short description
    description="Simple Python expense tracking library",

    # Automatically find package folders
    packages=find_packages(),

    # External libraries required
    install_requires=[],
)