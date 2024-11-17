from setuptools import find_packages, setup

with open("./README.md") as f:
    readme = f.read()

with open("./LICENSE") as f:
    license = f.read()

setup(
    name="temapi",
    version="0.1.5",
    description="Python API lib for TEM (https://tronenergy.market/) ",
    long_description=readme,
    long_description_content_type="text/markdown",
    license=license,
    author="Bohdan Kushnir",
    author_email="",
    url="https://github.com/8ByteCore8/tem-api",
    packages=find_packages(exclude=["tests", "examples"]),
    python_requires=">=3.6",
)
