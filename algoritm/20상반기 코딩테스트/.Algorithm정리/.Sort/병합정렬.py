import sys
sys.stdin = open('sort.txt','r')

# 머지소트
# 시간복잡도 O(NlogN)
# 리스트를 분리하여 정렬 진행

def Merge(Left,Right):
    Sort=[]
    LenL,LenR=len(Left),len(Right)
    l,r=0,0
    while l<LenL or r<LenR:
        if l<LenL and r<LenR:
            if Left[l]<=Right[r]:
                Sort.append(Left[l])
                l+=1
            else:
                Sort.append(Right[r])
                r+=1
        elif l<LenL:
            Sort.append(Left[l])
            l+=1
        elif r<LenR:
            Sort.append(Right[r])
            r+=1
    return Sort

def Merge_sort(List):
    if len(List)<=1:
        return List
    Mid=len(List)//2
    Left=Merge_sort(List[:Mid])
    Right=Merge_sort(List[Mid:])

    return Merge(Left,Right)

N=int(input())
L=[int(input())for x in range(N)]
for p in Merge_sort(L):print(p)