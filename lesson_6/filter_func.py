names = ('name_1', 'Yan', 'Yana', 'Dima', 'some_name')


def len_higher_4(x):
    if len(x) > 4:
        return x


def len_4_and_lower(y):
    if len(y) < 4:
        return y


res_1 = tuple(filter(len_higher_4, names))
res_2 = tuple(filter(len_4_and_lower, names))

print(res_1)
print(res_2)
