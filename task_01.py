# 1. Представлен список чисел. Необходимо вывести элементы исходного списка, значения которых больше
# предыдущего элемента. Use comprehension.
# in
# 9
#
# out
# [15, 16, 2, 3, 1, 7, 5, 4, 10]
# [16, 3, 7, 10]
#
# in
# 10
#
# out
# [28, 20, 10, 5, 1, 24, 7, 15, 23, 25]
# [24, 15, 23, 25]

from random import randint


def new_list(num=20):
    new_list = [randint(2, 100) for _ in range(num)]
    print(*f'Входящий список:\n{new_list}', sep='')
    return new_list


def out_list(in_list=new_list()):
    out_list = list(map(lambda x: x // 1, in_list))
    out_list = [in_list[i] for i in range(1, len(in_list)) if int(in_list[i - 1]) < int(in_list[i])]
    return out_list


print(*f'Исходящий список:\n{out_list()}', sep='')
