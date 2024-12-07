"""Convert json files to CSVs and load into bigquery"""
from google.cloud import bigquery
from google.oauth2 import service_account
import os, pandas as pd, json
# from dotenv import load_dotenv
# load_dotenv()

# convert json to csv
def convert_to_json(filename):
    
    # with open(filename, encoding="utf8") as f:
    #     content = f.readlines()

    # data =[eval(c) for c in content]#convert string to dict format

    try: 

        df = pd.read_json(filename)

    except ValueError:

        df = pd.read_json(filename, lines = True)

    df.to_csv(filename.replace('json', 'csv'), index = False, quoting=1,  escapechar="\\")

    print(df.columns)

    return filename.replace('json', 'csv')

client = bigquery.Client()

main_path = "/Users/Oamen/OneDrive/Documents/DATA PROJECTS/RetailXpress_data_warehouse/datasets"

json_files = [(f'{main_path}/{file}', file) for file in os.listdir(main_path) if file.endswith('json')]

dataset_id = 'data_lake'
dataset_ref = client.dataset(dataset_id)

for filename, tablename in json_files:

    print(filename, tablename)

    new_filename = convert_to_json(filename)
    print(new_filename)
    
    table_id = tablename.split('.')[0]
    print(table_id)

    table_ref = dataset_ref.table(table_id)

    job_config = bigquery.LoadJobConfig()
    job_config.source_format = bigquery.SourceFormat.CSV
    job_config.autodetect = True
    job_config.allow_quoted_newlines = True

    with open(new_filename, "rb") as source_file:
        job = client.load_table_from_file(
            source_file,
            table_ref,
            # location="europe-west1",  # Must match the destination dataset location.
            job_config=job_config,
        )  # API request

    job.result()  # Waits for table load to complete.

    print("Loaded {} rows into {}:{}.".format(job.output_rows, dataset_id, table_id))