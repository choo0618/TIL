import sys
sys.stdin = open('bj3425.txt','r')

while True:
    L = []
    tmp=0
    while True:
        l=list(map(str,input().split()))
        if l[0]=='QUIT':
            tmp=1
            break
        if l[0]=='END':break
        try:l[1]=int(l[1])
        except:pass
        L.append(l)
    if tmp:break
    N=int(input())
    for n in range(N):
        Stack,E = [int(input())],0
        for l in L:
            try:
                if l[0]=='NUM':Stack.insert(0,l[1])
                elif l[0]=='POP':Stack.pop(0)
                elif l[0]=='INV':Stack[0]*=-1
                elif l[0]=='DUP':Stack.insert(0,Stack[0])
                elif l[0]=='SWP':Stack[0],Stack[1]=Stack[1],Stack[0]
                elif l[0]=='ADD':Stack[0]+=Stack.pop(1)
                elif l[0]=='SUB':Stack[0]=Stack.pop(1)-Stack[0]
                elif l[0]=='MUL':Stack[0]*=Stack.pop(1)
                elif l[0]=='DIV':
                    t=1
                    if (Stack[0]>0 and Stack[1]<0) or (Stack[0]<0 and Stack[1]>0):t=-1
                    Stack[0]=abs(Stack.pop(1))//abs(Stack[0])
                    Stack[0]*=t
                else:
                    t=1
                    if Stack[1]<0:t=-1
                    Stack[0]=abs(Stack.pop(1))%abs(Stack[0])
                    Stack[0]*=t
            except:
                E=1
                break
        if E or len(Stack)!=1 or abs(Stack[0])>10**9:print('ERROR')
        else:print(Stack[0])
    print(input())