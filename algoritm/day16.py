import sys
sys.stdin = open("input.txt", "r")

# # Insertion Sort
# L=[int(x)for x in input().split()]
# for j in range(1,len(L)):
#     key=L[j]
#     i=j-1
#     while i>=0 and L[i]>key:
#         L[i+1]=L[i]
#         i-=1
#     L[i+1]=key
# print(L)

# # Merge Sort
# def merge(l,r):
#     x=y=k=0
#     lenth=len(l)+len(r)
#     result=[0]*lenth
#     while x<len(l) and y<len(r):
#         if l[x]>=r[y]:
#             result[k]=r[y]
#             y+=1
#         elif l[x]<r[y]:
#             result[k]=l[x]
#             x+=1
#         k+=1
#     while k!=lenth:
#         if x!=len(l):
#             result[k]=l[x]
#             x+=1
#         else:
#             result[k]=r[y]
#             y+=1
#         k+=1
#     return result
# def merge_sort(m):
#     if len(m)<=1:
#         return m
#     mid=len(m)//2
#     left=merge_sort(m[:mid])
#     right=merge_sort(m[mid:])
#     return merge(left,right)
# L=[int(x)for x in input().split()]
# print(merge_sort(L))

# # Linked List
# class Node:
#     def __init__(self,data,link=None):
#         self.data=data
#         self.link=link
# def Que(x):
#     global head
#     Newnode=Node(x)
#     if head==None:
#         head=Newnode
#     else:
#         p=head
#         if p.link:
#             while p.link:
#                 q=p.link
#                 if q.data>x:
#                     p.link=Newnode
#                     Newnode.link=q
#                     break
#                 p=p.link
#         p.link=Newnode
# L=[int(x)for x in input().split()]
# L.insert(0,0)
# head=None
# for n in L:
#     Que(n)
# head=head.link
# p=head
# while p:
#     print(p.data)
#     p=p.link

# Josephus Problem
# class Node:
#     def __init__(self,data,link=None):
#         self.data=data
#         self.link=link
# def Que(x):
#     global head
#     newnode=Node(x)
#     if head==None:
#         head=newnode
#     else:
#         p=head
#         while p.link:
#             q=p.link
#             p=p.link
#         p.link = newnode
#         if x==N-1:
#             newnode.link=head
# N=41
# head=None
# for man in range(N):
#     Que(man)
# p=head
# while p.link.link!=p:
#     p.link.link=p.link.link.link
#     p=p.link.link
#
# print(p.data+1)
# p = p.link
# print(p.data+1)