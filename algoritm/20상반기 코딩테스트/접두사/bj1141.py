import sys
sys.stdin = open('bj1141.txt','r')

N=int(input())
L=[input()for _ in range(N)]
L.sort(key=len)
L.reverse()
cnt=0
for i in range(1,N):
    for j in range(0,i):
        if L[j] and L[j][:len(L[i])]==L[i]:
            L[i]=0
            cnt+=1
            break
print(N-cnt)