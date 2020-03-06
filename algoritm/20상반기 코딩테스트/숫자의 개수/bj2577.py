import sys
sys.stdin = open('bj2577.txt','r')

M=[0]*10
for n in str(int(input())*int(input())*int(input())):M[int(n)]+=1
for p in M:print(p)