# Metadata Browser of the Text Retrieval Conference

This repository contains the resources of the TREC metadata browser available at [https://pages.nist.gov/trec-browser](https://pages.nist.gov/trec-browser) and the source code of the REST API server that can be used for principled queries and systematic access to the metadata of TREC (this repository also contains a [notebook](./api/demo.ipynb) that demonstrates and documents the use of the API). The underlying database containing the metadata can be obtained from the TREC program managers (see instructions below). 

## Overview 

| Directory / file | Description | 
| --- | --- | 
| [`browser/`](./browser/) | This directory contains all the resources required to build and run the TREC metadata browser. | 
| [`browser/build.ipynb`](./browser/build.ipynb) | Use this notebook to (re)build the files that are required to run the browser (see [instructions below](#building-the-browser-files)). | 
| [`api/`](./api/) | This directory contains the source code of the REST API server application. | 
| [`api/demo.ipynb`](./api/demo.ipynb) | This notebook demonstrates and documents the use of the REST API by providing three use case examples. | 

## Obtaining the database

The database is available for research and non-commercial purposes. It can be obtained by contacting the TREC program coordinator [trec (at) nist.gov]. **For the reviewers, we share the database confidentially with the help of an anonymized link. Details are given in the paper submission.**

## Running the demo of the REST API

Before running the [demo notebook](./api/demo.ipynb), please make sure to follow the setup [instructions outlined below](#running-the-rest-api-locally). Afterward, you can retrieve outputs from the REST API. Use the notebook for three possible use cases, including (1) a general introduction to the API invocations and retrieving metadata, (2) fetching resources of earlier TREC submissions, and (3) reproducing system comparisons of earlier tracks.

## Setup

1. Make sure you have [Python](https://www.python.org/), [Docker](https://www.docker.com/), and [docker-compose](https://docs.docker.com/compose/) installed.
2. Obtain the database file if you want to rebuild the browser files or run the REST API server.

## Building the browser files

**Note:** Building the browser files is not mandatory if you just want to run the browser locally. They are located in the `browser/src/` directory of this repository.

1. Clone this repository
```
git clone https://github.com/usnistgov/trec-browser.git
```

2. Obtain the database file and place it in the top level directory of this repository. You can choose any other directory but please make sure to adapt the file path in the notebook in that case.

3. Run the noteboook `browser/build.ipynb`. It will install the required Python packages, generate the browser files and place them in the `browser/src/` directory.

4. Make sure to have the required Python packages installed when building the browser in a local Python environment (see also [this requirements.txt file](./browser/src/requirements.txt)). Then, build the HTML files with the following command:
```
cd trec-browser/browser/src && mkdocs build
```

## Running the browser

**Note:** The most recent version of the TREC browser is available at [https://pages.nist.gov/trec-browser](https://pages.nist.gov/trec-browser). If you want to run it locally, e.g., for development purposes, please follow the instructions outlined below.

1. Clone this repository
```
git clone https://github.com/usnistgov/trec-browser.git
```

2. Change into the `browser/` directory and build/run the Docker container.
```
cd trec-browser/browser/ && docker compose up -d
```

3. Open your web browser and navigate to [`http://localhost:8000/trec-browser`](http://localhost:8000/trec-browser).

## Running the REST API

1. Clone this repository
```
git clone https://github.com/usnistgov/trec-browser.git
```

2. Obtain the database file and place it in the `api/src/` directory.

3. Change into the `api/` directory and build/run the Docker container.
```
cd trec-browser/api/ && docker compose up -d
```

4. The REST API is then available at `http://localhost:5000/trec/api/v1/`.