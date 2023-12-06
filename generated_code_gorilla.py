
from transformers import pipeline

def load_model():
    nlp = pipeline("text-generation", model="facebook/opt-66b", tokenizer="facebook/opt-66b", device=0)
    return nlp

def process_data(prompt, nlp):
    response = nlp(prompt, max_length=100, do_sample=True, temperature=0.7)
    return response[0]['generated_text'].strip()

prompt = "Hello world"

# Load the model
nlp = load_model()

# Process the data
response = process_data(prompt, nlp)

print(response)