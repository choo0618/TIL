import sys
sys.stdin = open('bj1213.txt','r')

S=[0]*26
for c in input():S[ord(c)-65]+=1
R,tmp,c=[],'',0
for i in range(26):
    if S[i]:
        R+=[chr(i+65)]*(S[i]//2)
        if S[i]%2:
            if not tmp:tmp=chr(i+65)
            else:c=1;break
if c:print('I\'m Sorry Hansoo')
else:print(''.join(R)+tmp+''.join(R[::-1]))
