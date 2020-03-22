import sys
sys.stdin = open('sort.txt','r')

# 버블정렬
# 시간복잡도 O(N^2)
# 현재위치에서 뒤쪽으로 리스트를 확인하며 자리를 바꾼다.

def bubble_sort(List):
    for i in range(len(List)-1):
        for j in range(len(List)-1):
            if List[j] > List[j+1]:
                List[j],List[j+1]=List[j+1],List[j]
N=int(input())
L=[int(input())for x in range(N)]
bubble_sort(L)
print(L)