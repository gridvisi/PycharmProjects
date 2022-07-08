#图书系统常用的高级函数技巧

id = [1, 2, 3, 4]
leaders = ['Elon Mask', 'Tim Cook', 'Bill Gates', 'Yang Zhou']
record = zip(id, leaders)
print(record)
# <zip object at 0x7f266a707d80>print(list(record))
# [(1, 'Elon Mask'), (2, 'Tim Cook'), (3, 'Bill Gates'), (4, 'Yang Zhou')]

id = [1, 2, 3, 4]
leaders = ['Elon Mask', 'Tim Cook', 'Bill Gates', 'Yang Zhou']
record = zip(id, leaders)
print(record)
# <zip object at 0x7f266a707d80>print(list(record))# [(1, 'Elon Mask'), (2, 'Tim Cook'), (3, 'Bill Gates'), (4, 'Yang Zhou')]
id = [1, 2, 3, 4]
record = zip(id)
print(list(record))# [(1,), (2,), (3,), (4,)]


from itertools import zip_longest
id = [1, 2]
leaders = ['Elon Mask', 'Tim Cook', 'Bill Gates', 'Yang Zhou']
long_record = zip_longest(id, leaders)
print(list(long_record))
# [(1, 'Elon Mask'), (2, 'Tim Cook'), (None, 'Bill Gates'), (None, 'Yang Zhou')]
# long_record_2 = zip_longest(id, leaders, fillvalue='Top')print(list(long_record_2))
# [(1, 'Elon Mask'), (2, 'Tim Cook'), ('Top', 'Bill Gates'), ('Top', 'Yang Zhou')]

record = [(1, 'Elon Mask'), (2, 'Tim Cook'), (3, 'Bill Gates'), (4, 'Yang Zhou')]
id, leaders = zip(*record)
print(id)# (1, 2, 3, 4)
# print(leaders)# ('Elon Mask', 'Tim Cook', 'Bill Gates', 'Yang Zhou')

record = [(1, 'Elon Mask'), (2, 'Tim Cook'), (3, 'Bill Gates'), (4, 'Yang Zhou')]
print(*record) # unpack the list by one asterisk# (1, 'Elon Mask') (2, 'Tim Cook') (3, 'Bill Gates') (4, 'Yang Zhou')id, leaders = zip((1, 'Elon Mask'), (2, 'Tim Cook'), (3, 'Bill Gates'), (4, 'Yang Zhou'))print(id)# (1, 2, 3, 4)print(leaders)# ('Elon Mask', 'Tim Cook', 'Bill Gates', 'Yang Zhou')

id = [1, 2, 3, 4]
leaders = ['Elon Mask', 'Tim Cook', 'Bill Gates', 'Yang Zhou']
# create dict by dict comprehensionleader_dict = {i: name for i, name in zip(id, leaders)}print(leader_dict)# {1: 'Elon Mask', 2: 'Tim Cook', 3: 'Bill Gates', 4: 'Yang Zhou'}# create dict by dict functionleader_dict_2 = dict(zip(id, leaders))print(leader_dict_2)# {1: 'Elon Mask', 2: 'Tim Cook', 3: 'Bill Gates', 4: 'Yang Zhou'}# updateother_id = [5, 6]other_leaders = ['Larry Page', 'Sergey Brin']leader_dict.update(zip(other_id, other_leaders))print(leader_dict)# {1: 'Elon Mask', 2: 'Tim Cook', 3: 'Bill Gates', 4: 'Yang Zhou', 5: 'Larry Page', 6: 'Sergey Brin'}

products = ["cherry", "strawberry", "banana"]
price = [2.5, 3, 5]
cost = [1, 1.5, 2]
for prod, p, c in zip(products, price, cost):
    print(f'The profit of a box of {prod} is £{p-c}!')
    # The profit of a box of cherry is £1.5!# The profit of a box of strawberry is £1.5!# The profit of a box of banana is £3!

matrix = [[1, 2, 3], [1, 2, 3]]
matrix_T = [list(i) for i in zip(*matrix)]
print(matrix_T)# [[1, 1], [2, 2], [3, 3]]