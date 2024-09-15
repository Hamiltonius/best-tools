
# Creating a list of life activities as per the user's request
# 

import pandas as pd

activities = [
    "Visit Hack the Box",
    "Visit Pentesterlab",
    "Work on homework and get an A",
    "Make dentist appointments",
    "Get base access",
    "Dieting",
    "Sleep 8 hours",
    "Exercise",
    "Drink 160 ounces of water per day",
    "Brush teeth",
    "Straighten teeth",
    "Pay off debt",
    "Keep budget in line",
    "Pay credit card each month with checking",
    "Get bikes for the kids",
    "Stretch neck (chronic pain)",
    "Training/Study for CFCM"
]

# Creating a DataFrame to store the life activities with columns for tracking progress
df = pd.DataFrame({
    'Life Activities': activities,
    'Status': ['Pending'] * len(activities),
    'Notes': [''] * len(activities)
})

# Saving the DataFrame as an Excel file with a 'Sept 2024 items' tab
file_path = '/Users/tgalarneau2024/Desktop/life_tracker_sept_2024.xlsx'
with pd.ExcelWriter(file_path, engine='xlsxwriter') as writer:
    df.to_excel(writer, sheet_name='Sept 2024 items', index=False)

# Output the path to the created Excel file
file_path
