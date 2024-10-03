import setuptools

ext = setuptools.extension.Extension("makefile", ["install/Makefile"])


setuptools.setup(
name="pyswisspair",
version="0.1.0",
description="Algorithm to pair players according to the Swiss system (not only) for Magic: The Gathering.",
ext_modules=[ext],
packages=["src"],
classifiers=[
"Programming Language :: Python :: 3",
"License :: OSI Approved :: MIT License",
"Operating System :: OS Independent",
],
python_requires=">=3.10",
)
