def merge_the_tools(string, k):
    # your code goes here
    n = len(string)
    strlist =[]
    for i in range(0, n, n//k):
        tempstr = string[i:i + n//k]
        inTheList = []
        for j in tempstr:
            if not j in inTheList:
                inTheList.append(j)
        strlist.append(''.join(inTheList))
    for i in strlist:
        print(i)
    

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)