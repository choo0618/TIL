import sys
sys.stdin = open('bj10039.txt','r')

print(sum(max(8,int(input())//5)for _ in range(5)))

print(sum(max(40,int(input()))//5 for _ in range(5)))

R=0
for i in range(5):
    r=int(input())
    R+=r//5 if r>=40 else 8
print(R)