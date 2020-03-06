import sys
sys.stdin = open('bj9489.txt','r')

N=int(input())
print('A' if N>=90 else 'B' if N>=80 else 'C' if N>=70 else 'D' if N>=60 else 'F')

if N>=90:print('A')
elif N>=80:print('B')
elif N>=70:print('C')
elif N>=60:print('D')
else:print('F')