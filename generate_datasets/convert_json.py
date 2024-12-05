"""To convert a json document to newline delimited json for easier upload in bigQuery - Not in use"""
import json, os, msgspec

main_path = "/Users/Oamen/OneDrive/Documents/DATA PROJECTS/RetailXpress_data_warehouse/datasets"

json_files = [f'{main_path}/{file}' for file in os.listdir(main_path) if file.endswith('json')]

for file in json_files:

    with open(file, 'rb') as f:
        j = msgspec.json.decode(f.read())
        
    j = b'\n'.join(map(msgspec.json.encode, j))

    with open(file, 'wb') as f:
        f.write(j)