from setuptools import setup, find_packages


with open('LICENSE') as f:
    license = f.read()


setup(
    name='ecmwf_mars',
    version='0.1.0',
    author='Stefan Lüdtke',
    url='https://github.com:sluedtke/ecmwf_mars.git',
    packages=find_packages(),
    license=license,
    tests_require=['pytest'],
    install_requires=['datetime']
)
