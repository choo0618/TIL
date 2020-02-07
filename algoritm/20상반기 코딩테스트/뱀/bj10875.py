import sys
sys.stdin = open('bj10875.txt','r')

dx=[1,0,-1,0]
dy=[0,-1,0,1]
def Check(t):
    global R,Die,Dir
    Next=(Now[0]+int(L[0])*dx[Dir],Now[1]+int(L[0])*dy[Dir])
    if L[1]=='L':Dir=Dir-1 if Dir-1>=0 else 3
    elif L[1]=='R':Dir=(Dir+1)%4
    tmp=1 if Now[0]!=Next[0] else 0
    idx=0
    for q in Q:
        a,b,c,d=min(q[0][0],q[1][0]),max(q[0][0],q[1][0]),min(q[0][1],q[1][1]),max(q[0][1],q[1][1])
        if idx==len(Q)-1:continue
        if tmp:  # 가로
            if a<=Next[0]<=b and Next[1]==q[0][1]==q[1][1]:R+=r-abs(a-Next[0]);Die=1;return  # 가로 가로
            if c<=Next[1]<=d and q[0][0]==q[1][0] and min(Now[0],Next[0])<=q[0][0]<=max(Now[0],Next[0]):R+=r-abs(Next[0]-q[0][0]);Die=1;return  # 가로 세로
        else:
            if c<=Next[1]<=d and Next[0]==q[0][0]==q[1][0]:R+=r-abs(d-Next[1]);Die=1;return  # 세로 세로
            if a<=Next[0]<=b and q[0][1]==q[1][1] and min(Now[1],Next[1])<=q[0][1]<=max(Now[1],Next[1]):R+=r-abs(Next[1]-q[0][1]);Die=1;return  # 세로 가로
        idx+=1
    if abs(Next[0])>N:Die=1;R+=N-abs(Now[0])+1;return
    elif abs(Next[1])>N:Die=1;R+=N-abs(Now[1])+1;return
    R+=r
    Q.append((Now, Next))
    return Next
N=int(input())
T=int(input())
Q=[]
Now,Dir,R,Die=(0,0),0,0,0
while not Die:
    try:L=input().split()
    except:L=[1,0]
    r=int(L[0])
    Next=Check(0)
    Now=Next
print(R)

