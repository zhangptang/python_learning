# -*-coding:utf-8-*-

if __name__ == '__main__':
    s1 = '你好'
    s2 = 'hello world'
    s3 = "hellp python"
    print(s1, s2, s3, end='')
    # 字符转义
    print('转义')
    s4 = '\'hello child\''
    s5 = '\n\\hello child\\\n'
    print(s4, s5, end='')
    print('不转义')
    s6 = r'\'hello child\''
    s7 = r'\n\\hello child\\\n'
    print(s6, s7, end='')
    print('\n复制')
    str1 = 'h1' * 3
    print(str1)
    print('+ 字符串拼接')
    str2 = '一号字'
    str1 += str2
    print(str1)
    print('------in  not in 判断包含')
    print('h1' in str1)
    print('h2' not in str1)
    # 从字符串中取出指定位置的字符(下标运算)
    str3 = 'admin1234'
    print(str3[2])
    # 字符串切片(从指定的开始索引到指定的结束索引)
    print('str3[2:5] == {}'.format(str3[2:5]))
    print('str3[2:] == {}'.format(str3[2:]))
    print('str3[2::2] == {}'.format(str3[2::2]))
    print('str3[::2] == {}'.format(str3[::2]))
    print('str3[::-1] == {}'.format(str3[::-1]))
    print('str3[-3:-1] == {}'.format(str3[-3:-1]))
