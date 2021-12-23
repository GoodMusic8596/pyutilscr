import setuptools

with open("README.md", "r") as fhandle:
    long_description = fhandle.read() 
setuptools.setup(
    name="pyutils-cr", 
    version="0.1.2", 
    author="Crow Randalf", 
    author_email="somethings8596@gmail.com", 
    description="A simple package that contains extremely useful utilities.", 
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/GoodMusic8596/pyutilscr", 
    packages=setuptools.find_packages(), 
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ], 
    python_requires='>=3.6',
)
