money = int(input('сколько денег потратишь (в рублях): '))
m = 0.22  # копейки = 1 голде = 400 серебра
gold = money / m
expdiscount = round(gold) * 35  # discount exp
exp = round(gold) * 25  # обычный обмен exp
print(round(gold), 'золотых будет')
print("Хватит на свободный опыт  =", round(exp), "опыта")
print("Хватит на свободный опыт со скидкой =", round(expdiscount), "опыта")
silver = 400*round(gold)
print('Хватит на', round(silver), "серебра")
bon = int(input('Если хочешь посчитать имущество то введи кол-во бон: '))
s = int(input("кол-во серебра: "))
g = int(input("кол-во золота: "))
is6 = 8000/2398  # 3.33 бона к 1 рублю
stg = 8000/1980  # 4 бона к 1 рублю
summa1 = bon * is6
summa2 = bon * stg
sr = (summa1+summa2)/2  # среднее по бонам
s1 = (s * m) / 400  # silver
g1 = g * m  # gold
print(round(sr))
print(s1)
print(g1)
print("Среднее кол-во реальных денег на аккаунте по сумме всей валюты: ", round(sr)+s1+g1, "рублей")
