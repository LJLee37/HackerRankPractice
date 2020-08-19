T = int(input())
for i in range(T):
    li = []
    a, b = map(int,input().split())
    for j in range(b):
        if a ** j in li:
            break
        li.append(a ** j)
    n = b % len(li)
    print(n + 1)
