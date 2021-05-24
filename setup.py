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
    url="https://github.com/Sebastian-Soto-M/Pyno",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        'certifi==2020.12.5',
        'chardet==4.0.0',
        'idna==2.10',
        'mypy==0.812',
        'mypy-extensions==0.4.3',
        'pydantic==1.8.2',
        'python-decouple==3.4',
        'requests==2.25.1',
        'requests-toolbelt==0.9.1',
        'typed-ast==1.4.3',
        'typing-extensions==3.10.0.0',
        'urllib3==1.26.4',
    ],
    packages=find_packages("pyno"),
    package_dir={"": "pyno"},
    python_requires=">=3.9",
    package_data={
        "": ["*.json"],
    }
)
