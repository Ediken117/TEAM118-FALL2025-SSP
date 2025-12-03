###############################################################################
# all_repositoryToCSV.py                                                      #
# Author: Gavin Faircloth (glf0016@auburn.edu)                                #
# Date: 12/1/25                                                               #
# Description: This script loads "all_repository" dataset and converts it to  #
# a CSV file with specified columns.                                          #
###############################################################################

from datasets import load_dataset
import pandas as pd

# Load the all_repository parquet file directly
df = pd.read_parquet("hf://datasets/hao-li/AIDev/all_repository.parquet")

# Select and rename columns according to requirements
df_output = pd.DataFrame({
    'REPOID': df['id'],
    'LANG': df['language'],
    'STARS': df['stars'],
    'REPOURL': df['url']
})

df_output.to_csv("all_repository.csv", index=False)
