from collections import Counter
import string
with open('canada.txt') as f:
    contents = f.read()
    list_contents = contents.split()
    stripped = contents.translate(str.maketrans({a:None for a in string.punctuation})).lower().split()

wordcount = Counter(stripped)


words = list(wordcount.items()) # .items() returns a list of tuples
words.sort(key=lambda tup: tup[1], reverse=True)  # sort largest to smallest, based on count
for i in range(min(10, len(words))):  # print the top 10 words, or all of them, whichever is smaller
    print(words[i])
