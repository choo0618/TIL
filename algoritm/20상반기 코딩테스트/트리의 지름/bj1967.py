import sys
sys.stdin=open('bj1967.txt','r')

N=int(input())
Dic={}
A=[[int(x)for x in input().split()]for y in range(N-1)]
for n in range(1,N+1):Dic[n]=[]
for q in A:Dic[q[0]].append((q[1],q[2]))
Que,R=[],0
que=[1]
while que:
    node=que.pop(0)
    Que.append(node)
    for q in Dic[node]:
        que.append(q[0])
MaxNode=[0]*(N+1)
Max=[[0]for _ in range(N+1)]
Len=[0]*(N+1)
while Que:
    node = Que.pop()
    for child in Dic[node]:
        m=child[1]+MaxNode[child[0]]
        Max[node].append(m)
        Len[node]=max(Max[node])
    MaxNode[node] += max(Max[node])
    Max[node].remove(max(Max[node]))
    try:Len[node]+=max(Max[node])
    except:pass
print(max(Len))
