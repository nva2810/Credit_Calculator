import math

print('Welcome to the credit calculator!')


def choice():
    while True:
        payment_type = input('''\nPlease specify your payment type.
If this is an annuity payment, enter "ann",
if this is a differentiated payment, enter "diff",
if you want to exit the program, enter "exit": ''')
        while payment_type != 'diff' and payment_type != 'ann' and payment_type != 'exit':
            print('\nIncorrect data. Please try again.')
            payment_type = input('Please specify your payment type: ')
        if payment_type == 'diff':
            diff()
        elif payment_type == 'ann':
            ann()
        elif payment_type == 'exit':
            print('\nGood Luck!')
            print(input('\nPress Enter to finish...'))
            break


def diff():
    principal = float(input('\nEnter the principal amount of the loan: '))
    periods = int(input('Enter the number of months of payment: '))
    interest = float(input('Enter the loan interest rate: ')) / 1200
    overpayment = 0
    while principal <= 0 or periods <= 0 or interest <= 0:
        print('\nIncorrect data. Please try again.')
        principal = float(input('Enter the principal amount of the loan: '))
        periods = int(input('Enter the number of months of payment: '))
        interest = float(input('Enter the loan interest rate: ')) / 1200
    for m in range(1, periods + 1):
        diff_payment = math.ceil(principal / periods + interest *
                                 (principal - (principal * (m - 1) / periods)))
        print(f'Month {m}: payment is {diff_payment}.')
        overpayment += diff_payment
    print(f'\nOverpayment = {overpayment - int(principal)}.')


def ann():
    user_type = input('''\nWhat exactly do you want to calculate?
Type "n" for number of monthly payments,
type "a" for annuity monthly payment amount,
type "p" for loan principal: ''')
    while user_type != 'n' and user_type != 'a' and user_type != 'p':
        print('\nIncorrect data. Please try again.')
        user_type = input('''Type "n" for number of monthly payments,
type "a" for annuity monthly payment amount,
type "p" for loan principal: ''')
    if user_type == 'n':
        principal = float(input('\nEnter the principal amount of the loan: '))
        payment = float(input('Enter the monthly payment: '))
        interest = float(input('Enter the loan interest rate: ')) / 1200
        while principal <= 0 or payment <= 0 or interest <= 0:
            print('\nIncorrect data. Please try again.')
            principal = float(input('Enter the principal amount of the loan: '))
            payment = float(input('Enter the monthly payment: '))
            interest = float(input('Enter the loan interest rate: ')) / 1200
        periods = math.ceil(math.log(payment / (payment - interest * principal),
                                     1 + interest))
        years = periods // 12
        months = periods % 12
        if years == 0:
            print(f'\nIt will take {months} months to repay this loan!')
        elif months == 0:
            if years == 1:
                print(f'\nIt will take {years} year to repay this loan!')
            else:
                print(f'\nIt will take {years} years to repay this loan!')
        else:
            print(f'\nIt will take {years} years and {months} months to repay this loan!')
        overpayment = int(payment * periods - principal)
        print(f'Overpayment = {overpayment}.')
    if user_type == 'a':
        principal = float(input('\nEnter the principal amount of the loan: '))
        periods = int(input('Enter the number of months of payment: '))
        interest = float(input('Enter the loan interest rate: ')) / 1200
        while principal <= 0 or periods <= 0 or interest <= 0:
            print('\nIncorrect data. Please try again.')
            principal = float(input('\nEnter the principal amount of the loan: '))
            periods = int(input('Enter the number of months of payment: '))
            interest = float(input('Enter the loan interest rate: ')) / 1200
        payment = math.ceil(principal * ((interest * (pow(1 + interest, periods))) /
                                         (pow(1 + interest, periods) - 1)))
        print(f'\nYour annuity payment = {payment}!')
        overpayment = int(payment * periods - principal)
        print(f'Overpayment = {overpayment}')
    if user_type == 'p':
        payment = float(input('\nEnter the monthly payment: '))
        periods = int(input('Enter the number of months of payment: '))
        interest = float(input('Enter the loan interest rate: ')) / 1200
        while payment <= 0 or periods <= 0 or interest <= 0:
            print('\nIncorrect data. Please try again.')
            payment = float(input('\nEnter the monthly payment: '))
            periods = int(input('Enter the number of months of payment: '))
            interest = float(input('Enter the loan interest rate: ')) / 1200
        principal = int((payment / ((interest * pow(1 + interest, periods)) /
                                    (pow(1 + interest, periods) - 1))))
        print(f'\nYour loan principal = {principal}!')
        overpayment = int(periods * payment - principal)
        print(f'Overpayment = {overpayment}.')


choice()
