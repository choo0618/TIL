import sys
sys.stdin = open('bj2669.txt','r')

Set=set()
for i in range(4):
    x1,y1,x2,y2=map(int,input().split())
    for i in range(y1,y2):
        for j in range(x1,x2):Set.add((i,j))
print(len(Set))