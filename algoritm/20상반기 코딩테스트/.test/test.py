import sys
sys.stdin = open('test.txt','r')

for N in range(1,11):
    S=''
    while N:
        N,b=divmod(N,3)
        S+='412'[b]
        if not b:N-=1
    print(S[::-1])