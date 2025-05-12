from setuptools import setup, find_packages

setup(
    name="runcode",
    version="0.1.0",
    author="Your Name",
    author_email="you@example.com",
    description="Offline LeetCode-style testing CLI",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/runcode",
    packages=find_packages(exclude=["tests"]),
    include_package_data=True,
    install_requires=[
        "click",
        "rich",
    ],
    entry_points={
        "console_scripts": [
            "runcode = runcode.__main__:cli",
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
)
