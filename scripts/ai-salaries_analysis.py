# ai_salaries_analysis.py

# ================================
# Import Libraries
# ================================
import pandas as pd
import os

# ================================
# Constants and Configurations
# ================================
# File paths and configurations
DATA_FILE_PATH = "/home/aimen/PycharmProjects/AI-Revolution-Analysis/data/salaries.csv"
CLEANED_DATA_FILE_PATH = "/home/aimen/PycharmProjects/AI-Revolution-Analysis/data/cleaned_salaries.csv"


# ================================
# Step 1: Load the Dataset
# ================================
def load_data(file_path):
    """Loads the dataset into a Pandas DataFrame."""
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"The file {file_path} does not exist.")

    df = pd.read_csv(file_path)
    print(f"Dataset loaded successfully with shape: {df.shape}")
    return df


# ================================
# Step 2: Data Exploration
# ================================
def explore_data(df):
    """Explores the dataset to understand its structure."""
    # Display the first few rows
    print("\n--- First few rows ---")
    print(df.head())

    # Get column info
    print("\n--- DataFrame Info ---")
    df.info()

    # Check for missing values
    print("\n--- Missing Values ---")
    missing_values = df.isnull().sum()
    print(missing_values[missing_values > 0])

    # Generate basic statistics
    print("\n--- Descriptive Statistics ---")
    print(df.describe(include='all'))


# ================================
# Step 3: Data Cleaning
# ================================
def clean_data(df):
    """Cleans and prepares the dataset for analysis."""
    # Identify unnecessary columns
    unnecessary_cols = [col for col in df.columns if 'unnamed' in col.lower()]
    if unnecessary_cols:
        print(f"\nDropping unnecessary columns: {unnecessary_cols}")
        df.drop(columns=unnecessary_cols, inplace=True)

    # Handle duplicates
    duplicate_count = df.duplicated().sum()
    if duplicate_count > 0:
        print(f"\nFound {duplicate_count} duplicates. Removing duplicates.")
        df.drop_duplicates(inplace=True)
    else:
        print("\nNo duplicates found.")

    # Ensure correct data types for numerical columns
    numeric_cols = ['salary', 'salary_in_usd']
    for col in numeric_cols:
        if df[col].dtype != 'int64':
            df[col] = df[col].astype(int)
            print(f"Converted {col} to integers.")

    # Standardize categorical columns
    categorical_cols = ['job_title', 'employee_residence', 'company_location', 'experience_level']
    for col in categorical_cols:
        df[col] = df[col].str.lower()  # Use lowercase for consistency

    print("\nData cleaning completed.")
    return df


# ================================
# Step 4: Save Cleaned Data
# ================================
def save_cleaned_data(df, file_path):
    """Saves the cleaned DataFrame to a CSV file."""
    df.to_csv(file_path, index=False)
    print(f"\nCleaned data saved to {file_path}")


# ================================
# Main Function to Run the Script
# ================================
def main():
    # Load and explore data
    df = load_data(DATA_FILE_PATH)
    explore_data(df)

    # Clean the dataset
    df_cleaned = clean_data(df)

    # Save cleaned data for Elasticsearch indexing
    save_cleaned_data(df_cleaned, CLEANED_DATA_FILE_PATH)


if __name__ == "__main__":
    main()
