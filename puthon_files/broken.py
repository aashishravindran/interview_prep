text="Hellooooooooo World"
letters=["h","e","l","o","d"]

import string

for s in string.punctuation:
	text=text.replace(s,"")

print(text)
setval= set(letters)

text=text.lower().split()
print(text)

count=0;
j=0
for char in text:
	if char[0] in setval:
		j=1
		while j<len(char) and char[j] in setval:
			j+=1
	if j==len(char):
		count+=1

print(count)
