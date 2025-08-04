word=input()
listword=[]
for x in word:
    if x.lower() not in "aeiouy":
        listword.append("."+x.lower())
print("".join(listword))

