import string

ALPHANUM = string.letters + string.digits
def int_to_base62(i):
    index = i - 1
    if index == 0:
        return ALPHANUM[0]
    
    base62 = []
    while index > 0:
        base62.append(ALPHANUM[index % 62])
        index /= 62
        base62.reverse()
    return ''.join(base62)

def base62_to_int(s):
    power = len(s) - 1
    num = 1
    for char in s:
        num += ALPHANUM.index(char) * (62 ** power)
        power -= 1
    return num
