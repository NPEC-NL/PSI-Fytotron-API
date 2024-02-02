from setuptools import setup

setup(
    name="psi fytotron",
    version="0.1",
    description="Python API implementation of PSI fytotron API",
    author="NPEc WUR",
    author_email="",
    url='https://github.com/wurDevTim/PSI-Fytotron-API',
    packages=["psi-fytotron"],
    provides=["psi-fytotron"],
    install_requires=["certifi", "six", "python_dateutil", "urllib3"],
    license="GNU GENERAL PUBLIC LICENSE v3",
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ])