Dic={'U':(0,1),'L':(-1,0),'R':(1,0),'D':(0,-1)}
def IS(y,x):
    return -5<=y<=5 and -5<=x<=5
def solution(dirs):
    answer=set()
    y,x=0,0
    for d in dirs:
        dx,dy=Dic[d]
        Y,X=y+dy,x+dx
        if IS(Y,X):
            answer.add((y,x,Y,X))
            answer.add((Y,X,y,x))
            y,x=Y,X
    return len(answer)//2