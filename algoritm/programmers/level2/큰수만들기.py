def solution(number, k):
    R=[]
    for n in number:
        R.append(n)
        if len(R)>1 and k:
            i = len(R)-1
            while i:
                if R[i]>R[i-1]:
                    R[i],R[i-1] = R[i-1],R[i]
                    R.pop()
                    k-=1
                    if not k:break
                else:break
                i-=1
    if k:R=R[:len(R)-k]
    return ''.join(R)