from transformers import AutoTokenizer

tokenizer = AutoTokenizer.from_pretrained("gpt2")

text = "I wanted to go to school"

# Text to token
text_to_token = tokenizer.tokenize(text)

# Text => token ids
ids = tokenizer.encode(text)

# Token Id => text
decode = tokenizer.decode(ids)


print("Text to token: ", text_to_token)
print("Token IDs: ", ids)
print("Token length: ", len(ids))
print("Decode: ", decode)