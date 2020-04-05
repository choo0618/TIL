def solution(directory, command):
    for c in command:
        C=c.split(' ')
        if C[0]=='mkdir':
            directory.append(C[1])
        elif C[0]=='rm':
            Len=len(C[1])
            n=0
            while n!=len(directory):
                if directory[n][:Len]==C[1]:
                    directory.pop(n)
                else:n+=1
        else:
            Len=len(C[1])
            New=[]
            if C[2]=='/':C[2]=''
            for d in directory:
                if C[1]==d[:Len]:
                    for i in range(len(C[1])-1,-1,-1):
                        if C[1][i]=='/':break
                    New.append(C[2]+d[i:])
            directory+=New
    print(directory)
    return directory

solution([
"/",
"/hello",
"/hello/tmp",
"/root",
"/root/abcd",
"/root/abcd/etc",
"/root/abcd/hello"
],
    [
        "mkdir /root/tmp",
        "cp /hello /root/tmp",
        "rm /hello"
    ],

)
solution([
"/"
],
    [
        "mkdir /a",
        "mkdir /a/b",
        "mkdir /a/b/c",
        "cp /a/b /",
        "rm /a/b/c"
    ]
)