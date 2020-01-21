import sys
sys.stdin=open('bj1967.txt','r')

N=int(input())
Dic={}
A=[[int(x)for x in input().split()]for y in range(N-1)]
for n in range(1,N+1):Dic[n]=[]
for q in A:Dic[q[0]].append((q[1],q[2]))
Que,R=[],0
que=[1]
while que:
    node=que.pop(0)
    Que.append(node)
    for q in Dic[node]:
        que.append(q[0])
MaxNode=[0]*(N+1)
Max=[[0]for _ in range(N+1)]
Len=[0]*(N+1)
while Que:
    node = Que.pop()
    for child in Dic[node]:
        m=child[1]+MaxNode[child[0]]
        Max[node].append(m)
        Len[node]=max(Max[node])
    MaxNode[node] += max(Max[node])
    Max[node].remove(max(Max[node]))
    try:Len[node]+=max(Max[node])
    except:pass
print(max(Len))



# node = int(input())
# tree_info = [[] for _ in range(node + 1)]
#
# for _ in range(node - 1):
#     parent, child, length = map(int, input().split())
#     tree_info[parent].append((child, length))
#
#
# # BFS함수로 정렬하기
# def bfs(graph_list, start):
#     visited = []
#     queue = [start]
#
#     while queue:
#         node = queue.pop(0)
#         visited.append(node)
#         for child in graph_list[node]:
#             queue.append(child[0])
#
#     return visited
#
#
# # 정렬에 쓸 리스트 생성
# bfs_node = bfs(tree_info, 1)
# max_node = [0 for _ in range(node + 1)]
# diameter = [[0] for _ in range(node + 1)]
# max_diameter = [0 for _ in range(node + 1)]
#
# # 최하단의 노드부터 일방향 최댓값, 지름 최댓값 추출
# while bfs_node:
#     temp = bfs_node.pop()
#
#     for child in tree_info[temp]:
#         try:
#             child_length = max_node[child[0]] + child[1]
#         except:
#             child_length = child[1]
#         diameter[temp].append(child_length)
#         max_node[temp] = max(diameter[temp])
#
#     max_diameter[temp] += max(diameter[temp])
#     diameter[temp].remove(max(diameter[temp]))
#     try:
#         max_diameter[temp] += max(diameter[temp])
#     except:
#         pass
# print(max(max_diameter))