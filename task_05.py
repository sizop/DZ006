# 5. ** Реализовать функцию, возвращающую n шуток, сформированных из трех случайных слов, взятых из трёх
# списков (по одному из каждого)
# nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
# adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью", "когда-то", "где-то"]
# adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
#
# in
# 10 True
#
# out
#
# ['дом ночью мягкий', 'огонь завтра зеленый', 'лес вчера яркий', 'автомобиль сегодня веселый',
#  'город позавчера утопичный']
#
# in
# 10 False
#
# out
#
# ['автомобиль ночью мягкий', 'огонь вчера веселый', 'автомобиль позавчера веселый', 'город вчера утопичный',
#  'лес сегодня зеленый', 'дом вчера яркий', 'автомобиль вчера зеленый', 'огонь позавчера яркий',
#  'огонь где-то утопичный', 'автомобиль где-то мягкий']

from random import choice


def joke(num, list_1, list_2, list_3):
    return [(choice(list_1) + (' ') + choice(list_2) + (' ') + choice(list_3)) for _ in range(num)]


nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью", "когда-то", "где-то"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]

print(joke(int(input('Количество:')), nouns, adverbs, adjectives))
