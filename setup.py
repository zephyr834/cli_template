from setuptools import setup, find_packages

with open('requirements.txt') as f:
    required = f.read().splitlines()

setup(
    name="myapp", 
    version="1.0.0",
    packages=find_packages(),
    author="Author",
    author_email="something@gmail.com",
    description="An Application.",
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url="https://github.com/username/myapp",
    py_modules=["app"],
    install_requires=required,
    tests_require=[
        "pytest",
    ],
    entry_points={
        "console_scripts": [
            "tasksu=cli:cli",
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',  # Minimum Python version requirement
)
