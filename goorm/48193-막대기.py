sticks = []
n = int(input())
for i in range(n):
    sticks.append(int(input()))
sticks.reverse()
curHeight = sticks[0]
count = 1
for i in sticks:
    if i > curHeight:
        curHeight = i
        count += 1
print(count)
