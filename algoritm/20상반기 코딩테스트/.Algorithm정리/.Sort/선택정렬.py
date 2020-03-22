import sys
sys.stdin = open('sort.txt','r')

# 선택정렬
# 시간복잡도 O(N^2)
# 선택한 값과 남은 값들의 최소값과 변경

def selection_sort(List):
    for i in range(len(List) - 1):
        min_idx=i
        for j in range(i+1,len(List)):
            if List[j]<List[min_idx]:
                min_idx=j
        List[i],List[min_idx]=List[min_idx],List[i]

N=int(input())
L=[int(input())for x in range(N)]
selection_sort(L)
print(L)