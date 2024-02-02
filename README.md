<h1 align="center"> PSI Fytotron API implementation
</h1>

<p align="center">
<a href="https://badge.fury.io/py/psi-fytotron">
<img src="https://badge.fury.io/py/psi-fytotron.svg" alt="PyPI version"/></a>
</p>

- [Documentation](https://wurDevTim.github.io/PSI-Fytotron-API) <br>
- [Source Code](https://github.com/wurDevTim/PSI-Fytotron-API) <br>
---
Photon System Instruments (PSI) develivers equipment accross the globe. 
Most of their cells are controlled by a fytotron PC, for which they also provide an API.
We, the NPEC team believes it's a waist of everyones time if we all have to implement the same code.
Therefore we created he swagger file and a simple python wrapper you can use to integrate the fytotron API.

## Installation 
`pip install psi-fytotron`  
Build and tested with python 3.8 on windows 10  
Cross platform support for Linux, macOS and Windows

## Example implementation
Uses a .env file with the following fields:
```
URL: <The url or ip-address of your fytotron machine >
PORT: <Poort on which the fytotron API is available>
```
The environment files have one additional depency: `pip install python-dotenv`
Example code:
https://github.com/wurDevTim/PSI-Fytotron-API/blob/main/example_implementation.py?plain=1#L2-L32


## Contributing
### Build requirements:
build >= 1.0.3
setuptools >= 21.0.0
twine >= 4.0.2
mkdocs >= 1.5.3
mkdocs-material >= 9.5.6


### Updating the swagger file
The API is automatically generated from the [swagger file](https://github.com/wurDevTim/PSI-Fytotron-API/blob/main/swagger_file/PSI_fytotron_API.json) with the [swagger editor](https://editor.swagger.io/).
After generation unpack the zip and move them to the following location:
- Move The `docs` folder to: `docs/Code/Swagger_docs` and replace all occurances of `..Readme.md` with `readme.md`
- `REAME.md` is copied to: `docs/Code/Swagger_docs` and the reference updates to `./`
- The code from `swagger_client` to `fytotron/swagger_client`. Replace all occurances of `from swagger_client` with `from fytotron.swagger_client`

### Documentation
Build with [mkdocs-material](https://squidfunk.github.io/mkdocs-material/)

## Authors
Tim van Daalen and Pinglin Zhang
NPEC
https://www.npec.nl/
