from setuptools import setup, find_packages

setup(
    name="CodeFusion",
    version="0.1.0",
    description="A tool to combine code files from a specified directory into a single text file.",
    author="Toni Maxx",
    author_email="tonimaxx@gmail.com",
    url="https://github.com/tonimaxx/CodeFusion",  
    packages=find_packages(),
    install_requires=[
        "pathspec>=0.9.0",
    ],
    entry_points={
        "console_scripts": [
            "codefusion=codefusion.main:combine_code_files",
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)