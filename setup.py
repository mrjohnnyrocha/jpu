# setup.py
from setuptools import setup, find_packages

setup(
    name="jpu",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        # List dependencies here
    ],
    entry_points={
        'console_scripts': [
            'start-shell = start_shell:main',
        ],
    },
)
