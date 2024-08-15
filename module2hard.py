def password(n):
    result = ''
    for i in range(1, n + 1):
        for j in range(i + 1, n + 1):
            sum_ = i + j
            if n % sum_ == 0:
                result += str(i) + str(j)
    return result
a = 0
while a < 3 or a > 20:
    a = int(input('Введите число от 3 до 20: '))

password = password(a)
print(f'Пароль для числа {a}: {password}')
