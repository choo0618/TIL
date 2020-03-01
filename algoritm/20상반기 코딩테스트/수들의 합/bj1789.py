import sys
sys.stdin = open('bj1789.txt','r')

N,t=int(input()),2
while N>0:
    N-=t
    t+=1
print(t-2)