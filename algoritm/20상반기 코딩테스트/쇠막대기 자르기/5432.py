import sys
sys.stdin=open('5432.txt','r')

for t in range(int(input())):
    S=input()
    S=S.replace('()','L')
    Q,R=[],0
    for s in S:
        if s=='(':Q.append(s);R+=1
        elif s==')':Q.pop()
        else:R+=len(Q)
    print('#%d %d'%(t+1,R))