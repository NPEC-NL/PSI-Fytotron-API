<h1 align="center"> PSI Fytotron API implementation
</h1>

<p align="center">
<a href="https://badge.fury.io/py/psi-fytotron">
<img src="https://badge.fury.io/py/psi-fytotron.svg" alt="PyPI version"/></a>
</p>

- [Documentation](https://npec-nl.github.io/PSI-Fytotron-API/) <br>
- [Source Code](https://github.com/NPEC-NL/PSI-Fytotron-API) <br>
---
Photon System Instruments (PSI) delivers equipment across the globe. 
Most of their cells are controlled by a fytotron PC, for which they also provide an optional API.
To simplify the implementation and sharing of analysis workflows, we created an OpenAPI specification file and use the [Openapi Generator](https://github.com/openapitools/openapi-generator) to generate this package.



## Installation & Usage
Install from PyPI:
```sh
pip install psi-fytotron
```
Build and tested with Python 3.9+  
Cross-platform support for Linux, macOS and Windows

## Example implementation
Uses a .env file with the following fields:
```
URL: http://<ip-address/path>:<port>/fyto/rest
TOKEN: <Fytotron API access token>
```
The environment files have one additional depency: `pip install python-dotenv`
Example code:
https://github.com/NPEC-NL/PSI-Fytotron-API/blob/main/example_implementation.py?plain=1#L2-L32


# Contributing
We welcome contributions! 
If you encounter bugs, have feature requests, or want to suggest improvements, please [create an issue](https://github.com/NPEC-NL/PSI-Fytotron-API/issues) and provide a clear description.

### Setting up a Development Environment
Requires Python 3.9+
1. **Create a virtual environment (venv):**
	```sh
	python -m venv .venv
	```
2. **Activate the venv:**
	- On Windows:
	  ```sh
	  .venv\Scripts\activate
	  ```
	- On macOS/Linux:
	  ```sh
	  source .venv/bin/activate
	  ```
3. **Install the package with build and test dependencies:**
	```sh
	pip install .[build, test]
	```


## For developers
This repository contains a few workflows, they work as follows:
- *build client*, is triggered by a commit and builds the python client from the specification file.
- *Build docs*, triggered by the completion of `build client` uses mkdocs to create the documentation pages.
- *Test fytotron client*, triggered by the completion of `build client` or by a pull request, runs the unittests on the repository.
-  *release*, can be triggered manually to create a release on testpypi or through a release to push to pypi. To install the release from testpypi, the following command can be used: `python -m pip install --index-url https://test.pypi.org/simple/ --extra-index-url https://pypi.org/simple psi-fytotron`


### Updating the OpenAPI specification file
The API is automatically generated from the [OpenAPI specification file](https://github.com/NPEC-NL/PSI-Fytotron-API/blob/main/OpenAPI_specification/PSI_fytotron_API.json) with the [openapi generator cli](https://github.com/OpenAPITools/openapi-generator-cli).
The workflows automatically build the client and copy the files to the right folders.

# Documentation
Build with [mkdocs-material](https://squidfunk.github.io/mkdocs-material/)

## Documentation for API Endpoints
All URIs are relative to *https://localhost:8000/fyto/rest*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*FytotronApi* | [**getvar**](docs/FytotronApi.md#getvar) | **GET** /getvar | Returns the current value of the variable
*FytotronApi* | [**info**](docs/FytotronApi.md#info) | **GET** /info | Returns all setpoints and actual values in the database.
*FytotronApi* | [**monitor**](docs/FytotronApi.md#monitor) | **GET** /monitor | Returns the current status of the fytotron
*FytotronApi* | [**setvar**](docs/FytotronApi.md#setvar) | **POST** /setvar | Set the setpoint value

## Documentation For Models
 - [InfoValues](docs/InfoValues.md)
 - [MonitorValues](docs/MonitorValues.md)

<a id="documentation-for-authorization"></a>
## Documentation For Authorization

Authentication schemes defined for the API:
<a id="ApiKeyAuth"></a>
### ApiKeyAuth

- **Type**: API key
- **API key parameter name**: X-Auth-Token
- **Location**: HTTP header
