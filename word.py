
# -*- coding: utf-8 -*-

import collections
from nltk.corpus import stopwords
stop_words = set(stopwords.words("English"))
print("stop_words", stop_words)
file=open('testing.txt')
wordcount={}

for word in file.read().lower().split():
	print ("word", word)
	word = word.replace(".","")
	word = word.replace(",","")
	word = word.replace("\"","")
	word = word.replace("“","")
	if word not in stop_words:
		if word not in wordcount:       
			wordcount[word] = 1
		else:
			wordcount[word] += 1
			d = collections.Counter(wordcount)

print(d.most_common(10))
for word, count in d.most_common(10):
	print(word, ": ", count)