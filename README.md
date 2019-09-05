# athena-buildings
A script that queries OpenStreetMap using AWS Athena for buildings in a given bounding box.

## Install

1. Setup the virtualenv
  ```bash
    $ virtualenv -p python3 venv
  ```
2. Install the requirements
  ```bash
    $ pip install -r requirements.txt
  ```
3. Copy the `.env` file and fill it
  ```bash
    $ cp .env.example .env
  ```

## Run
```bash
  $ python get_buildings.py
```
This gets the buildings in Iceland and stores it into a local GeoJSON file (in `output`).
The class that actually gets the data is in [models/buildings_generator.py](models/buildings_generator.py).

## Convert geojson to Mapxbox vector tiles.

1. Install Tippacanoe per
https://github.com/mapbox/tippecanoe#installation

2. Convert geojson to mbtiles
tippecanoe -zg -o uk_buildings_amenities.mbtiles --coalesce-densest-as-needed --extend-zooms-if-still-dropping uk_buildings.geojson

3. Upload the mbtiles to mapbox studio, style it and publish it
