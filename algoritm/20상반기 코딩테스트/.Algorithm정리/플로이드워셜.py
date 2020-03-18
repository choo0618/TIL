# A정점에서 B정점으로 최소 이동거리를 구하고 싶을떄

N=int(input())
Map=[[]]    # A>>B 이동 거리가 주어진
for k in range(N):
    for i in range(N):
        for j in range(N):
            Map[i][j]=min(Map[i][j],Map[i][k]+Map[k][j])
print(Map[A][B])