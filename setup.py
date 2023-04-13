from setuptools import find_packages, setup


with open("README.md", "r") as fh:
    long_description = fh.read()


setup(
    name="algo_opt_mod04",
    version="0.0.1",
    author="Mariana Nazar",
    author_email="a01660508@tec.mx",
    description="Algoritmos de optimización",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/marianaanazar/algo_opt_mod04.git",
    install_requires=[
        "numpy>=1.21.6"
    ],
    packages=find_packages(exclude=("tests",)),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3',
    tests_require=['pytest'],
)