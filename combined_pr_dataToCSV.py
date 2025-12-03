###############################################################################
# combined_pr_dataToCSV.py                                                    #
# Author: Gavin Faircloth (glf0016@auburn.edu)                                #
# Date: 12/2/25                                                               #
# Description: This script combines data from multiple CSVs to create a       #
# comprehensive pull request dataset with security flagging.                  #
###############################################################################

import pandas as pd
import re

# Security-related keywords (add more as needed from your References)
SECURITY_KEYWORDS = [
    'race', 'racy', 'buffer', 'overflow', 'stack', 'integer', 'signedness',
    'underflow', 'improper', 'unauthenticated', 'gain access', 'permission',
    'cross site', 'css', 'xss', 'denail service', 'dos', 'crash', 'deadlock',
    'injection', 'request forgery', 'csrf', 'xsrf', 'forged', 'security',
    'vulnerability', 'vulnerable', 'exploit', 'attack', 'bypass', 'backdoor',
    'threat', 'expose', 'breach', 'violate', 'fatal', 'blacklist', 'overrun',
    'insecure'
]

# Load the CSVs
print("Loading CSV files...")
df_pr = pd.read_csv("all_pull_request.csv")
df_task_type = pd.read_csv("pr_task_type.csv")

# Merge the dataframes on pull request ID
print("Merging data...")
df_combined = pd.merge(
    df_pr[['ID', 'TITLE', 'AGENTNAME', 'BODYSTRING']],
    df_task_type[['PRID', 'PRTYPE', 'CONFIDENCE']],
    left_on='ID',
    right_on='PRID',
    how='inner'
)

# Function to check for security keywords
def check_security(row):
    """Check if security-related keywords appear in title or body"""
    text = str(row['TITLE']).lower() + ' ' + str(row['BODYSTRING']).lower()
    
    for keyword in SECURITY_KEYWORDS:
        if re.search(r'\b' + re.escape(keyword) + r'\b', text):
            return 1
    return 0

# Apply security check
print("Checking for security keywords...")
df_combined['SECURITY'] = df_combined.apply(check_security, axis=1)

# Select and rename final columns
df_output = pd.DataFrame({
    'ID': df_combined['ID'],
    'AGENT': df_combined['AGENTNAME'],
    'TYPE': df_combined['PRTYPE'],
    'CONFIDENCE': df_combined['CONFIDENCE'],
    'SECURITY': df_combined['SECURITY']
})

# Save to CSV
print("Saving to CSV...")
df_output.to_csv("combined_pr_data.csv", index=False)

print(f"Done! Created combined_pr_data.csv with {len(df_output)} records")
print(f"Security flagged PRs: {df_output['SECURITY'].sum()}")
