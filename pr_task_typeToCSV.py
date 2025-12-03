###############################################################################
# pr_task_typeToCSV.py                                                        #
# Author: Gavin Faircloth (glf0016@auburn.edu)                                #
# Date: 12/1/25                                                               #
# Description: This script loads "pr_task_type" dataset and converts it to    #
# a CSV file with specified columns.                                          #
###############################################################################

from datasets import load_dataset
import pandas as pd

# Load the pr_task_type parquet file directly
df = pd.read_parquet("hf://datasets/hao-li/AIDev/pr_task_type.parquet")

# Select and rename columns according to requirements
df_output = pd.DataFrame({
    'PRID': df['id'],
    'PRTITLE': df['title'],
    'PRREASON': df['reason'],
    'PRTYPE': df['type'],
    'CONFIDENCE': df['confidence']
})

df_output.to_csv("pr_task_type.csv", index=False)
