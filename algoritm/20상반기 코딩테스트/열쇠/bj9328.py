import sys
sys.stdin = open('bj9328.txt','r')

# print(ord('a'))
# print(ord('A'))
T=int(input())
for t in range(T):
    Key={'.':'.'}
    dx=[1,0,-1,0]
    dy=[0,1,0,-1]
    def IS(y,x):
        return -1<y<H and -1<x<W
    H,W=map(int,input().split())
    Arr=[list(map(str,input()))for y in range(H)]
    K=input()
    if K!='0':
        for k in K:Key[chr(ord(k)-32)]='.'
    St,R=[],0
    for i in range(H):
        for j in range(W):
            if (j==0 or j==W-1 or i==0 or i==H-1)and Arr[i][j]!='*':St.append((i,j))
    while True:
        Len=len(Key)
        Map=[[0]*W for _ in range(H)]
        Que=[]
        for q in St:
            if Arr[q[0]][q[1]] in Key or ord(Arr[q[0]][q[1]])>=97 or Arr[q[0]][q[1]]=='$':Que.append(q);Map[q[0]][q[1]]=1
        while Que:
            Q=[]
            for q in Que:
                if Arr[q[0]][q[1]]=='$':R+=1;Arr[q[0]][q[1]]='.'
                for d in range(4):
                    Y=q[0]+dy[d]
                    X=q[1]+dx[d]
                    if IS(Y,X) and Arr[Y][X]!='*' and not Map[Y][X]:
                        k=ord(Arr[Y][X])
                        if 97<=k:Key[chr(k-32)]='.'
                        elif 65<=k:
                            try:Arr[Y][X]=Key[Arr[Y][X]]
                            except:continue
                        Map[Y][X]=1
                        Q.append((Y,X))
            Que=Q
        if Len==len(Key):break
    print(R)

