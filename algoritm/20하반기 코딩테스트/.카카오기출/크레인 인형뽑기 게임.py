def solution(board, moves):
    answer=0
    board=list(map(list,zip(*board[::-1])))
    Stack=[]
    for i in moves:
        i-=1
        if not board[i]:continue
        while board[i][-1]==0:board[i].pop()
        tmp=board[i].pop()
        if Stack and Stack[-1]==tmp:answer+=2;Stack.pop()
        else:Stack.append(tmp)
    return answer

solution([[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]],[1,5,3,5,1,2,1,4])