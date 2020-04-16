import sys
sys.stdin = open('bj8911.txt','r')

dx=[0,1,0,-1]
dy=[-1,0,1,0]
for t in range(int(input())):
    y,x,d,Y,X=0,0,0,set([0]),set([0])
    for c in input():
        if c=='F':y,x=y+dy[d],x+dx[d]
        elif c=='B':y,x=y-dy[d],x-dx[d]
        elif c=='R':d+=1;d%=4
        else:
            d-=1
            if d==-1:d=3
        if c in 'FB':Y.add(y);X.add(x)
    print(abs(max(Y)-min(Y))*abs(max(X)-min(X)))

