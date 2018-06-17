# -*- coding: utf-8 -*-

########################################################################
###  random
########################################################################
#
# 并非真正随机生成，系统可预测，os中的urandom类接近真正随机

from random import *

seq = [1, 3, 7, 9, 8, 15]
random()                    # 返回一个位于[0, 1]的随机数
uniform(1, 10)              # 返回一个位于[1, 10]的随机数
randrange(0,10,2)           # 返回一个位于range(start,stop,step)的随机数
choice(seq)                 # 随机返回序列seq中的一个元素
shuffle(seq)                # 就地打乱序列seq, <type 'list'>: [7, 3, 8, 9, 1, 15]
sample(seq,5)               # 随机返回序列seq中5个不同位置的元素
