import sys
sys.stdin = open('bj5587.txt','r')

N=int(input())
A=[[int(input())for x in range(N)],[]]
for k in range(1,2*N+1):
    if not k in A[0]:A[1].append(k)
A[0].sort()
A[1].sort()
turn=0
while True:
    s,k=0,0
    B=[0,0]
    B[turn]=A[turn].pop(0)
    turn=0
    while True:
        if not turn:
            try:
                while A[(turn+1)%2][k]<B[turn]:
                    k+=1
                    if k==len(A[(turn+1)%2]):break
                B[(turn+1)%2]=A[(turn+1)%2].pop(k)
            except:break
        else:
            try:
                while A[(turn+1)%2][s]<B[turn]:
                    s+=1
                    if k==len(A[(turn+1)%2]):break
                B[(turn+1)%2]=A[(turn+1)%2].pop(s)
            except:break
        turn+=1
        turn%=2
    if not len(A[0]) or not len(A[1]):break
print(len(A[1]))
print(len(A[0]))