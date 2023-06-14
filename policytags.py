#find all tables and columns with policy tags in your BigQuery

from google.cloud import bigquery

# Set up the BigQuery client
client = bigquery.Client()

piilevel1 = 'piitagID1'
piilevel2 = 'piitagID2'
piilevel3 = 'piitagID3'
datasets = list (client.list_datasets())
for dataset in datasets:
    tables = client.list_tables(dataset.dataset_id)
    for table in tables:
        table_id = dataset.dataset_id+"."+table.table_id
        table_ref = client.get_table(table_id)
        for schema in table_ref.schema:
            if schema.policy_tags :
                tags = str(schema.policy_tags)
                if piilevel1 in tags:
                    print (table_id+"."+schema.name, "PII Level 1\n")
                if piilevel2 in tags:
                    print (table_id+"."+schema.name, "PII Level 2\n")
                if piilevel3 in tags:
                    print (table_id+"."+schema.name, "PII Level 3\n")
