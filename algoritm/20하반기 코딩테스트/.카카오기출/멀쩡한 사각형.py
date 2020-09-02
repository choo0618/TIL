def Find(a,b):
    while b:
        a,b=b,a%b
    return a
def solution(w,h):
    Max=Find(w,h)
    return w*h-(w+h-Find(w,h))
    return w*h-Max*(w//Max+h//Max-1)
solution(8,12)