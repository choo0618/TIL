import sys
sys.stdin = open('bj5587.txt','r')

def Find(T):
    for idx,f in enumerate(A[T]):
        if f>B[turn[T]]:return idx
    return -1
N=int(input())
A=[[int(input())for x in range(N)],[]]
for k in range(1,2*N+1):
    if not k in A[0]:A[1].append(k)
A[0].sort()
A[1].sort()
T,turn=0,[1,0]
while True:
    B=[0,0]
    B[T]=A[T].pop(0)
    while True:
        idx = Find(turn[T])
        if idx==-1 or not A[0] or not A[1]:break
        B[turn[T]] = A[turn[T]].pop(idx)
        T=turn[T]
    if not A[0] or not A[1]:break
    if B[0]>B[1]:T=0
    else:T=1
print(len(A[1]))
print(len(A[0]))