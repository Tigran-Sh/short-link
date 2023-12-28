# Short Link Generator

[![Generic badge](https://img.shields.io/badge/version-1.0.0.-blue.svg)](https://shields.io/)


# Installation

```bash
# Clone the Project
git clone git@github.com:Tigran-Sh/short-link.git

cd short_link
```


## Setup **.env**

```
# copy .env.sample as .env

* On Windows:
    copy .env.sample .env

* On macOS and Linux:
    cp .env.sample .env

```

## Dependencies

> To use the make commands, you will need to have Docker and Docker Compose installed on your machine.

### Install Docker:

* On Windows:
    * Download and install Docker Desktop from [here](https://www.docker.com/products/docker-desktop).
* On macOS:
    * Download and install Docker Desktop from [here](https://www.docker.com/products/docker-desktop).
* On Linux:
    * Follow the instructions for your distribution from [here](https://docs.docker.com/engine/install/).

### Install Docker Compose:

* On Windows and macOS:
    * Docker Compose is included with Docker Desktop.
* On Linux:
    * Follow the instructions from [here](https://docs.docker.com/compose/install/) to install Docker Compose.

## Run the server on local environment using `make` command

```bash
# run the web server and db
make run

# run migrate command
make migrate    
```


## Additional commands with `make`

```bash
# run bash          
make bash 
```
