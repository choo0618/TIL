dx=[0,1,0,-1]
dy=[1,0,-1,0]
def solution(maze):
    answer = 0
    N=len(maze)
    def IS(y,x):
        return -1<y<N and -1<x<N

    y,x,d,left=0,0,0,1
    while (y,x)!=(N-1,N-1):
        Y,X=y+dy[left],x+dx[left]
        if (IS(Y,X) and maze[Y][X]==0) or not (IS(y+dy[d],x+dx[d]) and maze[y+dy[d]][x+dx[d]]==0):
            left,d=(left+1)%4,(d+1)%4
            while not IS(y+dy[d],x+dx[d]) or maze[y+dy[d]][x+dx[d]]:
                left,d=(left-1)%4,(d-1)%4
                if left==-1:left=3
                if d==-1:d=3
        y,x=y+dy[d],x+dx[d]
        answer+=1
    print(answer)
    return answer

# solution([[0, 1, 0, 1], [0, 1, 0, 0], [0, 0, 0, 0], [1, 0, 1, 0]])
solution([[0, 1, 0, 0, 0, 0], [0, 1, 0, 1, 1, 0], [0, 1, 0, 0, 1, 0], [0, 1, 1, 1, 1, 0], [0, 1, 0, 0, 0, 0], [0, 0, 0, 1, 1, 0]])