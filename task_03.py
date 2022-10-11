# 3. Написать функцию, аргументы имена сотрудников, возвращает словарь, ключи — первые буквы имён,
# значения — списки, содержащие имена, начинающиеся с соответствующей буквы.
# in
# "Иван", "Мария", "Петр", "Илья", "Марина", "Петр", "Алина", "Бибочка"
#
# out
#
# {'А': ['Алина'], 'Б': ['Бибочка'], 'И': ['Иван', 'Илья'], 'М': ['Марина', 'Мария'], 'П': ['Петр', 'Петр']}

def list_staff(staff=["Иван", "Мария", "Петр", "Илья", "Марина", "Петр", "Алина", "Бибочка"], list_keys=[]):
    for i in range(len(staff)):
        s = str(staff[i])[0]
        list_keys.append(s)
    d_staff = dict(zip(list_keys, staff))
    return d_staff
    # d_staff = {}
    # for str in staff:
    #     for word in str.split():
    #         d_staff[word[0]] = d_staff.setdefault(word[0],word)
    #
    # return d_staff

print(list_staff())
