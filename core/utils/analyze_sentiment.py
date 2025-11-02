from transformers import AutoTokenizer, AutoModelForSequenceClassification
from scipy.special import softmax
from functools import lru_cache
import numpy as np
import torch
import asyncio

_model = None
_tokenizer = None

def preload():
    global _model, _tokenizer
    if _model is None:

        Model = "cardiffnlp/twitter-roberta-base-sentiment"
        _tokenizer = AutoTokenizer.from_pretrained(Model)
        _model = AutoModelForSequenceClassification.from_pretrained(Model)

@lru_cache(maxsize=1000)
def encode_text(text):
    global _tokenizer 
    return _tokenizer(text, return_tensors='pt')

def return_logits(encoded_inputs):
    global _model
    with torch.no_grad():
        probs = _model(**encoded_inputs)
    return probs.logits[0].detach().numpy()

def turn_softmax(scores):
    return softmax(scores)

def idx_label(scores):
    labels = ['NEGATIVE', 'NEUTRAL', 'POSITIVE']
    idx = np.argmax(scores)
    return labels[idx]

async def analyze_setinment(text):
    encoded = encode_text(text)

    def _run_model():
        scores = return_logits(encoded)
        scores = turn_softmax(scores)
        label = idx_label(scores)
        confidence = round(float(np.max(scores)) * 100, 2)
        return label, confidence
   
    return await asyncio.to_thread(_run_model)
