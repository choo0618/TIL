import sys
sys.stdin = open('Test2.txt','r')

N,K=map(int,input().split())
L=[int(x)for x in input().split()]
Result=(N-1)//(K-1)
if (N-1)%(K-1):Result+=1
print(Result)

for t in range(int(input())):
    N,M=map(int,input().split())
    x,y=N//5,(N+M)//12
    Result=x
    if x>=y:R=y
    while N+M<=12*Result and Result:Result-=1
    print(Result)