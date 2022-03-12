import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="fairos-py-sdk",
    version="0.0.2",
    author="jusonalien",
    author_email="jusonalien@qq.com",
    description="a python SDK for FairOS",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/SwarmLover/FairOS-Python-SDK",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        'requests>=2.27.1',
    ]
)