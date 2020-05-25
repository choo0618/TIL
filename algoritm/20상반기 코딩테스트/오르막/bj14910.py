import sys
sys.stdin = open('bj14910.txt','r')

L=[-1000000]
R='Good'
for x in map(int,input().split()):
    if x>=L[-1]:L.append(x)
    else:R='Bad';break
print(R)