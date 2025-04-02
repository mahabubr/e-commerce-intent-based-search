from transformers import BartTokenizer, BartForConditionalGeneration

model_name = "facebook/bart-large-cnn"

model = BartForConditionalGeneration.from_pretrained(model_name)

tokenizer = BartTokenizer.from_pretrained(model_name)


def query(query: str):
    input_ids = tokenizer.encode(query, return_tensors="pt")

    output_ids = model.generate(input_ids, max_length=20, min_length=20, num_beams=6)

    output_text = tokenizer.decode(output_ids[0], skip_special_tokens=True)

    sentences = output_text.split(".")
    sentences = [s.strip() for s in sentences if s.strip()]

    longest_sentence = max(sentences, key=len)

    return longest_sentence
