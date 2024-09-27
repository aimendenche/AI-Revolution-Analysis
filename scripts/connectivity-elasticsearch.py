# index_to_elasticsearch.py

# ================================
# Import Libraries
# ================================
import pandas as pd
from elasticsearch import Elasticsearch, helpers
import os

# ================================
# Constants and Configurations
# ================================
CLEANED_DATA_FILE_PATH = "/home/aimen/PycharmProjects/AI-Revolution-Analysis/data/cleaned_salaries.csv"
INDEX_NAME = 'ai_salaries'
ES_HOST = "http://localhost:9200"


# ================================
# Step 1: Connect to Elasticsearch
# ================================
def connect_to_elasticsearch():
    """Establishes a connection to the Elasticsearch cluster."""
    es = Elasticsearch(ES_HOST)
    if es.ping():
        print("Successfully connected to Elasticsearch!")
    else:
        raise ConnectionError("Elasticsearch connection failed.")
    return es


# ================================
# Step 2: Load Cleaned Data
# ================================
def load_cleaned_data(file_path):
    """Loads the cleaned dataset into a Pandas DataFrame."""
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"The file {file_path} does not exist.")

    df = pd.read_csv(file_path)
    print(f"Cleaned dataset loaded successfully with shape: {df.shape}")
    return df


# ================================
# Step 3: Create Elasticsearch Index (If Needed)
# ================================
def create_index_if_not_exists(es, index_name):
    """Creates an index in Elasticsearch if it does not already exist."""
    if es.indices.exists(index=index_name):
        print(f"Index '{index_name}' already exists.")
    else:
        # Simply create the index without defining mappings
        es.indices.create(index=index_name)
        print(f"Index '{index_name}' created automatically by Elasticsearch.")


# ================================
# Step 4: Index Data to Elasticsearch
# ================================
def index_data(es, df, index_name):
    """Indexes the cleaned data into the Elasticsearch cluster."""
    # Convert DataFrame to JSON format suitable for Elasticsearch
    records = df.to_dict(orient='records')

    # Bulk index data using helpers
    actions = [
        {
            "_index": index_name,
            "_source": record
        }
        for record in records
    ]

    # Use bulk API to index the records
    helpers.bulk(es, actions)
    print(f"Successfully indexed {len(records)} records into '{index_name}'.")


# ================================
# Step 5: Automate the Full Process
# ================================
def main():
    # Step 1: Connect to Elasticsearch
    es = connect_to_elasticsearch()

    # Step 2: Load the cleaned data
    df_cleaned = load_cleaned_data(CLEANED_DATA_FILE_PATH)

    # Step 3: Create Elasticsearch index if not exists
    create_index_if_not_exists(es, INDEX_NAME)

    # Step 4: Index data into Elasticsearch
    index_data(es, df_cleaned, INDEX_NAME)


if __name__ == "__main__":
    main()
