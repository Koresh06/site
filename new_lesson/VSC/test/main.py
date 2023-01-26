from random import *

print('Добро пожаловать в числовую угадайку')


def is_valid(num):
    if num.isdigit():
        return 1 <= int(num) <= 100
    else:
        return False


def max_value():
    num = input('Введи максимальное значение\n')
    while is_valid(num) == False:
        print('А может быть все-таки введем целое число?')
    return int(num)


def new_game():
    print('Еще разок???\nда/нет')
    if input() == 'да':
        is_valid_num()
    else:
        print('Жаль, до новых встреч')


def is_valid_num():
    counter = 0
    max_value1 = max_value()
    random_num = randint(1, max_value1)
    while True:
        player_num = input(f'Вводите ваше число от 1 до {max_value1}\n')
        if is_valid(player_num) == False:
            print(
                f'А может быть все-таки введем целое число от 1 до {max_value1}?'
            )
            continue
        player_num = int(player_num)
        if random_num > player_num:
            print('Ваше число меньше загаданного, попробуйте еще разок')
            counter += 1
            continue
        elif random_num < player_num:
            print('Ваше число больше загаданного, попробуйте еще разок')
            counter += 1
            continue
        elif random_num == player_num:
            print(f'Вы угадали за {counter} раз, поздравляем!')
            print('Спасибо, что играли в числовую угадайку. Еще увидимся...')
            new_game()
            break


is_valid_num()