"""Load csv files into bigquery"""
from google.cloud import bigquery
from google.oauth2 import service_account
import os
# from dotenv import load_dotenv
# load_dotenv()

client = bigquery.Client()

main_path = "/Users/Oamen/OneDrive/Documents/DATA PROJECTS/RetailXpress_data_warehouse/datasets"

json_files = [file.split('.')[0] for file in os.listdir(main_path) if file.endswith('json')]
csv_files = [(f'{main_path}/{file}', file) for file in os.listdir(main_path) if file.endswith('csv') and file.split('.')[0] not in json_files]
# print(f'All csv: {csv_files}')
# print(json_files)

dataset_id = 'data_lake'
dataset_ref = client.dataset(dataset_id)

for filename, tablename in csv_files:
    print(filename)
    
    table_id = tablename.split('.')[0]

    table_ref = dataset_ref.table(table_id)
    job_config = bigquery.LoadJobConfig()
    job_config.source_format = bigquery.SourceFormat.CSV
    job_config.autodetect = True

    with open(filename, "rb") as source_file:
        job = client.load_table_from_file(
            source_file,
            table_ref,
            # location="europe-west1",  # Must match the destination dataset location.
            job_config=job_config,
        )  # API request

    job.result()  # Waits for table load to complete.

    print("Loaded {} rows into {}:{}.".format(job.output_rows, dataset_id, table_id))