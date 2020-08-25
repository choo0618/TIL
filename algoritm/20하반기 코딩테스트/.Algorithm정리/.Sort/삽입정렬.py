import sys
sys.stdin = open('sort.txt','r')

# 삽입정렬
# 시간복잡도 O(N^2)
# 현재위치에서 앞으로 리스트를 확인하며 자리를 바꾼다.

def insertion_sort(List):
    for end in range(1, len(List)):
        for i in range(end,0,-1):
            if List[i-1]>List[i]:
                List[i-1],List[i]=List[i],List[i-1]
N=int(input())
L=[int(input())for x in range(N)]
insertion_sort(L)
print(L)