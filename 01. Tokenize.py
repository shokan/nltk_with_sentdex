from nltk.tokenize import sent_tokenize, word_tokenize

# nltk.download("all")

# tokenizing - word tokenizers ... sentence tokenizers
# lexicon - words and their means
# corpora - body of text. ex: medical journals, speeches etc.

# investe speak - regulat english speak
# invester speak bull = someone who is positive about marker
# english speak bull = scary animal you want running @ you

example = "Hello Mr. Smith, who are you doing today? The wather is greate and Python is awesome. The sky ic "
print(sent_tokenize(example))

for word in word_tokenize(example):
	print(word)