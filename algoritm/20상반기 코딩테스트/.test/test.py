import sys
sys.stdin = open('test.txt','r')

a,b,c=map(int,input().split())
print(a**b%c)