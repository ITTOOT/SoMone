import pathlib

from setuptools import setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
    name="SoMone",
    version="0.1.0",
    description="Self-organizing map",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/xortech99/SoMone.git",
    author="Hayden Williams",
    author_email="",
    license="XORtech",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
    ],
    # dependency_links=['http://github.com/<username>/<reponame>/tarball/master#egg=<packagename>-<version#>'],
    packages=["sklearn_som", "matplotlib"],
    include_package_data=True,
    install_requires=["numpy"],
)
