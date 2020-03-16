def solution(n, money):
    DP=[1]+[0]*(n)
    for c in money:
        for i in range(c,n+1):
            if DP[i-c]:DP[i]+=DP[i-c]
    print(DP)
    return DP[n]

# def solution(n, money):
#     DP=[[0]*(n+1)for _ in range(len(money))]
#     DP[0][0]=1
#     for i in range(money[0],n+1,money[0]):DP[0][i]=1
#     for i in range(1,len(money)):
#         for j in range(n+1):
#             if j>=money[i]:DP[i][j]=(DP[i-1][j]+DP[i][j-money[i]])%1000000007
#             else:DP[i][j]=DP[i-1][j]
#     print(DP)
#     return DP[-1][-1]

solution(5,[1,2,5])