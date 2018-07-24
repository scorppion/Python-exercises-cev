v = input('Digite um valor: ')

print('{} é do tipo'.format(v), type(v))

print('{} é uma letra?'.format(v), v.isalpha())

print('{} é um número?'.format(v), v.isnumeric())

print('{} é um decimal?'.format(v), v.isdecimal())

print('{} é um digito?'.format(v), v.isdigit())

print('{} é um printavel?'.format(v), v.isprintable())