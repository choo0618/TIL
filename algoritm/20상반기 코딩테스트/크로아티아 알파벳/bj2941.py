import sys
sys.stdin = open('bj2941.txt','r')

S=input()
for s in ('c=','c-','dz=','d-','lj','nj','s=','z='):S=S.replace(s,'0')
print(len(S))