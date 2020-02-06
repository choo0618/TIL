import sys
sys.stdin = open('bj11726.txt','r')


N=int(input())
Map=[0,1,2]+[0]*(N-2)
for m in range(3,N+1):
    Map[m]=(Map[m-1]+Map[m-2])%10007
print(Map[N])