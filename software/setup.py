import os
import sys

from setuptools import setup, find_packages

setup(

    # Vitals
    name='kilsyth',
    license='BSD',
    url='https://github.com/kbeckmann/kilsyth',
    author='Konrad Beckmann',
    author_email='konrad.beckmann@gmail.com',
    description='Kilsyth FPGA',

    # Imports / exports / requirements.
    platforms='any',
    packages=find_packages(include=["kilsyth", "kilsyth.*"]),
    include_package_data=True,
    python_requires="~=3.8",
    install_requires=['nmigen', 'pergola_projects'],
    setup_requires=['setuptools'],

)
