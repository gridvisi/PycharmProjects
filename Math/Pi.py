
'''
John Wallis 在 1656 年发表了他的 π 乘积：偶数平方除以两个相邻奇数的无限乘积。
令人惊讶的是，科学家们在氢原子能态的量子力学公式中发现了它
'''

import math

def johnWallis(n):
    p = 1
    for i in range(1,n):
        p *= ((2*i)**2) / ((2*i-1)*(2*i+1))
    return 2*p
n = 100
print(johnWallis(n))


# smile face flip
face = [1,0,1,0]
# 1010 -> 1100->
# 1010 -> 0100 : -8 + 4 -2 = -6  ## 0100 -> 1010 :  8-4+2 =  6
# 1010 -> 0110 : -8 + 4 = -4
# 1010 -> 1101 :  4 - 2 + 1 = 3
# 1010 -> 1001 : -2 + 1 = -1
# 1010 -> 0000  # 8 + 0 + 2 + 0 = 10 -> -> 0
#
# 1110 ->         8 + 4 + 2 + 0 = 14
print(int('0b1010',2))
print([int(not i) for i in face])

print(0b1010 | 0b0000)
print(0b1111 & 0b0000)
print('^',bin(0b1010 ^ 0b0100))
print('^',bin(0b1010 ^ 0b1110))
print(~0b1111,bin(~0b1111))

idx = 1
#print(flip(idx,face))

'''
def flip(idx,face):
    try:
        if 0 < idx < len(face)-2:
           s = list(map(lambda x:not x,face if idx in range(idx-1,idx+1))
    except:
        s = face

    return s
'''
#https://www.unicode.org/emoji/charts/full-emoji-list.html
import emoji

#print([v for k,v in emoji.EMOJI_UNICODE['en'].items() ])

import emoji
# emoji.emojize() is deprecated and will be removed in version 2.0.0. Use language='alias' instead
print(emoji.emojize('Python is :thumbs_up:',language='alias'))
print(emoji.emojize('Python is :thumbs_up:',language='alias'))
#Python is 👍

print(emoji.emojize('Python is :smile:', language='alias'))
#Python is 👍

#print(emoji.demojize('Python is 👍'))
#Python is :thumbs_up:

#题目：有四个数字：1、2、3、4，能组成多少个互不相同且无重复数字的三位数？各是多少？
for num in range(6,58):
    a = num >> 4 & 3
    b = num >> 2 & 3
    c = num & 3
    if( (a^b) and (b^c) and (c^a) ):
        print (a+1,b+1,c+1)

#在实际编程中，如果能巧妙运用位操作，完全可以达到四两拨千斤的效果，正因为位操作的这些优点，
# 所以位操作在各大IT公司的笔试面试中一直是个热点问题
