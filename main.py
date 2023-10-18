# 1
'''
def de_none(list):
    new_list = []

    for i in list:
        if i != None:
            new_list.append(i)

    return new_list

lst = [None, None, 1, [], (), {}, None]

print(de_none(lst))
'''
# 2
'''
def list_insert(list_, start_, num_, rep_):
    for i in range(rep_):
        list_.insert(start_, num_)
    return list_

list = [1, 2, 3, 4, 5]
start = int(input('Введите индекс от которого добавить элемент: '))
num = int(input('Введите значение, которое нужно добавить: '))
rep = int(input('Введите количество повторений: '))

print(list_insert(list, start, num, rep))
'''

# 3
'''
def get_elem(d_,k_):
    for i in d_:
        if i == k_:
            return d_.get(i)


d = {'a': 1, 'b': None, 'c': [1, 2]}
k = 'a'

print(get_elem(d,k))
'''