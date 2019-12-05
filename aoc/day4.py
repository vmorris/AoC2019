from collections import defaultdict
import sys


def is_increasing(password):
    p_digits = list(map(int, list(password)))
    p_sorted = sorted(p_digits)
    return p_digits == p_sorted        


def has_double(password):
    d = defaultdict(list)
    c = password[0]
    d[c].append(1)
    for _c in password[1:]:
        if c == _c:
            d[_c][-1] += 1
        else:
            d[_c].append(1)
        c = _c
    for d in d.values():
        if 2 in d:
            return True
    return False
            
        
    '''
    try:
        for i in range(len(password)):
            if password[i] == password[i+1]:
                return True
    except IndexError:
        return False
    '''

if __name__ == '__main__':
    with open(sys.argv[1], 'r') as f:
        data = f.read().rstrip()
        
    r = data.split('-')
    
    values = range(int(r[0]), int(r[1]))

    tally = 0
    for v in values:
        if is_increasing(str(v)) \
            and has_double(str(v)):
                tally += 1
            
    print(tally)

    