"""
Serverless BERT Question-Answering API
Created by Mohamed Amine EL MOUSSAOUI
Email: maelmoussaoui1@gmail.com
Created: April 15, 2024
Last modified: April 28, 2024

Description: Lambda handler for BERT question-answering API using HuggingFace transformers
"""

from transformers import AutoModelForQuestionAnswering, AutoTokenizer

def get_model(model):
  """Loads model from Hugginface model hub"""
  try:
    model = AutoModelForQuestionAnswering.from_pretrained(model,use_cdn=True)
    model.save_pretrained('./model')
  except Exception as e:
    raise(e)
  
def get_tokenizer(tokenizer):
  """Loads tokenizer from Hugginface model hub"""
  try:
    tokenizer = AutoTokenizer.from_pretrained(tokenizer)
    tokenizer.save_pretrained('./model')
  except Exception as e:
    raise(e)
  
get_model('mrm8488/mobilebert-uncased-finetuned-squadv2')
get_tokenizer('mrm8488/mobilebert-uncased-finetuned-squadv2')