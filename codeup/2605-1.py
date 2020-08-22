lines = []
for i in range(7):
    aLine = list(map(int, input().split()))
    lines.append(aLine)

checked = []
def isAdjecent(i, j, fromI, fromJ):
    retval = 0
    if [i,j] in checked:
        return 0
    if i != fromI or j != fromJ:
        checked.append([i,j])
        retval += 1
    if i < 6:
        if lines[i][j] == lines[i + 1][j]:
            if retval == 0:
                retval += 1 # 현재의 칸.
                checked.append([i, j])
            retval += isAdjecent(i + 1, j, i, j)
    if j < 6:
        if lines[i][j] == lines[i][j + 1]:
            if retval == 0:
                retval += 1
                checked.append([i, j])
            retval += isAdjecent(i, j + 1, i, j)
    if i > 1:
        if [i - 1, j] not in checked:
            if lines[i][j] == lines[i - 1][j]:
                if retval == 0:
                    retval += 1
                    checked.append([i,j])
                retval += isAdjecent(i - 1, j, i, j)
    if j > 1:
        if [i, j - 1] not in checked:
            if lines[i][j] == lines[i][j - 1]:
                if retval == 0:
                    retval += 1
                    checked.append([i,j])
                retval += isAdjecent(i, j - 1, i, j)

    return retval

def solve():
    count = 0
    for i in range(7):
        for j in range(7):
            #if [i,j] not in checked:
                if isAdjecent(i,j,i,j) >= 3:
                    count += 1
    print(count)

solve()