def solution(A, B, C, D):
    Num = []
    Num.append(A)
    Num.append(B)
    Num.append(C)
    Num.append(D)
    Num.sort()
    Result = set()
    for x_idx, x in enumerate(Num):
        if x > 2: break

        for y_idx, y in enumerate(Num):
            if x == 2 and y >= 4: break
            if x_idx == y_idx: continue

            for z_idx, z in enumerate(Num):
                if z_idx == x_idx or z_idx == y_idx: continue
                if z > 5: break
                Result.add((x, y, z))

    return len(Result)

print(solution(4,4,4,4))