from collections import deque
dx=[1,0,-1,0]
dy=[0,1,0,-1]
def IS(y,x,Len):
    return -1<y<Len and -1<x<Len
def solution(board):
    Len=len(board)
    answer=[[10**9]*Len for _ in range(Len)]
    answer[0][0]=0
    Q=deque([(0,0,0,-1)])
    while Q:
        y,x,s,d=Q.popleft()
        for Dir in range(4):
            Y,X,S=y+dy[Dir],x+dx[Dir],s+100
            if d!=-1 and Dir!=d:S+=500
            if IS(Y,X,Len) and board[Y][X]==0 and answer[Y][X]>=S:
                answer[Y][X]=S
                Q.append((Y,X,S,Dir))
    return answer[-1][-1]
solution([[0,0,1,0],[0,0,0,0],[0,1,0,1],[1,0,0,0]])
solution([[0,0,0],[0,0,0],[0,0,0]])
solution([[0,0,0,0,0,0,0,1],[0,0,0,0,0,0,0,0],[0,0,0,0,0,1,0,0],[0,0,0,0,1,0,0,0],[0,0,0,1,0,0,0,1],[0,0,1,0,0,0,1,0],[0,1,0,0,0,1,0,0],[1,0,0,0,0,0,0,0]])