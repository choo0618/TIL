import sys
sys.stdin = open('sort.txt','r')

# 카운팅소
# 시간복잡도 O(N)
# 속도는 빠르나 최대값을 구해 카운팅 리스트를 만들어야하므로 숫자가 매우크면 메모리면에서 비효율적이다.

Counting=[0]*10001
N=int(input())
for _ in range(N):
    Counting[int(input())]+=1
for i in range(10001):
    sys.stdout.write('%s\n'%i*Counting[i])