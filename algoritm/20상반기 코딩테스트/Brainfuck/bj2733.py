import sys
sys.stdin = open('bj2733.txt','r')

T=int(input())
for t in range(T):
    print('PROGRAM #%d:'%(t+1))
    A=''
    Map,Q={},[]
    while True:
       I=input()
       if I=='end':break
       for i in I:
           if i=='%':break
           if i in '<>+-.[]':A+=i
    Check=0
    for i in range(len(A)):
        if A[i]=='[':Q.append(i)
        elif A[i]==']':
            if not Q:Check=1;break
            a=Q.pop()
            Map[a]=(a,i)
            Map[i]=(a,i)
    if Q:Check=1
    if Check:print('COMPILE ERROR')
    else:
        R=''
        map,P,cnt,idx = [0]*32768,0,0,0
        while cnt!=1280000:
            if A[idx]=='>':
                P+=1
                P%=32767
            elif A[idx]=='<':
                P-=1
                if P<0:P=32767
            elif A[idx]=='+':
                map[P]+=1
                map[P]%=255
            elif A[idx]=='-':
                map[P]-=1
                if map[P]<0:map[P]=255
            elif A[idx]=='.':R+=chr(map[P])
            elif A[idx]=='[':
                if not map[P]:idx=Map[idx][1];cnt+=1;continue
            elif A[idx]==']':
                if map[P]:idx=Map[idx][0];cnt+=1;continue
            idx+=1
            if idx==len(A):print(R);break
            cnt+=1
    if cnt==1280000:print('COMPILE ERROR')


#
# T=int(input())
# for t in range(T):
#     print('PROGRAM #%d:'%(t+1))
#     A=''
#     Check=0
#     while True:
#        I=input()
#        if I=='end':break
#        for i in I:
#            if i=='%':break
#            if i in '<>+-.[]':A+=i
#     Map={}
#     for idx,a in enumerate(A):
#         check=0
#         if a=='[':
#             tmp,check1=0,1
#             for a1 in range(idx+1,len(A)):
#                 if A[a1]=='[':tmp+=1
#                 elif A[a1]==']':
#                     if tmp:tmp-=1
#                     else:
#                         Map[idx]=(idx,a1)
#                         Map[a1]=(idx,a1)
#                         check1=0
#                         break
#             if check1:check=1
#         if check:Check=1
#     if Check:print('COMPILE ERROR')
#     else:
#         R=''
#         map,P,cnt,idx = [0]*32768,0,0,0
#         while cnt!=1280000:
#             if A[idx]=='>':
#                 P+=1
#                 P%=32767
#             elif A[idx]=='<':
#                 P-=1
#                 if P<0:P=32767
#             elif A[idx]=='+':
#                 map[P]+=1
#                 map[P]%=255
#             elif A[idx]=='-':
#                 map[P]-=1
#                 if map[P]<0:map[P]=255
#             elif A[idx]=='.':R+=chr(map[P])
#             elif A[idx]=='[':
#                 if not map[P]:idx=Map[idx][1];cnt+=1;continue
#             elif A[idx]==']':
#                 if map[P]:idx=Map[idx][0];cnt+=1;continue
#             idx+=1
#             if idx==len(A):print(R);break
#             cnt+=1
#     if cnt==1280000:print('COMPILE ERROR')
#     print(Map)