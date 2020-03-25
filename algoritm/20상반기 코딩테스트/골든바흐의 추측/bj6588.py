import sys
sys.stdin = open('bj6588.txt','r')

Map=[1]*1000001
Map[0]=Map[1]=0
for i in range(2,int(1000000**0.5+1)):
    if not Map[i]:continue
    for j in range(i,1000000//i+1,):Map[i*j]=0
while True:
    N=int(sys.stdin.readline())
    if not N:break
    R=[]
    for n in range(2,N//2+1):
        if Map[n] and Map[N-n]:break
    print('%d = %d + %d'%(N,n,N-n))