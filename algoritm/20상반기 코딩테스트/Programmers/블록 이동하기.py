from collections import deque
dx=[1,1,-1,-1]
dy=[1,-1,1,-1]
def IS(y1,x1,y2,x2,N):
    return -1<y1<N and -1<x1<N and -1<y2<N and -1<x2<N
def solution(board):
    N=len(board)
    Map=[[[[0]*N for _ in range(N)]for __ in range(N)]for ___ in range(N)]
    Map[0][0][0][1]=1
    Q=deque([(0,0,0,1,0)])
    while Q:
        y1,x1,y2,x2,c=Q.popleft()
        if (y1,x1)==(N-1,N-1) or (y2,x2)==(N-1,N-1):print(c);return c
        for Y1,X1,Y2,X2 in (y1,x1+1,y2,x2+1),(y1+1,x1,y2+1,x2),(y1,x1-1,y2,x2-1),(y1-1,x1,y2-1,x2):
            if IS(Y1,X1,Y2,X2,N) and board[Y1][X1]==board[Y2][X2]==0 and not Map[Y1][X1][Y2][X2]:
                Map[Y1][X1][Y2][X2]=1
                Q.append((Y1,X1,Y2,X2,c+1))
        if y1==y2:  # 가로
            for d,Y1,X1,Y2,X2 in (0,y1+1,x1+1,y2,x2),(1,y1,x1,y2+1,x2-1),(2,y1-1,x1+1,y2,x2),(3,y1,x1,y2-1,x2-1):
                if IS(Y1,X1,Y2,X2,N) and board[Y1][X1]==board[Y2][X2]==0:
                    if (d==0 or d==1) and (board[y1+1][x1] or board[y2+1][x2]):continue
                    if (d==2 or d==3) and (board[y1-1][x1] or board[y2-1][x2]):continue
                    if Y1>Y2:Y1,X1,Y2,X2=Y2,X2,Y1,X1
                    if Map[Y1][X1][Y2][X2]:continue
                    Map[Y1][X1][Y2][X2]=1
                    Q.append((Y1,X1,Y2,X2,c+1))
        elif x1==x2:    # 세로
            for d,Y1,X1,Y2,X2 in (0,y1+1,x1+1,y2,x2),(1,y1,x1,y2-1,x2+1),(2,y1+1,x1-1,y2,x2),(3,y1,x1,y2-1,x2-1):
                if IS(Y1,X1,Y2,X2,N) and board[Y1][X1]==board[Y2][X2]==0:
                    if (d==0 or d==1) and (board[y1][x1+1] or board[y2][x2+1]):continue
                    if (d==2 or d==3) and (board[y1][x1-1] or board[y2][x2-1]):continue
                    if X1>X2:Y1,X1,Y2,X2=Y2,X2,Y1,X1
                    if Map[Y1][X1][Y2][X2]:continue
                    Map[Y1][X1][Y2][X2]=1
                    Q.append((Y1,X1,Y2,X2,c+1))

solution([[0, 0, 0, 1, 1],[0, 0, 0, 1, 0],[0, 1, 0, 1, 1],[1, 1, 0, 0, 1],[0, 0, 0, 0, 0]])