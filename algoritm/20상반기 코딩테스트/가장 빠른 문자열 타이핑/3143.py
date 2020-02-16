import sys
sys.stdin = open('3143.txt','r')

for t in range(int(input())):
    A,B=map(str,input().split())
    print('#%d %s'%(t+1,len(A.replace(B,'.'))))


