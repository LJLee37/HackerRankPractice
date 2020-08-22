lines = []
visits = []
for i in range(7):
    aLine = list(map(int, input().split()))
    lines.append(aLine)
    visits.append([0] * len(aLine))

def solve(x, y):
    if x < 0 or y < 0 or x > 6 or y > 6:
        return 0

    if visits[y][x] != 0:
        return 0

    visits[y][x] = 1
    count = 1
    color = lines[y][x]

    if y < 6 and lines[y+1][x] == color:
        count += solve(x, y+1)
    if y > 0 and lines[y-1][x] == color:
        count += solve(x, y-1)
    if x < 6 and lines[y][x+1] == color:
        count += solve(x+1, y)
    if x > 0 and lines[y][x-1] == color:
        count += solve(x-1, y)

    return count

answer = 0
for y in range(7):
    for x in range(7):
        r = solve(x, y)
        if r >= 3:
            answer += 1

print(answer)