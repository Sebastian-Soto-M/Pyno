from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    detailed_description = fh.read()

setup(
    name="pyno",
    version="0.1",
    author="Sebastian Soto Madrigal",
    author_email="s.m.sebastian.n@gmail.com",
    description="A wrapper for Notion's Api",
    long_description=detailed_description,
    long_description_content_type="text/markdown",
    url="",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages=find_packages("pyno"),
    package_dir={"": "pyno"},
    python_requires=">=3.9",
    package_data={
        "": ["*.json"],
    }
)
