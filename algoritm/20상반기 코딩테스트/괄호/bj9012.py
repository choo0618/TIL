import sys
sys.stdin = open('bj9012.txt','r')

for t in range(int(input())):
    Q=[]
    for i in input():
        if i=='(':Q.append(1)
        else:
            if Q:Q.pop()
            else:Q.append(1);break
    print('NO' if Q else 'YES')
