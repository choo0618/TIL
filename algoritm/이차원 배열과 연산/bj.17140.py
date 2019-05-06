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
            ll+=z
        if len(ll)>r:r=len(ll)
        A[i]=ll
    for m in range(len(A)):
        if len(A[m])!=r:
            A[m]+=[0]*(r-len(A[m]))
def C():
    R()
L=[int(x)for x in input().split()]
A=[[int(x)for x in input().split()]for y in range(3)]

print(L)
print(A)
Result=0
while True:
    # if A[L[0]-1][L[1]-1]==L[2]:break
    if len(A)<=len(A[0]):R()
    Result+=1
    # if A[L[0]-1][L[1]-1]==L[2]:break
    A=list(map(list, zip(*A[::-1])))
    if len(A)>len(A[0]):
        C()
        for i in range(len(A)):
            for j in range(i+1,len(A[0]),1):
                A[i][j],A[j][i]=A[j][i],A[i][j]
    Result+=1
    # if A[L[0]-1][L[1]-1]==L[2]: break
print(Result)