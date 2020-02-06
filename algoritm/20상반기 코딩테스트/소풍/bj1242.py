import sys
sys.stdin=open('bj1242.txt','r')

N,K,M=map(int,input().split())
for i in range(1,N+1):
    n=K%(N-i+1) if K%(N-i+1) else N-i+1
    if M==n:break
    M=M-n if M>n else (M-n)+N-i+1
print(i)
