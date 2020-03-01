import sys
sys.stdin = open('bj1924.txt','r')

M=[0,31,28,31,30,31,30,31,31,30,31,30,31]
D=['SUN','MON','TUE','WED','THU','FRI','SAT']
x,y=map(int,input().split())
print(D[(sum(M[:x])+y)%7])
