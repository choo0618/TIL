import sys
sys.stdin = open('스마트밴드.txt','r')

Max=220-int(input())
Result=[0]*6
Chk=[]
for _ in (60,68,75,80,90):
    Chk.append(Max*_/100)
while True:
    try:M=int(input())
    except:break
    if M<Chk[0]:Result[5]+=1
    elif M<Chk[1]:Result[4]+=1
    elif M<Chk[2]:Result[3]+=1
    elif M<Chk[3]:Result[2]+=1
    elif M<Chk[4]:Result[1]+=1
    else:Result[0]+=1
print(Result)

