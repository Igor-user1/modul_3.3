def print_params(a=1, b='string', c=True):
    print(a, b, c)


print_params()

print_params(a=5, b='Tree')

print_params(b=25)

print_params(c=[1, 2, 3])

values_list = ['one', 2, False]

values_dict = {'a': 15, 'b': 'good', 'c': 1.6}

print_params(*values_list)

print_params(**values_dict)

values_list_2 = [13, 'yes']

print_params(*values_list_2, 42)
