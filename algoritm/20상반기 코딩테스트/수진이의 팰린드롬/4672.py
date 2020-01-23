import sys
sys.stdin=open('4672.txt','r')

T=int(input())
for t in range(T):
    S=input()
    Dic={}
    for s in S:
        try:Dic[s]+=1
        except:Dic[s]=1
    R=0
    for v in Dic.values():R+=(v*(v+1))//2
    print("#%d %d"%(t+1,R))