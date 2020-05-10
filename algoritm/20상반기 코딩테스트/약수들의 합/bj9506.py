import sys
sys.stdin = open('bj9506.txt','r')

while True:
    N=int(input())
    if N==-1:break
    L=[]
    R=[]
    for n in range(1,int(N**0.5)+1):
        if not N%n:
            L.append(n)
            R.append(N//n)
    L+=R[::-1]
    Sum=sum(L[:-1])
    if Sum==N:
        P=' + '.join(map(str,L[:-1]))
        print('%d = %s'%(N,P))
    else:print(N,'is NOT perfect.')
