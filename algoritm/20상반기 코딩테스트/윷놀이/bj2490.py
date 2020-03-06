import sys
sys.stdin = open('bj2490.txt','r')

for i in range(3):print('EABCD'[input().count('0')])