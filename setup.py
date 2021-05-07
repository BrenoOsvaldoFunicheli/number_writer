import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="number_writer", # Replace with your own username
    version="0.0.1",
    author="Example Author",
    author_email="bfunicheli@estudante.ufscar.com",
    description="A small example package to transform number into text",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/pypa/sampleproject",
    
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        
    ],
    # package_dir={"": "number_writer"},
    packages=['number_writer']
)