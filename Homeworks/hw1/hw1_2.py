# Дан массив a1,...,an из n натуральных чисел.
# Требуется отсортировать числа в массиве в порядке возрастания суммы цифр, а при равной сумме цифр — по возрастанию самого числа.

n = int(input())
l = list(map(int, input().split()))[:n]

def sort_func(item):
    return (item//10) + (item%10), item


print(*sorted(l, key=sort_func), sep = " ") 