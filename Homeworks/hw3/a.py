def solution1(args):
    return [c * 4 for c in args] 

def solution2(args):
    return [c * i for i, c in enumerate(args, 1)] 

def solution3(args):
    return [d for d in args if d % 3 == 0 or d % 5 == 0] 

def solution4(args):
    return [e for l in args for e in l] 

def solution5(args):
    return [
        (a, b, c) \
        for c in range(1, args+1) for b in range(1, c+1) for a in range(1, b+1) \
        if c**2 == b**2 + a**2] 
            
def solution6(args):
    return [[i + j for i in args[1]] for j in args[0]]

def solution7(args):
    return [[a[i] for a in args] for i in range(len(args[0]))]

def solution8(args):
    return [list(map(int, s.split(' '))) for s in args]

def solution9(args):
    return {chr(v+97): v**2 for v in args}

def solution10(args):
    return {(name[0].upper() + name[1:].lower()) for name in args if len(name) > 3}

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