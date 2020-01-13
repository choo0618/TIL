import sys
sys.stdin = open('bj2980.txt','r')

N,L = map(int,input().split())
A = [[int(x)for x in input().split()]for y in range(N)]
T,Now = 0,0
for a in A:
    T+=a[0]-Now
    Now+=a[0]-Now
    tmp = T % (a[1]+a[2])
    if tmp<=a[1]:T+=a[1]-tmp
print(T+L-Now)
