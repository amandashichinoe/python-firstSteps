print('Simple calculator!')

first_number = input('First number? ')
operation = input('Operation? ')
second_number = input('Second number? ')

if first_number.isnumeric() == False or second_number.isnumeric() == False:
    print('Please input a number.')
    exit()

first_number = int(first_number)
second_number = int(second_number)

if operation == '+':
    result = first_number + second_number
    type_operation = 'sum'

elif operation == '-':
    result = first_number - second_number
    type_operation = 'difference'

elif operation == '*':
    result = first_number * second_number
    type_operation = 'product'

elif operation == '/':
    result = first_number / second_number
    type_operation = 'quotient'

elif operation == '**':
    result = first_number ** second_number
    type_operation = 'exponent'

elif operation == '%':
    result = first_number % second_number
    type_operation = 'modulus'

else:
    print('Operation not recognized.')
    exit()

print(type_operation + ' of ' + str(first_number) + ' ' + operation + ' ' + str(second_number) + ' equals ' + str(result))

