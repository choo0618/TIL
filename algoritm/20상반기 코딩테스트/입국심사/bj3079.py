import sys
sys.stdin = open('bj3079.txt','r')

def Check():
    p=0
    for i in T:p+=Mid//i
    if M<=p:return True
    return False
N,M=map(int,input().split())
T=[int(input())for _ in range(N)]
L,R=0,M*max(T)
while L<=R:
    Mid=(L+R)//2
    if Check():R=Mid-1
    else:L=Mid+1
print(L)

def Check():
    p=0
    for i in T:p+=Mid//i
    if M<=p:return True
    return False
for t in range(int(input())):
    N,M=map(int,input().split())
    T=[int(input())for _ in range(N)]
    L,R=0,M*max(T)
    while L<=R:
        Mid=(L+R)//2
        if Check():R=Mid-1
        else:L=Mid+1
    print('#%d %d'%(t+1,L))