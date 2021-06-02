from setuptools import find_packages, setup

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
    url="https://github.com/Sebastian-Soto-M/pyno",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        'certifi==2021.5.30',
        'chardet==4.0.0',
        'idna==2.10',
        'pydantic==1.8.2',
        'requests==2.25.1',
        'responses==0.13.3',
        'six==1.16.0',
        'typing-extensions==3.10.0.0',
        'urllib3==1.26.5',
    ],
    packages=find_packages(),
    namespace_packages=['pyno'],
    python_requires=">=3.8",
    package_data={
        "": ["*.json"],
    },
    zip_safe=False
)
