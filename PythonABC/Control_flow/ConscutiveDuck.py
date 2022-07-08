'''
https://www.codewars.com/kata/5dae2599a8f7d90025d2f15f/train/python

 test.assert_equals(consecutive_ducks(69), True)
        test.assert_equals(consecutive_ducks(8), False)
        test.assert_equals(consecutive_ducks(57), True)
        test.assert_equals(consecutive_ducks(6), True)
        test.assert_equals(consecutive_ducks(13), True)
        test.assert_equals(consecutive_ducks(16), False)
        test.assert_equals(consecutive_ducks(91), True)
        test.assert_equals(consecutive_ducks(75), True)
        test.assert_equals(consecutive_ducks(38), True)
        test.assert_equals(consecutive_ducks(25), True)
        test.assert_equals(consecutive_ducks(32), False)
        test.assert_equals(consecutive_ducks(65), True)
        test.assert_equals(consecutive_ducks(13), True)
        test.assert_equals(consecutive_ducks(16), False)
        test.assert_equals(consecutive_ducks(99), True)
    @test.it("Check Medium Values")
    def __():
        test.assert_equals(consecutive_ducks(522), True)
        test.assert_equals(consecutive_ducks(974), True)
        test.assert_equals(consecutive_ducks(755), True)
        test.assert_equals(consecutive_ducks(512), False)
        test.assert_equals(consecutive_ducks(739), True)
        test.assert_equals(consecutive_ducks(1006), True)
        test.assert_equals(consecutive_ducks(838), True)
        test.assert_equals(consecutive_ducks(1092), True)
        test.assert_equals(consecutive_ducks(727), True)
        test.assert_equals(consecutive_ducks(648), True)
        test.assert_equals(consecutive_ducks(1024), False)
        test.assert_equals(consecutive_ducks(851), True)
        test.assert_equals(consecutive_ducks(541), True)
        test.assert_equals(consecutive_ducks(1011), True)
        test.assert_equals(consecutive_ducks(822), True)
    @test.it("Check Large Values")
    def __():
        test.assert_equals(consecutive_ducks(382131), True)
        test.assert_equals(consecutive_ducks(118070), True)
        test.assert_equals(consecutive_ducks(17209), True)
        test.assert_equals(consecutive_ducks(32768), False)
        test.assert_equals(consecutive_ducks(161997), True)
        test.assert_equals(consecutive_ducks(400779), True)
        test.assert_equals(consecutive_ducks(198331), True)
        test.assert_equals(consecutive_ducks(325482), True)
        test.assert_equals(consecutive_ducks(88441), True)
        test.assert_equals(consecutive_ducks(648), True)
        test.assert_equals(consecutive_ducks(65536), False)
        test.assert_equals(consecutive_ducks(323744), True)
        test.assert_equals(consecutive_ducks(183540), True)
        test.assert_equals(consecutive_ducks(65271), True)
        test.assert_equals(consecutive_ducks(5263987), True)
'''

# 限制从 1 开始的连续正整数
def consecutive_ducks(n):
    s = 0
    i = int((2 * n) ** 0.5)
    while s <= n*2:
        s = (i + 1) * i
        print(i,i+1,s,n*2)
        if s == n*2:
            return True
        i += 1
    return False
n = 5050
print(consecutive_ducks(n))


#