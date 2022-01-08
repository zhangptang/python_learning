# -*-coding:utf-8-*-
"""
 list的遍历方法
"""

list1 = [1, 4, 7, 10]

for index in range(len(list1)):
    print(list1[index], end=' ')

print('\n---------------')
for value in list1:
    print(value, end=' ')

for index, value in enumerate(list1):
    print('index is  {}, value is {}'.format(index, value))
