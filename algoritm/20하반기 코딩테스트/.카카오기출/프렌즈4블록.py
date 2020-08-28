def solution(m, n, board):
    for _ in range(m):
        board[_]=list(map(str,board[_]))
    board=list(map(list,zip(*board[::-1])))
    m,n=n,m
    answer = 0
    while True:
        tmp=[]
        Point=[[1]*n for _ in range(m)]
        for i in range(m-1):
            for j in range(n-1):
                if board[i][j] and board[i][j]==board[i+1][j]==board[i][j+1]==board[i+1][j+1]:
                    for y,x in (i,j),(i+1,j),(i,j+1),(i+1,j+1):
                        answer+=Point[y][x]
                        Point[y][x]=0
                        tmp.append((y,x))
        if not tmp:return answer
        for i,j in tmp:board[i][j]=0
        for i in range(m):
            chk=0
            for j in range(n-1,-1,-1):
                if board[i][j]==0:board[i].pop(j);chk+=1
            for _ in range(chk):board[i].append(0)
solution(4,5,['CCBDE', 'AAADE', 'AAABF', 'CCBBF'])
solution(6, 6, ["TTTANT", "RRFACC", "RRRFCC", "TRRRAA", "TTMMMF", "TMMTTJ"])
