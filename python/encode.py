'''
encode()和decode()
用来存放一位0或1，就是计算机里最小的存储单位，叫做【位】，也叫【比特】（bit）。
我们规定8个比特构成一个【字节】（byte），这是计算机里最常用的单位。
1B(byte)  = 8 bit
1KB = 1024B = 1024 byte

【编码】encode()；反之，就是【解码】decode()
'你想编码的内容'.encode('你使用的编码表')
'你想解码的内容'.decode('你使用的编码表')
'''
print('你好'.encode('utf-8'))
print('你好'.encode('gbk'))
print(b'\xe4\xbd\xa0\xe5\xa5\xbd'.decode('utf-8'))
print(b'\xc4\xe3\xba\xc3'.decode('gbk'))
# b'\xc4\xe3\xba\xc3'，这代表它是bytes（字节）类型的数据.
# \x是分隔符，用来分隔一个字节和另一个字节。
# 类似网址中的%：https://www.baidu.com/s?wd=%E5%90%B4%E6%9E%AB
# UTF-8编码的字节就一定要用UTF-8的规则解码，其他编码同理
print(type('你好'))
print(type(b'\xc4\xe3\xba\xc3')) 
# 字符：'1'， '中'， 'a'， '$'， '￥' 。
# 字节则是计算机中存储数据的单元，一个8位的二进制数


