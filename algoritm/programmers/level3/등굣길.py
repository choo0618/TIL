def solution(m, n, puddles):
    M=[[0]*m for _ in range(n)]
    for p in puddles:
        M[p[1]-1][p[0]-1]= -1
    M[0][0]=1
    for y in range(n):
        for x in range(m):
            if M[y][x]==-1 or (not y and not x):continue
            else:
                left=0
                if y-1>-1 and M[y-1][x]!=-1:left=M[y-1][x]
                up=0
                if x-1>-1 and M[y][x-1]!=-1:up=M[y][x-1]
                M[y][x]=left+up
    return M[n-1][m-1]%1000000007