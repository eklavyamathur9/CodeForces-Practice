word=input()
cu=0
cl=0
for x in word:
    if x.islower():
        cl+=1
    elif x.isupper():
        cu+=1
if cu>cl:
    print(word.upper())
else:
    print(word.lower())