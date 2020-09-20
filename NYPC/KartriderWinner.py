import pdb
playerCount = int(input())
photoCount = int(input())
photos = list(map(int, input().split()))
answer = {photos[0]}

def find_sub(begin, end):
    temp = photos[begin:end]
    #pdb.set_trace()
    for i in temp:
        #pdb.set_trace()
        if temp.count(i) > 1:
            if i != photos[begin]:
                return False
    return True

for i in range(1, photoCount - 1):
    e = i + 1
    #pdb.set_trace()
    if photos[i] in answer:
        continue
    else:
        while e < photoCount:
            #pdb.set_trace()
            if photos[i] == photos[e]:
                if e - i > 1:
                    if find_sub(i, e):
                        answer.add(photos[i])
                    break
                else:
                    answer.add(photos[i])
                    break
            else:
                e += 1

print(' '.join(list(map(str, answer))))
