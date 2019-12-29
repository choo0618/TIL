import sys
sys.stdin = open('bj17779.txt','r')

def Sum(y1,x1,y2,x2,y3,x3,y4,x4):
    Map=[0]*5
    J1=x1+1
    for y in range(0,y2):
        if y>=y1:J1-=1
        Map[0] += sum(Arr[y][:J1])

    J2=x1+1
    for y in range(0,y3+1):
        if y>=y1+1:J2+=1
        Map[1] += sum(Arr[y][J2:])

    J3=x2-1
    for y in range(y2,N):
        if y<=y4:J3+=1
        Map[2] += sum(Arr[y][:J3])

    J4=x3+1
    for y in range(y3+1,N):
        if y<=y4+1:J4-=1
        Map[3] += sum(Arr[y][J4:])

    Map[4] = T-sum(Map)
    # print(Map, max(Map)-min(Map))
    # print(y1,x1,y2,x2,y3,x3,y4,x4)
    return max(Map)-min(Map)

N = int(input())
Arr = [list(map(int,input().split()))for _ in range(N)]
Result = 987654321
T = 0
for s in Arr:
    T += sum(s)
for i1 in range(0,N-2):
    for j1 in range(1,N-1):
        for d1 in range(1,j1+1):
            for d2 in range(1,N-j1):
                i2,j2 = i1+d1,j1-d1
                i3,j3 = i1+d2,j1+d2
                i4,j4 = i2+d2,j2+d2
                if not 0<i4<N and 0<j4<N:break
                r = Sum(i1,j1,i2,j2,i3,j3,i4,j4)
                # print(r)
                if r<Result:Result=r
print(Result)
