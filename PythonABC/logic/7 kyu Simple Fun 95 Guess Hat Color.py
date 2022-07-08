'''
https://www.codewars.com/kata/58c21c4ff130b7cab400009e/solutions/python

任务挑战|puzzle
四个人，A、B、C和D，站成一排，一前一后。前三个人（a、b、c）和最后一个人（d）之间有一堵墙。
甲、乙、丙三人按身高顺序排成一排，这样。

1可以看到2和3的背影，2可以看到3的背影，3能看到墙
有4顶帽子，2个黑色，2个白色。每个人都有一顶帽子。他们都看不到自己的帽子，但是甲可以看到乙和丙的帽子，而乙可以看到丙的帽子，丙和丁都看不到任何帽子。
一旦一个人知道了自己帽子的颜色，就大声喊出来。你的任务是让谁先猜到自己的帽子，就把谁送回去。你可以假设他们只有在得出正确的结论时才会说话。
输入|输出
[输入]字符串a：a的帽子颜色"白 "或 "黑"
[输入]字符串b：b的帽子颜色“白 "或 "黑"
[输入]字符串c：c的帽子颜色"白 "或 "黑"
[输入]字符串d：d的帽子颜色"白 "或 "黑"
[输出]一个整数
先猜中他帽子颜色的人，1代表a，2代表b，3代表c，4代表d。
'''

def guess_hat_color(a,b,c,d):
    if b != c:
        return 2
    elif b == c:
        return 1