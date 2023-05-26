# Задача 1.2.

# Пункт A. 
# Приведем плейлист песен в виде списка списков
# Список my_favorite_songs содержит список названий и длительности каждого трека
# Выведите общее время звучания трех случайных песен в формате
# Три песни звучат ХХХ минут

my_favorite_songs = [
    ['Waste a Moment', 3.03],
    ['New Salvation', 4.02],
    ['Staying\' Alive', 3.40],
    ['Out of Touch', 3.03],
    ['A Sorta Fairytale', 5.28],
    ['Easy', 4.15],
    ['Beautiful Day', 4.04],
    ['Nowhere to Run', 2.58],
    ['In This World', 4.02],
]
import random
list_01 = [my_favorite_songs[0][1], 
        my_favorite_songs[1][1], 
        my_favorite_songs[2][1],
        my_favorite_songs[3][1],
        my_favorite_songs[4][1],
        my_favorite_songs[5][1],
        my_favorite_songs[6][1],
        my_favorite_songs[7][1],
        my_favorite_songs[8][1]]
k = 3
y = []
total = 0
while k !=0:
    x =  random.choice(list_01)
    k -= 1
    y.append(x)
print ("Три песни звучат", sum(y), "минут")
#ДОП.Решение пункта С (если правильно понял задание)
import random
list_01 = [my_favorite_songs[0][0], 
        my_favorite_songs[1][0], 
        my_favorite_songs[2][0],
        my_favorite_songs[3][0],
        my_favorite_songs[4][0],
        my_favorite_songs[5][0],
        my_favorite_songs[6][0],
        my_favorite_songs[7][0],
        my_favorite_songs[8][0]]
generation = 3
spisok = []
total = 0
while generation !=0:
    xq =  random.choice(list_01)
    generation -= 1
    spisok.append(xq)
print ("Решение пункта С для А", spisok)


# Пункт B. 
# Есть словарь песен 
# Распечатайте общее время звучания трех случайных песен
# Вывод: Три песни звучат ХХХ минут.

my_favorite_songs_dict = {
    'Waste a Moment': 3.03,
    'New Salvation': 4.02,
    'Staying\' Alive': 3.40,
    'Out of Touch': 3.03,
    'A Sorta Fairytale': 5.28,
    'Easy': 4.15,
    'Beautiful Day': 4.04,
    'Nowhere to Run': 2.58,
    'In This World': 4.02,
}
#Решение
import random
Q = 3
T = []
total = 0
while Q !=0:
    E =  random.choice (list(my_favorite_songs_dict.values()))
    Q -= 1
    T.append(E)
print ("Три песни звучат", sum(T), "минут")
#ДОП.Решение пункта С (если правильно понял задание)
import random
H = 3
F = []
total = 0
while H !=0:
    S =  random.choice (list(my_favorite_songs_dict.keys()))
    H -= 1
    F.append(S)
print ("Решение пункта С для задания В", F)

# Дополнительно для пунктов A и B
# Пункт C.
# Сгенерируйте случайные песни с помощью модуля random
# import random

# Дополнительно 
# Пункт D.
# Переведите минуты и секунды в формат времени. Используйте модуль datetime 
