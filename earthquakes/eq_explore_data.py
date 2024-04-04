from pathlib import Path
import json

path = Path('past24_eq.geojson')
contents = path.read_text()
readble_content = json.loads(contents)
with open('readable_eq_data.geojson', 'w') as file:
    json.dumps(readble_content, file)