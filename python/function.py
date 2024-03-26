'''
组织好的、可以重复使用的、用来实现单一功能的代码
定义函数 def 函数名(参数1,参数2,...参数n): 函数体 return 语句
如果没有return，实际是return None
调用函数 函数名(参数1,参数2,...参数n)
位置参数：按位置顺序传递
不定长参数：不确定参数个数
默认参数：给参数默认值，默认参数必须放在位置参数和不定长参数之后
返回多个参数（元组tuple[]）
'''

# 无参函数
def pika1():
    print('我最喜爱的神奇宝贝是皮卡丘')
# 多参求和函数
def sum(x,y):
    return x + y

# 定义打印圣诞树函数并调用
def tree(Height):
    print('Merry Christmas!')
    for i in range(Height):
        print((Height-i)*2*' '+'o'+ i*'~x~o')
        print(((Height-i)*2-1)*' '+(i*2+1)*'/'+'|'+(i*2+1)*'\\')
tree(4)

# 位置参数 appetizer,course 不定长参数：不确定参数个数 *barbeque，默认参数 dessert
def menu(appetizer,course,*barbeque,dessert='绿豆沙'):
    print('一份开胃菜：' + appetizer)
    print('一份主食：' + course)
    print('一份甜品：' + dessert)
    for i in barbeque :
        print('一份烤串：' + i)
menu('话梅花生','黄焖鸡米饭','牛肉串','羊肉串')

# 返回多个参数
def lover(name1,name2):
    face = name1 + '的脸蛋'
    body = name2 + '的身材'
    return face,body
a=lover('李若彤','林志玲')
print('返回多个参数（元组tuple[]）:')
print('我的梦中情人：'+a[0]+' + '+a[1])

