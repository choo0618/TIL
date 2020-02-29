import sys
sys.stdin = open('bj11719.txt','r')

while True:
    try:print(input())
    except:break

import sys
print(sys.stdin.read())