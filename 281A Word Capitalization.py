word=input()
l1=word[0].upper()
final=[l1]
n=len(word)
for x in range(1,n):
    final.append(word[x])
print("".join(final))
    
