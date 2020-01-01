import sys
sys.stdin = open('bj17825.txt','r')

def DFS(Idx,r,state):
    global R,cnt
    if Idx == 10:
        cnt+=1
        if r>R:R=r
        return
    for m in [1,2,3,4]:
        if state[m]=='f':continue
        s = State[state[m]][List[Idx]]
        if not s in state or s=='f':
            tmp = state[m]
            state[m]=s
            if s=='f':DFS(Idx+1,r,state)
            else:DFS(Idx+1,r+Score[s],state)
            state[m] = tmp
List = [int(x)for x in input().split()]
# [],2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,13,16,19,22,24,28,27,26,25,30,35,40,[]
#    1 2 3 4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32
Score = [0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,13,16,19,22,24,28,27,26,25,30,35,40]
State=[
[0,1,2,3,4,5],
[1,2,3,4,5,6],
[2,3,4,5,6,7],
[3,4,5,6,7,8],
[4,5,6,7,8,9],
[5,20,21,22,28,29],
[6,7,8,9,10,11],
[7,8,9,10,11,12],
[8,9,10,11,12,13],
[9,10,11,12,13,14],
[10,23,24,28,29,30],
[11,12,13,14,15,16],
[12,13,14,15,16,17],
[13,14,15,16,17,18],
[14,15,16,17,18,19],
[15,25,26,27,28,29],
[16,17,18,19,31,'f'],
[17,18,19,31,'f','f'],
[18,19,31,'f','f','f'],
[19,31,'f','f','f','f'],
[20,21,22,29,30,31],
[21,22,28,29,30,31],
[22,28,29,30,31,'f'],
[23,24,28,29,30,31],
[24,28,29,30,31,'f'],
[25,26,27,28,29,30],
[26,27,28,29,30,31],
[27,28,29,30,31,'f'],
[28,29,30,31,'f','f'],
[29,30,31,'f','f','f'],
[30,31,'f','f','f','f'],
[31,'f','f','f','f','f'],]
R = 0
cnt=0
DFS(0,0,[0,0,0,0,0])
print(cnt)