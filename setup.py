import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="weixin-api",
    version="1.1.1",
    author="kerol",
    author_email="ikerol@163.com",
    description="weixin api",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/kerol/weixin-api",
    packages=setuptools.find_packages(),
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
    install_requires=[
        'requests',
        'ujson',
        'pycrypto',
    ]
)
