'''

ECT蟒蛇计划。主题公园游乐设施

 一目了然...核心科目数学
学科领域代数
建议的年龄13至16岁


概述
使用这个程序来帮助学生概念化文字问题，特别是。
在一个主题公园里有90个人在排队。每5分钟有40人上车，63人加入队伍。估计600人排队需要多长时间。
这个程序可以用来进一步了解如何在课堂上使用Python，作为与学生的演示或讨论，或者作为向学生介绍
各种CT概念的一种方式，如模式识别或抽象，邀请他们扩展程序的现有功能。

Python程序

'''
# Copyright 2015 Google Inc. All Rights Reserved.
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at

# http://www.apache.org/licenses/LICENSE-2.0

# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Word problem on estimation:  There are 90 people in line at a theme park ride.
Every 5 minutes, 40 people get on the ride and 63 join the line.
Estimate how long it would take for 600 people to be in line."""

starting_peeps = 90
time = 0
new_peeps = 63
leaving_peeps = 40

while starting_peeps <= 600:
    starting_peeps = starting_peeps + new_peeps - leaving_peeps
    time = time + 5

print(time, "minutes")

