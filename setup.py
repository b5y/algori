from setuptools import setup, find_packages

setup(
    name='algori',
    version='0.0.1',
    include_package_data=True,
    install_requires=[],
    packages=find_packages(),
    setup_requires=[
        'pytest-runner',
    ],
    tests_require=[
        'pytest>=3.0.2',
    ],
)
