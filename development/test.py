from transformers import pipeline

# distilbert-base-uncased-finetuned-sst-2-english
classifer = pipeline("sentiment-analysis")

res = classifer("Man I really do enjoy doing research! Was that sarcasm or was it not?")

print(res)