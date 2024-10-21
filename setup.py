from setuptools import setup

# The information here can also be placed in setup.cfg - better separation of
# logic and declaration, and simpler if you include description/version in a file.
setup(
    name="swisspair",
    version=open("VERSION").read().strip(),
    author="Karel Jilek",
    author_email="los.karlosss@gmail.com",
    description="Python bindings for Swiss pairing algorithm for (not only) Magic: The Gathering.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    zip_safe=False,
    python_requires=">=3.9",
    requires=[]
)
