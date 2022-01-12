# -*-coding:utf-8-*-

"""
 字符串中一些方法的调用实例
"""

if __name__ == '__main__':
    str1 = 'adminpwd1234'
    # 计算字符串的长度
    print(len(str1))
    # 字符串首字母大写
    print(str1.capitalize())
    # 字符串每个单词首字母大写
    print(str1.title())
    # 字符串字母大写
    print(str1.upper())
    # 从字符串中查找子串的位置
    print(str1.find('12'))
    print(str1.find('tl'))
    # 与find类似但找不到子串时会引发异常
    print(str1.index('12'))
    # print(str1.index('tl'))
    # 字符串是否以某个字符开头
    print(str1.startswith('admin'))
    print(str1.startswith('pwd'))
    # 字符串是否以某个字符结尾
    print(str1.endswith('34'))
    print(str1.endswith('admin'))
    # 将字符串以指定的宽度居中并在两侧填充指定的字符
    print(str1.center(30, '*'))
    # 将字符串以指定的宽度靠右放置左侧填充指定的字符
    print(str1.rjust(30, ' '))
    # 检测字符串是否由数字组成
    print(str1.isdigit())
    # 检测字符串是否由字母组成
    print(str1.isalpha())
    # 检测字符串是有字母和数据组成
    print(str1.isalnum())
    str2 = '   zptang_study@163.com '
    # 字符串修剪左右两侧的空格
    print(str2.strip())
    # 修剪左侧空格
    print(str2.lstrip())
    # 修剪右侧空格
    print(str2.rstrip())
    str3= 'ready go \n'
    # 修剪右侧\n
    print(str3.rstrip('\n'))
    print('------')
