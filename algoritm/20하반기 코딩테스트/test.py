Map = [[1],[0,2],[0,1,3,4],[2,4],[0]]
def countPerms(n):
    DP = [[1]*5]+[[0]*5 for _ in range(n-1)]
    for i in range(n-1):
        for j in range(5):
            tmp = DP[i][j]
            for k in Map[j]:
                DP[i+1][k]+=tmp
    print(sum(DP[-1])%1000000007)
    return sum(DP[-1])%1000000007
countPerms(100000)