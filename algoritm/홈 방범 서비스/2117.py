import sys
sys.stdin = open('2117.txt','r')

dx=[1,0,-1,0]
dy=[0,1,0,-1]
T=int(input())
for n in range(T):
    L=[int(x)for x in input().split()]
    A=[[int(x)for x in input().split()]for y in range(L[0])]
    H,R=[],0
    for i in range(L[0]):
        for j in range(L[0]):
            if A[i][j]:H.append([i,j])
    for i in range(L[0]):
        for j in range(L[0]):
            h,r=[],0
            for z in H:h.append(abs(z[0]-i)+abs(z[1]-j)+1)
            k=1
            while k<=max(h):
                m,hm=k*k+(k-1)*(k-1),0
                for c in h:
                    if c<=k:hm+=L[1]
                if hm-m>=0:
                    if r<hm//L[1]:r=hm//L[1]
                k+=1
            if r>R:R=r
    print('#%d %d'%(n+1,R))