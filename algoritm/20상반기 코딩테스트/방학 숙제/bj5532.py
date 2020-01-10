import sys
sys.stdin = open('bj5532.txt','r')

L=int(input())
A = [int(input())for x in range(4)]
l=[0,0]
for d in range(2):
    if A[d]%A[d+2]:l[d]=A[d]//A[d+2]+1
    else:l[d]=A[d]//A[d+2]
print(L-max(l))