import os
import sys
from models.buildings_generator import BuildingsGenerator


if __name__ == '__main__':
    try:
        query_id = sys.argv[1]
    except KeyError:
        query_id = None

    generator = BuildingsGenerator(
        -8.82,
        1.92,
        49.79,
        60.94,
        os.environ['S3_BUCKET'],
        'uk',
        query_id=query_id
    )
    buildings = generator.generate()
    with open('output/uk_buildings.geojson', 'w') as file_:
        file_.write(buildings)
