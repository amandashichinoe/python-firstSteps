first_string = 'A literal string'
second_string = "A literal string"
print(second_string == first_string)

print('-------------')

third_string = 'A single quoted literal string with a " double quote'
fourth_string = "A double quoted literal string with a ' single quote"
print(third_string)
print(fourth_string)

print('-------------')

fifth_string = 'A single quoted literal string with an \' escaped single quote'
sixth_string = "A double quoted literal string with a \" escaped double quote"
seventh_string = 'A literal string with a \n new line character'
eighth_string = 'A literal string with a \t tab character'

print(fifth_string)
print(sixth_string)
print(seventh_string)
print(eighth_string)

print('-------------')

ninth_string = r"A literal string with a \n new line character printed raw"

print(ninth_string)

print('-------------')

tenth_string = '''A literal string
on more than one line
sometimes known as a verbatim string.'''

eleventh_string = """Another literal string
     on more than one line
using double quotes."""

print(tenth_string)
print(eleventh_string)

print('-------------')

first = 'Conrad'
second = 'Grant'
third = 'Bob'
print(first, second)
print(first, second, third)
print(first, second, third, sep='-')
print(first, second, third, sep='-', end='.')

