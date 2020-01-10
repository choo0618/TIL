import sys
sys.stdin = open('bj1057.txt','r')

N,K,L = map(int,input().split())
R = 0
while K!=L:
    K=(K+1)//2
    L=(L+1)//2
    R+=1
print(R)


#             89
#      18             9 13
#   13    58     911      1315
# 12 34 56 78 910 1112 1314 1516