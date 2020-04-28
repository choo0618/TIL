import sys
sys.stdin = open('bj11723.txt','r')

# def AE(x):
#     for i in range(1,21):S[i]=x
# S=[0]*21
# for t in range(int(input())):
#     a,*b=map(str,input().split())
#     if b:b=int(b[0])
#     if a=='add':S[b]=1
#     elif a=='remove':S[b]=0
#     elif a=='check':print(1 if S[b] else 0)
#     elif a=='toggle':S[b]=0 if S[b] else 1
#     elif a=='all':AE(1)
#     else:AE(0)

S=[]
for t in range(int(input())):
    L=input().split()
    if L[0]=='add':
        if not L[1] in S:S.append(L[1])
    elif L[0]=='remove':
        if L[1] in S:S.remove(L[1])
    elif L[0]=='check':print(1 if L[1] in S else 0)
    elif L[0]=='toggle':
        if L[1] in S:S.remove(L[1])
        else:S.append(L[1])
    elif L[0]=='all':S=['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20']
    else:S=[]
