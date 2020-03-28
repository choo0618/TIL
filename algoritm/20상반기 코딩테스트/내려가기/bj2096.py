import sys
sys.stdin = open('bj2096.txt','r')

N=int(input())
Max=[0]*5
Min=[0]*5
tmp1=[0]*5
tmp2=[10**9]*5
for i in range(N):
    L=[int(x)for x in input().split()]
    for j in range(1,4):tmp1[j]=max(Max[j-1],Max[j],Max[j+1])+L[j-1]
    for i in range(1,4):Max[i]=tmp1[i]
    for j in range(1,4):tmp2[j]=min(Min[j-1],Min[j],Min[j+1])+L[j-1]
    for i in range(5):Min[i]=tmp2[i]
print(max(Max),min(Min))


