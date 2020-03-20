import sys
sys.stdin = open('bj9251.txt','r')

S1=' '+input()
l1=len(S1)
S2=' '+input()
l2=len(S2)
DP=[[0]*l1 for _ in range(l2)]
for i in range(1,l2):
    for j in range(1,l1):
        DP[i][j]=max(DP[i-1][j],DP[i][j-1],DP[i-1][j-1]+(S1[j]==S2[i]))
print(DP[-1][-1])