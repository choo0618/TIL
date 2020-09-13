def DFS(n,cnt):
    a,b=divmod(int(n),10)
    if cnt>=answer[1]:return
    if a==0:
        answer[0]=n
        answer[1]=cnt
        return
    Len=len(n)
    for i in range(Len-1):
        x,y=n[:i+1],n[i+1:]
        if (i!=1 and x[0]=='0') or (i!=Len-1 and y[0]=='0'):continue
        DFS(str(int(x)+int(y)),cnt+1)

def solution(n):
    answer=[10**9,0]

    def DFS(n, cnt):
        a,b=divmod(int(n),10)
        if cnt>=answer[0]:return
        if a==0:
            answer[0]=cnt
            answer[1]=int(n)
            return
        Len=len(n)
        for i in range(Len-1):
            x,y=n[:i+1],n[i+1:]
            if (i!=1 and x[0]=='0') or (i!=Len-1 and y[0]=='0'):continue
            DFS(str(int(x)+int(y)),cnt+1)

    DFS(str(n), 0)
    print(answer)
    return answer

solution(9)
solution(73425)