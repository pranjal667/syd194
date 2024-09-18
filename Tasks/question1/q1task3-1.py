import os
import spacy
import csv
from collections import Counter

# To load the spaCy model use the following code:
nlp_model = spacy.load("en_core_sci_sm") 
nlp_model.max_length = 750000000

# Update the path of the input and output file
input_file_path = r'/Users/krishkc/Documents/assignment2_SoftwareNow/output.txt'
output_file_path = r'/Users/krishkc/Documents/assignment2_SoftwareNow/word_frequencies.numbers'



# Function to process the text and count word frequencies as per the required question
def get_word_frequencies(text):
    processed_doc = nlp_model(text)
    words_list = [token.text.lower() for token in processed_doc if token.is_alpha]
    word_frequencies = Counter(words_list)
    return word_frequencies

# To read the input text file
with open(input_file_path, 'r', encoding='utf-8') as file:
    input_text = file.read()

word_frequencies = get_word_frequencies(input_text)

top_30_common_words = word_frequencies.most_common(30)

# To write the results to a CSV file
with open(output_file_path, 'w', newline='', encoding='utf-8') as output_csv_file:
    csv_writer = csv.writer(output_csv_file)
    csv_writer.writerow(['Word', 'Count'])  # Write header
    csv_writer.writerows(top_30_common_words)

print(f"Top 30 common words and their counts saved in '{output_file_path}'.")