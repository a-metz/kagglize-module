import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="kagglize-module",
    version="0.0.1",
    author="Alexander Wah Tak Metz",
    author_email="alexander.wt.metz@gmail.com",
    description="Generates a single python script to recreate files of a python module.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/wahtak/kagglize-module",
    scripts=["kagglize-module"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    install_requires=["click"],
)
