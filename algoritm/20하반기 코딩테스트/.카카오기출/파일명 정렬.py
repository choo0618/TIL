def solution(files):
    Len=len(files)
    for i in range(Len):
        Chk=1
        e=len(files[i])
        for j in range(e):
            if Chk and files[i][j].isdigit():s,Chk=j,0
            elif Chk==files[i][j].isdigit()==0:e=j;break
        files[i]=[files[i],files[i][:s].upper(),files[i][s:e],files[i][e:],i]
    files.sort(key=lambda x:(x[1],int(x[2]),x[-1]))
    for i in range(Len):
        files[i]=files[i][0]
    return files

solution(["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"])
