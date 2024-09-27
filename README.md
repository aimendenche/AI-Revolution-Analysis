AI Revolution Analysis
Overview

This project analyzes a dataset of AI job salaries to derive insights and prepare data for indexing in Elasticsearch. The final objective is to visualize and monitor AI salary trends using Kibana.
Table of Contents

    Project Structure
    Environment Setup & Dependencies
    Scripts Overview
        ai-salaries_analysis.py
        connectivity-elasticsearch.py
    Elasticsearch & Kibana Setup
    How to Run the Project
    Data Visualization in Kibana

Project Structure

graphql

AI-Revolution-Analysis
├── dashboards/                    # Future folder for Kibana dashboards (to be filled after visualizations are saved)
├── data/                          # Folder for datasets
│   ├── salaries.csv               # Original dataset with raw AI salary data
│   └── cleaned_salaries.csv       # Cleaned dataset ready for Elasticsearch indexing
├── notebooks/                     # Jupyter notebooks for data exploration
│   └── Salaries_Analysis.ipynb    # Notebook for EDA (Exploratory Data Analysis)
├── scripts/                       # Folder containing Python scripts
│   ├── ai-salaries_analysis.py    # Script for loading, cleaning, and saving data
│   └── connectivity-elasticsearch.py # Script for connecting to Elasticsearch and indexing data
├── venv/                          # Virtual environment for project dependencies
├── README.md                      # Project documentation (this file)
└── requirements.txt               # Python dependencies

Environment Setup & Dependencies
1. Clone the Repository

bash

git clone https://github.com/aimendenche/AI-Revolution-Analysis.git
cd AI-Revolution-Analysis

2. Python Environment & Packages

    Create a Virtual Environment (Recommended)

    bash

python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

Install Project Dependencies

bash

    pip install -r requirements.txt

3. Check Installed Packages

The requirements.txt file contains the following packages necessary for the project:

    pandas: For data manipulation and analysis.
    matplotlib, seaborn: For data visualization.
    elasticsearch: For connecting and indexing data into Elasticsearch.

Scripts Overview
1. ai-salaries_analysis.py

Purpose: This script handles data loading, cleaning, and saving the cleaned dataset for further analysis and indexing into Elasticsearch.

Key Steps:

    Load Data:
        Reads the CSV file (data/salaries.csv) containing raw AI salary data.
        Displays an overview of the data structure, column info, and missing values.

    Data Cleaning:
        Remove Unnecessary Columns: Drops any irrelevant columns (like unnamed index columns).
        Handle Duplicates: Identifies and removes duplicate rows in the dataset.
        Standardize Data Types: Ensures all numerical columns (e.g., salaries) are integers, and categorical text columns are standardized to lowercase for consistency.

    Save Cleaned Data:
        The cleaned data is saved as a new CSV file (data/cleaned_salaries.csv) ready for further processing.

Run the Script:

bash

python scripts/ai-salaries_analysis.py

2. connectivity-elasticsearch.py

Purpose: This script handles connecting to Elasticsearch, creating an index if it does not exist, and bulk indexing the cleaned data for visualization and analysis in Kibana.

Key Steps:

    Connect to Elasticsearch:
        Connects to a local Elasticsearch instance running at http://localhost:9200.
        Verifies the connection before proceeding.

    Load Cleaned Data:
        Loads the cleaned dataset from data/cleaned_salaries.csv.

    Create Elasticsearch Index (If Not Exists):
        Checks if the index (ai_salaries) exists in Elasticsearch.
        If not, it creates the index dynamically without predefined mappings, allowing Elasticsearch to auto-detect field types.

    Index Data to Elasticsearch:
        Converts the DataFrame records into JSON format.
        Uses Elasticsearch's bulk indexing helper to efficiently index all data into the specified index.

Run the Script:

bash

python scripts/connectivity-elasticsearch.py

Elasticsearch & Kibana Setup
1. Install Elasticsearch & Kibana

Install Elasticsearch (Version 8.15.1 to match the project):

bash

curl -L -O https://artifacts.elastic.co/downloads/elasticsearch/elasticsearch-8.15.1-amd64.deb
sudo dpkg -i elasticsearch-8.15.1-amd64.deb
sudo systemctl enable elasticsearch
sudo systemctl start elasticsearch

Install Kibana (Version 8.15.1):

bash

curl -L -O https://artifacts.elastic.co/downloads/kibana/kibana-8.15.1-amd64.deb
sudo dpkg -i kibana-8.15.1-amd64.deb
sudo systemctl enable kibana
sudo systemctl start kibana

2. Access Services

    Elasticsearch: http://localhost:9200
    Kibana: http://localhost:5601

How to Run the Project
Step 1: Data Cleaning & Preparation

Run the script to clean the raw data and save it for Elasticsearch:

bash

python scripts/ai-salaries_analysis.py

Step 2: Elasticsearch Indexing

After cleaning, index the data into Elasticsearch:

bash

python scripts/connectivity-elasticsearch.py

Step 3: Verify in Kibana

    Open Kibana in your browser at http://localhost:5601.
    Go to Discover to confirm the data is correctly indexed.

Data Visualization in Kibana
1. Create an Index Pattern

    Navigate to "Stack Management":
        Click on "Stack Management" under Management in the sidebar.

    Create an Index Pattern:
        Go to "Index Patterns" and click "Create index pattern".
        Enter ai_salaries* as the index pattern name.
        Select a timestamp field if available (or choose no time filter).

    Start Discovering Your Data:
        Once the index pattern is created, you can explore your indexed data under "Discover".

2. Create Visualizations

    Go to "Visualize Library":
        In Kibana, navigate to "Visualize Library".

    Choose a Visualization Type:
        Select a visualization type (e.g., bar chart, pie chart).

    Configure the Visualization:
        Choose ai_salaries as the data source.
        Use the fields in the data (e.g., job_title, salary_in_usd) to build visual insights.

Conclusion

This project enables detailed exploration and visualization of AI job salary data using Python, Elasticsearch, and Kibana. Follow the steps to clean, index, and analyze the data to gain insights into salary trends in the AI industry.

Feel free to customize and extend the project as needed. Happy analyzing!
