###############################################################################
# all_pull_requestToCSV.py                                                    #
# Author: Gavin Faircloth (glf0016@auburn.edu)                                #
# Date: 12/1/25                                                               #
# Description: This script loads "all_pull_request" dataset and converts it to#
# a CSV file with specified columns.                                          #
###############################################################################

from datasets import load_dataset
import pandas as pd

dataset = load_dataset("hao-li/AIDev", split="train")

df = pd.DataFrame(dataset)

# Select and rename columns according to requirements
df_output = pd.DataFrame({
    'TITLE': df['title'],
    'ID': df['id'],
    'AGENTNAME': df['agent'],
    'BODYSTRING': df['body'],
    'REPOID': df['repo_id'],
    'REPOURL': df['repo_url']
})

df_output.to_csv("all_pull_request.csv", index=False)

