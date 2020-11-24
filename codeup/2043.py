instr = input()
"""있어도 되고 없어도 됨.
removes = ['a', 'e', 'h', 'i', 'o', 'u', 'w', 'y']
for i in removes:
    instr.replace(i, '')
    """
retval = [instr[0]]
before = ''
scores = [['b', 'f', 'p', 'v'], ['c', 'g', 'j', 'k', 'q', 's', 'x', 'z'], ['d', 't'], ['l'], ['m', 'n'], ['r']]
for i in instr[1:]:
    if len(retval) == 4:
        break
    if i == before:
        continue
    before = i
    for j in range(6):
        if i in scores[j]:
            retval.append(str(j + 1))
            break
while(len(retval) < 4):
    retval.append('0')
print(''.join(retval))
