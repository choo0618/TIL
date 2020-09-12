def Check(y,x,i,j):
    if y==i and x==j:return 0
    if y==i or x==j:return 1
    else:return 2
def DFS(cnt,y,x,r,Dic,Max):
    global answer
    if r>answer:return
    if cnt==Max:
        answer=min(answer,r)
        return
    for i in range(1,Max+1):
        if V[i]:continue
        V[i]=1
        (y1,x1),(y2,x2),n=Dic[i]
        DFS(cnt+1,y2,x2,r+n+Check(y,x,y1,x1),Dic,Max)
        DFS(cnt+1,y1,x1,r+n+Check(y,x,y2,x2),Dic,Max)
        V[i]=0
answer=10**9
V=[0]*7
def solution(board, r, c):
    global answer
    Len=len(board)
    Dic={n:[] for n in range(1,7)}
    Max=0
    for i in range(Len):
        for j in range(Len):
            if board[i][j]:Dic[board[i][j]].append((i,j))
            Max=max(Max,board[i][j])
    for n in range(1,Max+1):
        (y,x),(i,j)=Dic[n]
        Dic[n].append(Check(y,x,i,j))

    DFS(0,r,c,0,Dic,Max)
    print(answer+2*Max)
    return answer+2*Max

# solution([[3, 0, 0, 2], [1, 0, 0, 0], [0, 0, 0, 1], [2, 0, 3, 0]], 1, 0)
solution([[3, 0, 0, 2], [0, 0, 1, 0], [0, 1, 0, 0], [2, 0, 0, 3]], 0, 1)