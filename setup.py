import fast
from setuptools import setup


with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="FastCLI",
    version="0.0.1",
    author="Jônatas Luiz de Oliveira",
    author_email="contact@jonatasoliveira.dev",
    description="A FastAPI CLI",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/jonatasoli/fastcli",
    project_urls={
        "Bug Tracker": "https://github.com/jonatasoli/fastcli/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "fast"},
    packages=setuptools.find_packages(where="fast"),
    python_requires=">=3.9",
    extras_require={
        "typer": ">=0.4.0",
        "cookiecutter": ">=1.7.3"
)
