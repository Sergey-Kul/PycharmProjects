educational_grant = float(input("Введите месячную стипендию: "))  # месячная стипуха
mes_plata = float(input("Введите месячный расход: "))  # расходы в месяц
expenses = mes_plata - educational_grant # оплата за 1 месяц идёт без %
print("Расход за %2d месяц - %8.2f руб" % (1, expenses))  # вывод 1 месяца
i = 0
while i < 9:
    i += 1
    procent = ((mes_plata / 100) * 3)
    expenses = mes_plata + procent - educational_grant
    mes_plata = mes_plata + procent # увеличиваем % расхода за каждый месяц
    print("Расход за %2d месяц - %8.2f руб" % (i+1, expenses))
