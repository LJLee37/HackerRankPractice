T = int(input())
for _ in range(T):
    aString = input()
    isPalindrome = 0
    lenAStr = len(aString)
    for i in range(lenAStr // 2):
        if aString[i] != aString[-1-i]:
            isPalindrome = 1
            break
    if isPalindrome == 0:
        print(0)
        continue
    for i in range(lenAStr):
        newString = ""
        isPalindrome = 1
        if i > 0 and i < lenAStr:
            newString = aString[:i-1] + aString[i+1:]
        elif i == 0:
            newString = aString[1:]
        else:
            newString = aString[:lenAStr - 1]
        for j in range(lenAStr // 2):
            if newString[j] != newString[-1-j]:
                isPalindrome = 2
                break
        if isPalindrome == 1:
            print(1)
            break
    if isPalindrome == 2:
        print(2)
