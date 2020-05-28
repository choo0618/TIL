import sys
sys.stdin = open('bj5373.txt','r')

Dic={'U':0,'F':9,'D':18,'L':27,'R':36,'B':45}
R=[
    [38,37,36,11,10,9,29,28,27,47,46,45],
    [36,39,42,20,19,18,35,32,29,6,7,8],
    [42,43,44,51,52,53,33,34,35,15,16,17],
    [9,12,15,18,21,24,53,50,47,0,3,6],
    [45,48,51,26,23,20,17,14,11,8,5,2],
    [27,30,33,24,25,26,44,41,38,2,1,0],
]
def Ro(i):
    D=R[i//9]
    a,b,c=C[D[0]],C[D[1]],C[D[2]]
    for r in range(0,9,3):C[D[r]],C[D[r+1]],C[D[r+2]]=C[D[r+3]],C[D[r+4]],C[D[r+5]]
    C[D[9]],C[D[10]],C[D[11]]=a,b,c
    C[i],C[i+1],C[i+2],C[i+3],C[i+5],C[i+6],C[i+7],C[i+8]=C[i+2],C[i+5],C[i+8],C[i+1],C[i+7],C[i],C[i+3],C[i+6]
for t in range(int(input())):
    C=[]
    for c in 'wrygbo':C+=list(c*9)
    input()
    for c,d in map(str,input().split()):
        for t in range(1 if d=='-' else 3):Ro(Dic[c])
    for p in [0,3,6]:print(''.join(C[p:p+3]))