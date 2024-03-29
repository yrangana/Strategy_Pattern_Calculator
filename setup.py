# setup file for the package
from setuptools import setup, find_packages

with open("requirements.txt", "r", encoding="utf-8") as _f:
    requirements = [line for line in _f.read().split("\n")]

setup(
    name="spcalc",
    description="Stratergy Pattern Calculator",
    packages=find_packages(),
    author="Yasiru Rangana",
    entry_points="""
    [console_scripts]
    spcalc=spcalc.main:main
    """,
    install_requires=requirements,
    version="2.0.0",
    url="https://github.com/yrangana/Strategy_Pattern_Calculator",
)
