lines = []
for i in range(7):
    aLine = list(map(int, input().split()))
    lines.append(aLine)
def solve(y, x):
    count = 0
    color = lines[y][x]
    if (lines[y + 1][x] == color):
        count += 1
        count += solve(y + 1, x)
for y in range(7):
    for x in range(7):
        print(x, y, lines[y][x])