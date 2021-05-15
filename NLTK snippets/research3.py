from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize

ps = PorterStemmer()

##example_words = ["smart","smarting","smartest","smarter","smartly"]
##for w in example_words:
##    print(ps.stem(w))

new_text = "It is very important to be smartest in the room. No matter who is more smarter you or the other smart guy. We just have to choose smartly to be more smart."

words = word_tokenize(new_text)

for w in words:
    print(ps.stem(w))
