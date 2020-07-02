import re
from itertools import starmap
import operator
from functools import reduce
from operator import itemgetter


def solution1(args):
    return list(map(lambda s: int(''.join(re.findall(r'\d+', s))[::-1]), args))

def solution2(args):
    return list(starmap(operator.mul, args)) 

def solution3(args):
    return list(filter(lambda x: x % 6 == 0 or x % 6 == 2 or x % 6 == 5, args))
    
def solution4(args):
    return list(filter(lambda x: bool(x) is True, args))

def solution5(args):
    return list(map(lambda x: operator.setitem(x, 'square', x['width'] * x['length']), args))

def solution6(args):
    return list(map(lambda x: \
                    list(map(lambda y: operator.setitem(y, 'square', x['width'] * x['length']) or y, [dict(x)] ))[0], \
                    args))

def solution7(args):
    return reduce(lambda x, y: x.intersection(y), args)

def solution8(args):
    return list(map(lambda d: reduce(lambda x, y: operator.setitem(d, y, args.count(y)) or d, args, None), [{}]))[0]

def solution9(args):
    return list(map(lambda student: student['name'], filter(lambda x: itemgetter('gpa')(x) > 4.5, args)))    

def solution10(args):
    return list(filter(lambda x: sum(map(lambda y: int(y), x[0::2])) == sum(map(lambda y: int(y), x[1::2])), args))

solutions = {
    'solution1': solution1,
    'solution2': solution2,
    'solution3': solution3,
    'solution4': solution4,
    'solution5': solution5,
    'solution6': solution6,
    'solution7': solution7,
    'solution8': solution8,
    'solution9': solution9,
    'solution10': solution10,
}