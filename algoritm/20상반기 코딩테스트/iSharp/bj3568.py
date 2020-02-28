import sys
sys.stdin = open('bj3568.txt','r')

# L=input().replace(',','').replace(';','').replace('[]','_').split()
# for i in range(1,len(L)):
#     P,p,n=L[0],'',' '
#     for idx,j in enumerate(L[i]):
#         if j in '_&*':p=j+p
#         else:n+=j
#     P+=p
#     P=P.replace('_','[]')
#     print(P+n+';')


for t in range(int(input())):
    A,*B=input().split()
    for b in B:
        i=0
        for c in b:i+=1 if not c in '[]*&,;' else 0
        print(A+b[len(b)-2:i-1:-1].replace('][','[]')+' '+b[:i]+';')
