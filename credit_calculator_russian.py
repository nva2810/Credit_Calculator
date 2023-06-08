import math

print('Добро пожаловать в кредитный калькулятор!')


def choice():
    while True:
        payment_type = input('''\nПожалуйста, укажите ваш тип оплаты.
Если это аннуитетный платеж, введите "анн",
если это дифференцированный платеж, введите "дифф",
если хотите выйти из программы, введите "выход": ''')
        while payment_type != 'дифф' and payment_type != 'анн' and payment_type != 'выход':
            print('\nНеверные данные. Пожалуйста, попробуйте еще раз.')
            payment_type = input('Пожалуйста, укажите ваш тип оплаты: ')
        if payment_type == 'дифф':
            diff()
        elif payment_type == 'анн':
            ann()
        elif payment_type == 'выход':
            print('\nУдачи!')
            print(input('\nНажмите Enter, чтобы закончить...'))
            break


def diff():
    principal = float(input('\nВведите основную сумму кредита: '))
    periods = int(input('Введите количество месяцев оплаты: '))
    interest = float(input('Введите процентную ставку по кредиту: ')) / 1200
    overpayment = 0
    while principal <= 0 or periods <= 0 or interest <= 0:
        print('\nНеверные данные. Пожалуйста, попробуйте еще раз.')
        principal = float(input('\nВведите основную сумму кредита: '))
        periods = int(input('Введите количество месяцев оплаты: '))
        interest = float(input('Введите процентную ставку по кредиту: ')) / 1200
    for m in range(1, periods + 1):
        diff_payment = math.ceil(principal / periods + interest *
                                 (principal - (principal * (m - 1) / periods)))
        print(f'Месяц {m}-ый: оплата составляет {diff_payment}.')
        overpayment += diff_payment
    print(f'\nПереплата = {overpayment - int(principal)}.')


def ann():
    user_type = input('''\nЧто именно вы хотите рассчитать?
Введите "п" для количества ежемесячных платежей,
введите "e" для суммы ежемесячного платежа,
введите "к" для основного долга по кредиту: ''')
    while user_type != 'п' and user_type != 'е' and user_type != 'к':
        print('\nНеверные данные. Пожалуйста, попробуйте еще раз.')
        user_type = input('''Введите "п" для количества ежемесячных платежей,
введите "e" для суммы ежемесячного платежа,
введите "к" для основного долга по кредиту: ''')
    if user_type == 'п':
        principal = float(input('\nВведите основную сумму кредита: '))
        payment = float(input('Введите ежемесячный платеж: '))
        interest = float(input('Введите процентную ставку по кредиту: ')) / 1200
        while principal <= 0 or payment <= 0 or interest <= 0:
            print('\nНеверные данные. Пожалуйста, попробуйте еще раз.')
            principal = float(input('\nВведите основную сумму кредита: '))
            payment = float(input('Введите ежемесячный платеж: '))
            interest = float(input('Введите процентную ставку по кредиту: ')) / 1200
        periods = math.ceil(math.log(payment / (payment - interest * principal),
                                     1 + interest))
        years = periods // 12
        months = periods % 12
        if years == 0:
            if months == 1:
                print(f'\nНа погашение этого кредита уйдет 1 месяц!')
            elif 1 < months < 5:
                print(f'\nНа погашение этого кредита уйдет {months} месяца!')
            else:
                print(f'\nНа погашение этого кредита уйдет {months} месяцев!')
        elif months == 0:
            if years == 1:
                print(f'\nНа погашение этого кредита уйдет 1 год!')
            elif 1 < years < 5 or 20 < years < 25:
                print(f'\nНа погашение этого кредита уйдет {years} года!')
            else:
                print(f'\nНа погашение этого кредита уйдет {years} лет!')
        elif years == 1:
            if months == 1:
                print(f'\nНа погашение этого кредита уйдет 1 год и 1 месяц!')
            elif 1 < months < 5:
                print(f'\nНа погашение этого кредита уйдет 1 год и {months} месяца!')
            else:
                print(f'\nНа погашение этого кредита уйдет 1 год и {months} месяцев!')
        elif 1 < years < 5 or 20 < years < 25:
            if months == 1:
                print(f'\nНа погашение этого кредита уйдет {years} года и 1 месяц!')
            elif 1 < months < 5:
                print(f'\nНа погашение этого кредита уйдет {years} года и {months} месяца!')
            else:
                print(f'\nНа погашение этого кредита уйдет {years} года и {months} месяцев!')
        else:
            if months == 1:
                print(f'\nНа погашение этого кредита уйдет {years} лет и 1 месяц!')
            elif 1 < months < 5:
                print(f'\nНа погашение этого кредита уйдет {years} лет и {months} месяца!')
            else:
                print(f'\nНа погашение этого кредита уйдет {years} лет и {months} месяцев!')
        overpayment = int(payment * periods - principal)
        print(f'Переплата = {overpayment}.')
    if user_type == 'е':
        principal = float(input('\nВведите основную сумму кредита: '))
        periods = int(input('Введите количество месяцев оплаты: '))
        interest = float(input('Введите процентную ставку по кредиту: ')) / 1200
        while principal <= 0 or periods <= 0 or interest <= 0:
            print('\nНеверные данные. Пожалуйста, попробуйте еще раз.')
            principal = float(input('\nВведите основную сумму кредита: '))
            periods = int(input('Введите количество месяцев оплаты: '))
            interest = float(input('Введите процентную ставку по кредиту: ')) / 1200
        payment = math.ceil(principal * ((interest * (pow(1 + interest, periods))) /
                                         (pow(1 + interest, periods) - 1)))
        print(f'\nВаш ежемесячный аннуитетный платеж = {payment}!')
        overpayment = int(payment * periods - principal)
        print(f'Переплата = {overpayment}')
    if user_type == 'к':
        payment = float(input('\nВведите ежемесячный платеж: '))
        periods = int(input('Введите количество месяцев оплаты: '))
        interest = float(input('Введите процентную ставку по кредиту: ')) / 1200
        while payment <= 0 or periods <= 0 or interest <= 0:
            print('\nНеверные данные. Пожалуйста, попробуйте еще раз.')
            payment = float(input('\nВведите ежемесячный платеж: '))
            periods = int(input('Введите количество месяцев оплаты: '))
            interest = float(input('Введите процентную ставку по кредиту: ')) / 1200
        principal = int((payment / ((interest * pow(1 + interest, periods)) /
                                    (pow(1 + interest, periods) - 1))))
        print(f'\nВаша основная сумма кредита = {principal}!')
        overpayment = int(periods * payment - principal)
        print(f'Переплата = {overpayment}.')


choice()
