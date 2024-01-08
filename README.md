# Metadata Browser of the Text REtrieval Conference (TREC)

## Running the browser locally

1. Clone this repository
```
git clone https://github.com/usnistgov/trec-browser.git
```

2. Change into the `browser/` directory and build/run the Docker container.
```
cd trec-browser/browser/ && docker compose up -d
```

3. Open your web browser and navigate to [`http://localhost:8000/trec-browser`](http://localhost:8000/trec-browser).

## Running the REST-API locally

1. Clone this repository
```
git clone https://github.com/usnistgov/trec-browser.git
```

2. Place the SQLite database file in the `api/src/` directory.

3. Change into the `api/` directory and build/run the Docker container.
```
cd trec-browser/api/ && docker compose up -d
```

4. The REST-API is then available at `http://localhost:5000/trec/api/v1/`.