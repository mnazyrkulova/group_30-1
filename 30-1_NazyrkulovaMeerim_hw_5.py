import random
my_money = 1000

while True:
    number = int(input('Вы хотите поставить на? 1-apple, 2-limon,3-lime, 4-break:'))
    if number == 4:
        break
    bet = int(input('Ваша ставка:'))
    random_number = random.randint(1, 30)
    if my_money >= bet:
        if number == 3 and random_number == 10:
            print(f'Вы выиграли {bet * 2}$. !Хотите сыграть еще?')
            my_money += bet
        elif number == 1 and 1 == 22:
            print(f'Вы выиграли {bet * 2}$. Хотите сыграть еще?')
            my_money += bet
        elif number == 2  and 1 == 18:
            print(f'Вы выиграли {bet * 2}$. Хотите сыграть еще?')
            my_money += bet
        else:
            print(f'Вы проиграли {bet}$. Хотите сыграть еще? Если нет, нажмите 4')
            my_money -= bet
    else:
        print(f'У вас не достаточно денег. Вам не хватает {bet - my_money} $.')











