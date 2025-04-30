import pandas as pd

# Read the Excel file
df = pd.read_excel('europe.xlsx')

# Convert the DataFrame to a CSV file
csv_file = 'europe.csv'  # The name of the output CSV file
df.to_csv(csv_file, index=False)
