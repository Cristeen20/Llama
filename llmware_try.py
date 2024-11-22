
import sklearn
import sklearn.metrics # for cosine similarity
from llmware.prompts import Prompt
import time
import os
from sentence_transformers import SentenceTransformer
import PyPDF2

# Initialize the embedding model
model = SentenceTransformer('all-MiniLM-L6-v2')
reader = "do you know"
#PdfReader([path to PDF of tax cuts and jobs act]) 

embeddings = []
for pg in reader.pages:
    text = pg.extract_text() 
    embedding = model.encode(text)
    embeddings.append(embedding)

question = 'What is a qualified opportunity zone partnership interest?'
q_embed = model.encode(question)

cos_sim = [(idx, sklearn.metrics.pairwise.cosine_similarity([e], [q_embed])[0][0]) for idx, e in enumerate(embeddings)]
most_relevant = sorted(cos_sim, key=lambda x: x[1], reverse=True)[0][0]

model_name = "llmware/dragon-llama-7b-gguf"
prompter = Prompt().load_model(model_name)

response = prompter.prompt_main(question, context='\n\n'.join([reader.pages[132].extract_text()]), 
                                prompt_name="default_with_context", temperature=0.3)

print(response['llm_response'])
