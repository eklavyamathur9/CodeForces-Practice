word1=input()
word2=input()
w1=word1.lower()
w2=word2.lower()
n=len(word1)
c=0
for x in range(n):
    if w1[x]==w2[x]:
        c=0 
    elif w1[x]<w2[x]:
        c=-1
        break
    else:
        c=1
        break
print(c)
