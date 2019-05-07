import sys
sys.stdin = open('bj.17140.txt','r')

def R():
    r=0
    for i in range(len(A)):
        M=[0]*101
        l=[]
        ll=[]
        for j in range(len(A[i])):
            if A[i][j]:M[A[i][j]]+=1
        for k in range(101):
            if M[k]:
                l.append([k,M[k]])
        l.sort(key=lambda t:t[1])
        for z in l:
            if len(ll)<=100:ll+=z
        if len(ll)>r:r=len(ll)
        A[i]=ll
    for m in range(len(A)):
        if len(A[m])!=r:
            A[m]+=[0]*(r-len(A[m]))
def C():
    global A
    A=list(map(list,zip(*A[::-1])))
    R()
    A=list(map(list, zip(*A[::1])))
def check():
    if len(A)>L[0]-1 and len(A[0])>L[1]-1:
        if A[L[0]-1][L[1]-1]==L[2]:return True
    return False
L=[int(x)for x in input().split()]
A=[[int(x)for x in input().split()]for y in range(3)]
Result=0
while True:
    if Result>100:Result=-1;break
    if check():break
    if len(A)>=len(A[0]):
        R()
        Result+=1
    if check():break
    if len(A)<len(A[0]):
        C()
        Result+=1
    if check():break
print(Result)