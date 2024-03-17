import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="PythonHornDesign",
    version="0.0.1",
    author="Kurt Schoenhoff",
    author_email="Kurt@Kurtsch.com.au",
    description="An acoustic horn design generator",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/pypa/sampleproject",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Unlicence",
        "Operating System :: OS Independent",
    ],
)