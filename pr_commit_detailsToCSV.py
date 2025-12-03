###############################################################################
# pr_commit_detailsToCSV.py                                                   #
# Author: Gavin Faircloth (glf0016@auburn.edu)                                #
# Date: 12/1/25                                                               #
# Description: This script loads "pr_commit_details" dataset and converts it  #
# to a CSV file with specified columns.                                       #
###############################################################################

from datasets import load_dataset
import pandas as pd

# Load the pr_commit_details parquet file directly
df = pd.read_parquet("hf://datasets/hao-li/AIDev/pr_commit_details.parquet")

# Select and rename columns according to requirements
df_output = pd.DataFrame({
    'PRID': df['pr_id'],
    'PRSHA': df['sha'],
    'PRCOMMITMESSAGE': df['message'],
    'PRFILE': df['filename'],
    'PRSTATUS': df['status'],
    'PRADDS': df['additions'],
    'PRDELSS': df['deletions'],
    'PRCHANGECOUNT': df['changes'],
    'PRDIFF': df['patch'].str.encode('ascii', errors='ignore').str.decode('ascii')
})

df_output.to_csv("pr_commit_details.csv", index=False)