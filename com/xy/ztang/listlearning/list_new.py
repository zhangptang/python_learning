# -*-coding:utf-8-*-
"""
list 相关知识学习
"""

list1 = [1, 3, 5, 7]
print(list1)
# 元素重复
print(list1 * 3)
# 元素长度
print(len(list1))
# 下标运算
print(list1[0])
print(list1[3])
print(list1[-1])
print(list1[-4])
list1[2] = 20
print(list1)
# 遍历
for index in range(len(list1)):
    print(list1[index], end=' ')
# for遍历
print('\n----')
for item in list1:
    print(item, end=' ')
print("\n----")
# 通过enumerate函数处理列表之后再遍历可以同时获得元素索引和值
for index, item in enumerate(list1):
    print(f'{index} ==> {item}')
