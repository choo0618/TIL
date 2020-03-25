# 1000 까지 확인
Map=[0,0]+[1]*999
for i in range(2,1000**0.5+1):    # N의 루트까지 확인
    if not Map[i]:continue
    for j in range(i,1000//i+1):Map[i*j]=0     # i의 배수 지우기