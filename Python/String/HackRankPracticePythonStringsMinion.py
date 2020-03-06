def minion_game(string):
    # your code goes here
    score = [0,0]#0: Stuart, 1: Kevin
    VOWEL = ['A', 'E', 'I', 'O', 'U']
    for i in range(len(string)):
        temp = string[i]
        if temp in VOWEL:
            score[1] += len(string) - i
        else:
            score[0] += len(string) - i
    if score[0] > score[1]:
        print("Stuart", score[0])
    elif score[0] < score[1]:
        print("Kevin", score[1])
    else:
        print("Draw")

if __name__ == '__main__':
    s = input()
    minion_game(s)