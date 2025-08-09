word1=input()
word2=input()
w1=word1.lower()
w2=word2.lower()
if w2==w1[::-1]:
    print('YES')
else:
    print('NO')
