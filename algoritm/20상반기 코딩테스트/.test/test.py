import sys
sys.stdin = open('test.txt','r')

input()
print(*sorted({*input().split()},key=int))
# print(*sorted({*input().split()}))
print(*[1,2,3,4,5])