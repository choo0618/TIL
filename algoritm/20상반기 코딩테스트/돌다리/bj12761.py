import sys
sys.stdin=open('bj12761.txt','r')

A,B,N,M=map(int,input().split())
Map=[987654321]*100001
Map[N]=0
Que=[(N,0)]
Check=0
while Que and not Check:
    Q=[]
    for q in Que:
        if q[0]==M:Check=1;break
        for idx,d in enumerate([-1,1,A,B,-A,-B,A,B]):
            state=q[0]+d
            turn=q[1]+1
            if idx==6 or idx==7:
                state=q[0]*d
            if -1<state<100001 and turn<Map[state]:
                Map[state]=turn
                Q.append((state,turn))
    Que=Q
print(Map[M])