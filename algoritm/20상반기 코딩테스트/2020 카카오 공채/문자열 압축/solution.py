def Check(n,S,Len):
    r=''
    idx=0
    while idx<Len:
        tmp=1
        s=S[idx:idx+n]
        while True:
            idx+=n
            if S[idx:idx+n]==s:tmp+=1
            else:break
        if tmp==1:r+=s
        else:r+=str(tmp)+s
    return len(r)
def solution(s):
    Len=len(s)
    answer=Len
    for n in range(1,Len//2+1):
        answer=min(answer,Check(n,s,Len))
    return answer

print(solution('xababcdcdababcdcd'))