import random 


def get_symbols(answers, all_symbols):
    symbols = ''
    for i in range(len(answers)):
        if answers[i].lower() == 'д':
            symbols += all_symbols[i]
    return symbols


def get_pass(symbols):
    n = random.choice(symbols)
    password = []
    for _ in range(count):
        chars = ''
        i = 0
        while i < langht:
            n = random.choice(symbols)
            if exclude == 'н':
                chars += n
                i += 1
            else:
                if n in 'il1Lo0O':
                    continue
                else:
                    chars += n
                    i += 1
        password.append(chars)
    return password


count = int(input('Ведите количество генерируемых паролей:  '))
langht = int(input('Введите длину одного пароля:  '))
add_digits = input('Включать ли цифры 0123456789? (д / н):  ')
add_upper = input(
    'Включать ли прописные буквы ABCDEFGHIJKLMNOPQRSTUVWXYZ? (д / н):  ')
add_lower = input(
    'Включать ли строчные буквы abcdefghijklmnopqrstuvwxyz? (д / н):  ')
add_punctuation = input('Включать ли символы !#$%&*+-=?@^_? (д / н):  ')
exclude = input('Исключать ли неоднозначные символы il1Lo0O? (д / н):  ')
answers = add_digits + add_upper + add_lower + add_punctuation
all_symbols = [
    '0123456789', 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz',
    '!#$%&*+-=?@^_.'
]

print('Ваши сгенерированные пароли:', sep='\n')
print(*get_pass(get_symbols(answers, all_symbols)), sep='\n')