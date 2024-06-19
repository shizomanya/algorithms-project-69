from setuptools import setup, find_packages

setup(
    name='search_engine',
    version='0.1',
    packages=find_packages(),
    install_requires=[],
    entry_points={
        'console_scripts': [
            'search_engine = search_engine:main',
        ],
    },
)
