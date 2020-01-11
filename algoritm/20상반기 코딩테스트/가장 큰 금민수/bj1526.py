import sys
sys.stdin = open('bj1526.txt','r')

# def DFS(str):
#     global R
#     if str and int(str)<=N:
#         if int(str)>R:
#             R=int(str)
#     if str and int(str)>N:
#         return
#     for s in ['7','4']:
#         DFS(str+s)
#
# N,R = int(input()),0
# DFS('')
# print(R)

a=input()
while sum(i not in'47'for i in a):
    a=str(int(a)-1)
print(a)