n = int(input())

def is_palindrome(s):
    n = len(s)//2
    l = len(s)
    for i in range(n):
        if s[i] != s[l - i - 1]:
            return False
    return True

def remove_at1(s,i):
    return s[:i] + s[i+1:]

def remove_at(s, i):
    l = list(s)
    del l[i]
    return ''.join(l)

for i in range(n):
    answer = 2
    s = input()
    r = is_palindrome(s)
    if r == True:
        answer = 0
    else:
        for j in range(len(s)):
            s2 = remove_at(s, j)
            r = is_palindrome(s2)
            if r == True:
                answer = 1
                break
    print(answer)
