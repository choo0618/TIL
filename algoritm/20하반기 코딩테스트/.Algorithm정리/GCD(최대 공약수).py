# GCD 최대 공약수 구하기
def GCD(a,b):
    while b:
        a,b=b,a%b
    return a

GCD(a,b)