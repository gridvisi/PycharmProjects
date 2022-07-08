'''
100rmb，bonus = 每买 3 瓶可乐, 空瓶子换 1 瓶
100rmb，price = 3元一瓶

'''

def coco(rmb,p,bonus):
    #初始条件
    bottle = 0
    empty = 0 #
    while rmb > 0:
        rmb -= p
        bottle += 1
        empty += 1
        #积攒到3个空瓶时
        #变量表达购买到3的倍数时，手头空瓶的数量
        if empty == bonus:
            bottle += 1
            empty = 0
    return bottle,empty,rmb  #结束状态

rmb,p,bonus = 100,3,3
print(coco(rmb,p,bonus))
