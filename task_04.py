# 4. * Функция принимает в качестве аргументов строки в формате «Имя Фамилия», возвращает словарь,
# ключи — первые буквы фамилий, значения — словари, реализованные по схеме предыдущего задания.
# in
# "Иван Сергеев", "Инна Серова", "Петр Алексеев",
# "Илья Иванов", "Анна Савельева", "Юнона Ветрякова",
# "Борис Аркадьев", "Антон Серов", "Павел Анисимов"
#
# out
#
# {'С': {'А': ['Анна Савельева', 'Антон Серов'], 'И': ['Иван Сергеев', 'Инна Серова']},
#  'А': {'Б': ['Борис Аркадьев'], 'П': ['Павел Анисимов', 'Петр Алексеев']}, 'И': {'И': ['Илья Иванов']},
#  'В': {'Ю': ['Юнона Ветрякова']}}

def list_words(staff=()):
    d_staff_first={}
    words = staff.split(',')
    print(words)
    for word_first in words:
        sim_first_name = word_first[(word_first.find(' ') + 1)]
        if d_staff_first.get(sim_first_name):
            d_staff_first[words[0]] = d_staff_first[words[0]] + (', ') + word_first
        d_staff_first[words[0]] = d_staff_first.setdefault(sim_first_name, word_first)

    return d_staff_first


print(list_words(str(input('Введите список:'))))
