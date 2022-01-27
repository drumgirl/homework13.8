a = int(input('Введите количество билетов:'))
price = []
for i in range(1, a+1):
    age = int(input(f"Возраст {i} участника? "))
    if age < 18:
        price.append(0)
    elif 18 < age < 25:
        price.append(990)
    elif age > 25:
        price.append(1390)
if a > 3 :
    s = int(sum(price) - (sum(price) * 0.1))
    print("Сумма вашей покупки со скидкой равна: ", s)
else:
    s = sum(price)
print("Сумма вашей покупки равна: ", s)