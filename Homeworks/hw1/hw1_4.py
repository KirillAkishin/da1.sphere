# Дан массив a1,...,an из n натуральных чисел.
# Требуется отсортировать числа в массиве в порядке возрастания суммы цифр, 
# а при равной сумме цифр — по возрастанию самого числа.

def reorder_list(input_v, cols):
    n = len(input_v)
    v = input_v.copy()
    k = n // cols
    c = n % cols
    i = 0
    if k == 0:
        for column in range(0, n):
            v[column] = input_v[column]
        return v
    for column in range(0, cols):
        for row in range(0, k):
            v[row*cols + column] = input_v[i]
            i += 1
        if c != 0:
            row += 1
            v[row*cols + column] = input_v[i]
            i += 1
            c -= 1
    return v

# def print_by_cols(v, cols):
#     for i in range(0, len(v), cols):
#         print(*v[i:i+cols], sep='\t')

# v = list(range(2, 124))
# cols = 13

# v_new = reorder_list(v, cols)

# print_by_cols(v, cols)
# print()
# print_by_cols(v_new, cols)  

