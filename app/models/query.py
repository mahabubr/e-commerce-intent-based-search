from transformers import BartTokenizer, BartForConditionalGeneration

model_name = "facebook/bart-large-cnn"

model = BartForConditionalGeneration.from_pretrained(model_name)

tokenizer = BartTokenizer.from_pretrained(model_name)

print(sum(p.numel() for p in model.parameters() if p.requires_grad))


def query(query: str):
    input_ids = tokenizer.encode(query, return_tensors="pt")

    output_ids = model.generate(input_ids, max_length=62, num_beams=5)

    output_text = tokenizer.decode(output_ids[0], skip_special_tokens=True)

    return output_text.split(".")
