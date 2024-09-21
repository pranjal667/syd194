import spacy
from concurrent.futures import ThreadPoolExecutor

# Load the spaCy model
nlp = spacy.load("en_core_sci_sm")
nlp.disable_pipes('parser', 'ner')

# Check available labels in the model
print("Available Entity Labels:", nlp.get_pipe('ner').labels)

# Function to process a batch of text
def process_batch(batch):
    docs = nlp.pipe(batch, disable=["parser", "ner"])

    # Extract entities (adjust labels based on your model)
    diseases = []
    drugs = []

    for doc in docs:
        diseases.extend([ent.text for ent in doc.ents if ent.label_ == "DISEASE"])
        drugs.extend([ent.text for ent in doc.ents if ent.label_ == "CHEMICAL"])

    return diseases, drugs

# Function to read file and split at sentence boundaries
def process_large_text_file(file_path, chunk_size=10 * 1024 * 1024, batch_size=10):
    with open(file_path, "r", encoding="utf-8") as file:
        buffer = ''
        while True:
            chunk = file.read(chunk_size)
            if not chunk:
                break  # End of file
            buffer += chunk

            # Ensure the chunk ends at sentence boundary (try splitting by '\n')
            sentences = buffer.split('\n')
            buffer = sentences.pop()  # Keep the last incomplete sentence in buffer

            # Yield batches of sentences
            while len(sentences) >= batch_size:
                yield sentences[:batch_size]
                sentences = sentences[batch_size:]

            # Put remaining sentences back into the buffer
            buffer = '\n'.join(sentences) + buffer

        # Yield any remaining sentences
        if buffer.strip():
            yield [buffer.strip()]

# Process each batch of chunks concurrently
def process_batches(batches):
    with ThreadPoolExecutor() as executor:
        results = list(executor.map(process_batch, batches))

    # Aggregate results
    all_diseases = [disease for result in results for disease in result[0]]
    all_drugs = [drug for result in results for drug in result[1]]

    # Print the extracted diseases and drugs
    print("Diseases:", all_diseases)
    print("Drugs:", all_drugs)

    return all_diseases, all_drugs

# Example usage:
file_path = 'S:\present study material\master life\subjects\sem2\softwareNow\A2Syd194\output.txt'
chunk_size = 1000000  # Adjust as needed
batch_size = 10
batches = process_large_text_file(file_path, chunk_size=chunk_size, batch_size=batch_size)

# Process batches
process_batches(batches)