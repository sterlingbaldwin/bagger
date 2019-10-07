import sys
import os
from setuptools import find_packages, setup
from bagger.version import __version__

setup(
    name="bagger",
    version=__version__,
    author="Sterling Baldwin",
    author_email="baldwin32@llnl.gov",
    description="Create BDBag file archives",
    entry_points={'console_scripts':
                  ['bagger = bagger.__main__:main']},
    packages=['bagger'],
    package_dir={'bagger': 'bagger'},
    package_data={'bagger': ['LICENSE']},
    include_package_data=True)
