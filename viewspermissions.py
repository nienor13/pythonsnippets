#get permissions for all views in dataset, put in jsons in folder, and zip it up
import os
import json
import requests
import shutil
from datetime import date
from google.cloud import bigquery


# Set up the BigQuery client
client = bigquery.Client()

# Set the project and dataset ID for the dataset containing the views
project_id = 'projectname'
dataset_id = 'datasetname'
parentdir = "c:/temp/"
folder="BQPermissions"+str(date.today())
zipdir=os.path.join(parentdir,folder)
if not os.path.exists (zipdir):
    os.makedirs (zipdir)
views = client.list_tables(dataset_id)
viewlist = list (views)
for view in viewlist:
    view_id=view.table_id
    table_ref = client.dataset(dataset_id).table(view_id)
    policy = client.get_iam_policy(table_ref)
    policy_json = policy.to_api_repr()
    policy_filename = f'{view_id}.json'
    path=os.path.join(zipdir,policy_filename)
    with open(path, 'w') as f:
        f.write(json.dumps(policy_json))
shutil.make_archive(zipdir,"zip",zipdir)
