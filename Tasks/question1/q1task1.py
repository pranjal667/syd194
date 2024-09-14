#Question 1
#Task1: Extract the ‘text’ in all the CSV files and store them into a single ‘.txt file’.

import os
import pandas as pd

# Specify the directory where your CSV files are located
csv_folder = 'S:\present study material\master life\subjects\sem2\softwareNow\csvFiles'

# Specify the output directory
output_folder = 'S:\present study material\master life\subjects\sem2\softwareNow\syd194\Tasks\question1'

# Create the output directory if it doesn't exist
os.makedirs(output_folder, exist_ok=True)

# Specify the output text file within the output directory
output_txt_file = os.path.join(output_folder, 'output.txt')

# Function to extract only text data from the CSV file
def extract_text_from_csv(csv_file):
    df = pd.read_csv(csv_file, dtype=str)  
    text_data = []

    # Loop through all the cells and filter out non-textual data
    for row in df.values:
        text_row = [cell for cell in row if isinstance(cell, str) and not cell.isdigit()]
        text_data.append('\t'.join(text_row))  

    return '\n'.join(text_data) 

# List all CSV files in the specified folder
csv_files = [file for file in os.listdir(csv_folder) if file.endswith('.csv')]

# Open the output text file in append mode
with open(output_txt_file, 'a', encoding='utf-8') as output_file:
    # Loop through each CSV file and extract text
    for csv_file in csv_files:
        csv_path = os.path.join(csv_folder, csv_file)
        extracted_text = extract_text_from_csv(csv_path)
        
        # Write the extracted text to the output text file
        output_file.write(f"=== {csv_file} ===\n{extracted_text}\n\n")

print(f"Text extracted from all CSV files and stored in '{output_txt_file}'.")


