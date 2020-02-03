import sys
sys.stdin = open('bj10250.txt','r')


for t in range(int(input())):
    H,W,N=map(int,input().split())
    F=N%H
    ho=N//H+1
    if not F:F=H;ho-=1
    F=str(F)
    Ho=str(ho)
    if len(Ho)==1:Ho='0'+Ho
    print(F+Ho)