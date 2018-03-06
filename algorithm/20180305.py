#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
大厅里有100盏灯，每盏灯都编了号码，分别为1-100。每盏灯由一个开关来控制。（开关按一下，灯亮，再按一下灯灭。开关的编号与被控制的灯相同。）开始时，灯是全灭的。现在按照以下规则按动开关。
第一次，将所有的灯点亮。
第二次，将所有2的倍数的开关按一下。
第三次，将所有3的倍数的开关按一下。
以此类推。第N次，将所有N的倍数的开关按一下。
问第100次按完以后，大厅里还有几盏灯是亮的。
'''

light = [0] * 100
for i in range(1, 101):
    for k in range(i, 101):
        if k % i == 0:
            if light[k - 1] == 0:
                light[k - 1] = 1
            else:
                light[k - 1] = 0

count = 0
s = ""
for i in range(len(light)):
    if light[i] == 1:
        count += 1
        s += "-" + str(i + 1)

print count
print s[1:]
