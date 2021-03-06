from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="spaw",
    version="0.2",
    author="Anas Mohamed",
    author_email="amohamed@ualberta.ca",
    description="SPAW is an Unofficial Streamable API Wrapper for Python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/amohamed11/StreamablePythonAPIWrapper",
    packages=find_packages(),
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3.0",
        "Operating System :: OS Independent",
    ),
)
