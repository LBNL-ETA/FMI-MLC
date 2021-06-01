import setuptools

with open("README.md", "r") as f:
    long_description = f.read()

setuptools.setup(
    name="FMI-MLC",
    version="1.0.0",
    author="Gehbauer, Christoph",
    description="Functional Mock-up Interface - Machine Learning Center",
    license_files = ['license.txt'],
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/LBNL-ETA/FMI-MLC",
    project_urls={
        "Bug Tracker": "https://github.com/LBNL-ETA/FMI-MLC/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    packages=setuptools.find_packages(),
    python_requires=">=3.6",
    install_requires= ['gym', 'pandas', 'numpy']
)
