import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

train_text = input()
stop_words = set(stopwords.words("english"))
words = word_tokenize(train_text)

filtered_sentence = [w for w in words if not w in stop_words]
print(filtered_sentence)

tagged_sentence= []

def process_content():
    try:
        for i in filtered_sentence:
            words = nltk.word_tokenize(i)
            tagged = nltk.pos_tag(words)
            tagged_sentence.append(tagged)
            print(tagged)
    except Exception as e:
        print(str(e))

process_content()

print(tagged_sentence)
arr0 = []
arr1 = []
arr2 = []

for k in tagged_sentence:
    if(k[0][1]=='NNP'):
        arr0.append(k[0][0])
    elif(k[0][1]=='NN' or k[0][1]=='NNS' or k[0][1]=='NNPS'):
        arr1.append(k[0][0])
    else:
          arr2.append(k[0][0])
print("This is 0th array")
print(arr0)    

print("This is first array")
print(arr1)

print("This is second array")
print(arr2)