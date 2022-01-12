from transformers import AutoTokenizer, AutoModelForTokenClassification
from transformers import pipeline

tokenizer = AutoTokenizer.from_pretrained("sagorsarker/mbert-bengali-ner")
model = AutoModelForTokenClassification.from_pretrained("sagorsarker/mbert-bengali-ner")

nlp = pipeline("ner", model=model, tokenizer=tokenizer)
example = "আমি জাহিদ এবং আমি ঢাকায় বাস করি।"

ner_results = nlp(example)
print(ner_results)