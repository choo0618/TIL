import sys
sys.stdin = open('bj1039.txt','r')

N,K=map(int,input().split())
Q=[str(N)]
Len=len(str(N))
while K:
    que=set()
    for q in Q:
        List=list(map(str,q))
        for i in range(Len):
            for j in range(i+1,Len):
                if not i and List[j]=='0':continue
                List[i],List[j]=List[j],List[i]
                que.add(''.join(List))
                List[i],List[j]=List[j],List[i]
    Q=list(que)
    K-=1
print(max(int(x)for x in Q+[-1]))