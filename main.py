# name = input('Введите имя: ')
# if name == 'Valera':
#    print('Здравствуйте, администратор')
# if name == 'иди на хуй':
#    print('Отсоси!')
# else:
#    print('Привет,', name)

number = int(input('Введите число: '))
if number % 3 ==0 and number % 5 == 0:
    print('FizzBuzz')
elif number % 3 == 0:
    print('Fizz')
elif number % 5 == 0:
    print('Buzz')
else:
    print('иди на хуй')

