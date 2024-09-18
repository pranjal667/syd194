import csv
from transformers import AutoTokenizer
from collections import Counter

# Function to count unique tokens and save to CSV
def count_unique_tokens(file_path, output_file_path, model_name='bert-base-uncased', top_k=30):
    # Initialize the tokenizer
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    
    # Read the input text file
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()

    # Tokenize the text
    tokens = tokenizer.tokenize(text)

    # Count the frequency of each token
    token_counts = Counter(tokens)

    # Get the top 'top_k' most common tokens
    top_tokens = token_counts.most_common(top_k)

    # Write the results to a CSV file
    with open(output_file_path, 'w', newline='', encoding='utf-8') as output_csv_file:
        csv_writer = csv.writer(output_csv_file)
        csv_writer.writerow(['Token', 'Count'])  # Write header
        csv_writer.writerows(top_tokens)

    print(f"Top {top_k} tokens and their counts saved in '{output_file_path}'.")

# Example usage
input_file_path = r'S:\present study material\master life\subjects\sem2\softwareNow\A2Syd194\output.txt'
output_file_path = r'S:\present study material\master life\subjects\sem2\softwareNow\A2Syd194\output_3.2.csv'
count_unique_tokens(input_file_path, output_file_path)
