ru = 'абвгдежзийклмнопрстуфхцчшщъыьэюяабвгдежзийклмнопрстуфхцчшщъыьэюя'
encrypt = input('Введите сообщение: ')
key = int(input('Введите ключ (диапазон 1 - 25): '))
encrypt = encrypt.lower()
encrypted = ''
for letter in encrypt:
    posichion = ru.find(letter)
    newPosition = posichion + key
    if letter in ru:
        encrypted = encrypted + ru[newPosition]
    else:
        encrypted = encrypted + letter
print('Твой шифр:', encrypted)