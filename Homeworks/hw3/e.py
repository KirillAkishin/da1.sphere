def brackets(n):
    file_name = 'hardcode.txt'
    with open(file_name, 'w') as f:
        def bb(n, opened=0, closed=0, res=''):
            if opened + closed == 2 * n:
                f.write(res + '\n')
            if opened < n:
                bb(n, opened + 1, closed, res + '(')
            if opened > closed:
                bb(n, opened, closed + 1, res + ')')
        bb(n)
    with open(file_name, 'r') as f:
        for line in f:
            yield line[:-1]


if __name__ == "__main__":
    n = input()
    n = int(n)
    for i in brackets(n):
        print(i)