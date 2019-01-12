from setuptools import setup, find_packages
import subprocess
import sys

if sys.version_info >= (3, 0):
    try:
        from distutils.command.build_py import build_py_2to3 as build_py
        from distutils.command.build_scripts import build_scripts_2to3 as build_scripts
    except ImportError:
        raise ImportError("build_py_2to3 not found in distutils - it is required for Python 3.x")
    suffix = "-py3k"
else:
    from distutils.command.build_py import build_py
    from distutils.command.build_scripts import build_scripts
    suffix = ""

with open('readme.rst') as f:
    long_description = f.read()

setup(
    name="ftd3xx" + suffix,
    version=1.0,
    packages=find_packages(),
    author="Future Technology Devices International Ltd.",
    description="Python interface to ftd3xx.dll using ctypes",
    keywords="ftd3xx d3xx ft60x",
    url='http://www.ftdichip.com/Products/ICs/FT600.html',
    zip_safe=False,
    long_description=long_description,
    cmdclass = {'build_py': build_py, 'build_scripts': build_scripts},
)
