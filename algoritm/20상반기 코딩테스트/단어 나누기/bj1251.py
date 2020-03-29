import sys
sys.stdin = open('bj1251.txt','r')

S=input()
Len=len(S)
R=[]
for i in range(1,Len-2):
    for j in range(i+1,Len-1):
        R.append(S[:i][::-1]+S[i:j+1][::-1]+S[j+1:][::-1])
print(sorted(R)[0])