import sys
sys.stdin = open('test.txt','r')

DP=[0]*101
for i in range(1,101):
    for j in range(i,101,i):DP[j]=1^DP[j]
for t in range(int(input())):
    print(sum(DP[1:int(input())+1]))