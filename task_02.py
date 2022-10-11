# 2. Для чисел в пределах от 20 до N найти числа, кратные 20 или 21. Use comprehension.
# in
# 100
#
# out
# [20, 21, 40, 42, 60, 63, 80, 84, 100]
#
# in
# 424
#
# out
# [20, 21, 40, 42, 60, 63, 80, 84, 100, 105, 120, 126, 140, 147, 160, 168, 180, 189, 200, 210,
#  220, 231, 240, 252, 260, 273, 280, 294, 300, 315, 320, 336, 340, 357, 360, 378, 380, 399, 400, 420]

def new_list():
    num = int(input('Верхняя граница списка: '))
    n_l = [i for i in range(20, num+1)]
    return n_l


def out_list(in_list=new_list()):
    o_l = list(filter(lambda x: x % 20 == 0 or x % 21 == 0, in_list))
    return o_l


print(out_list())
