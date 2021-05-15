from nltk.tokenize import sent_tokenize, word_tokenize

example_text = "Hello there, how are you."
example_text2 = "Hello there, how are you doing today? The weather is great and Python is awesome."
example_text3 = "Hello Mr. Manish Swami, how are you doing today? The weather is great and Python is awesome."

print(word_tokenize(example_text))
print(word_tokenize(example_text2))
print(word_tokenize(example_text3))
