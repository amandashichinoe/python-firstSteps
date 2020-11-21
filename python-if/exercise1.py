#if, elif, else
value = '8'

if value == '7':
    print('The value is 7')
elif value == '8':
    print('The value is 8')
elif value == '9':
    print('The value is 9')
else:
    print('The value is not one we''re looking for')

print('-------------')


#blocos de código if aninhados
first_value = True
second_value = '6'

if first_value:
    if second_value == '6':
        print('Got here!')

print('-------------')