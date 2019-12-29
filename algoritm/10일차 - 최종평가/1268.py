import sys
sys.stdin = open('1268.txt', 'r')

R,N,K = map(int,input().split())
Robot = [(map(int,input().split()))for _ in range(N)]
Robot = [[int(x)for x in input().split()]for _ in range(N)]
print(Robot)
for r in Robot:
    R_Set = set(Robot)
    print(R_Set)
    R_Set -= {r}
    print(R_Set)
    break