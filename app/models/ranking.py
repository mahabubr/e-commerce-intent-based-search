from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch
import json

model_name = "cross-encoder/ms-marco-MiniLM-L6-v2"

tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSequenceClassification.from_pretrained(model_name)


def product_score(search, product):
    inputs = tokenizer(
        [search, product["Description"]],
        padding=True,
        truncation=True,
        return_tensors="pt",
    )

    with torch.no_grad():
        outputs = model(**inputs)

    score = outputs.logits.squeeze().tolist()

    return score


def ranking(search, result):
    product_scores = []

    for product in result:
        score = product_score(search, product)
        product_scores.append((product, score))

    sorted_product_scores = sorted(
        product_scores, key=lambda x: (x[1][0], x[1][1]), reverse=True
    )

    sorted_result_with_score = [
        {"product": product, "score": score} for product, score in sorted_product_scores
    ]

    return sorted_result_with_score
