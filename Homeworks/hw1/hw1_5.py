# Загадано натуральное число x от 1 до 100000 (оба числа включены). 
# Вам нужно написать программу, отгадывающую это число.
# 
# Программа может задавать вопросы вида «Верно ли, что x < a» для различных a, 
# но ответы на эти вопросы она получает не сразу.

# Вопросы задаются раундами — в одном раунде можно задать произвольное количество вопросов 
# и по окончании раунда получить ответы на все эти вопросы.

# За каждый вопрос нужно заплатить 1 монету, за каждый раунд 10 монет. 
# Нужно привести алгоритм, который отгадает число x, заплатив не больше чем 100 монет.

import sys

def safe_input(): 
    try:
        return input()
    except EOFError:
        sys.exit(0)

def series_of_questions(step,start_point, n):
    for i in range(1, n+1):
        print("? {}".format(int(start_point + step*i)))

def series_of_answers(n):
    # list_of_answers = []
    count = 0
    for i in range(1, n+1):
        answer = safe_input().split()
        # list_of_answers.append(int(answer[0]))
        count += int(answer[0])
    return count

rounds = 5
questions_in_round = 9
start_point = 0
end_point = 100_000
step = int((end_point-start_point) // (questions_in_round+1))

for r in range(1, rounds+1):
    series_of_questions(step, start_point, questions_in_round)
    if start_point == 99_990:
        print("? {}".format(100_000))

    print("+")
    count = series_of_answers(questions_in_round)
    if (start_point == 99_990) and (int(safe_input().split()[0]) == 0):
        start_point += 1

    start_point += (questions_in_round-count) * step
    end_point = start_point + step
    step = (end_point-start_point) // (questions_in_round+1)
    
print("! {}".format(start_point))