import sys
sys.stdin = open('bj1094.txt','r')

X = int(input())
print(X)
R,r = 0,0
Stick = [64,32,16,8,4,2,1,1]
for s in Stick:
    if s <= X and R+s <= X:
        R+=s
        r+=1
print(r)

# print(bin(int(input())).count('1'))