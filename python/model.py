# 引入同一目录的模块
import testModel,random
testModel.hi()
# 引入同一目录的模块并使用别名
import testModel as test
test.hi()
# from … import …语句可以让你从模块中导入一个指定的部分到当前模块
from testModel import hi
hi()
# 程序的入口【if __name__ == '__main__'】

a = random.random()  # 随机从0-1之间（包括0不包括1）抽取一个小数
print(a)

# 随机从0-100（包括0和100）之间抽取一个数字
a = random.randint(0,100)  
print(a)
# 随机从字符串，列表等对象中抽取一个元素（可能会重复）
a = random.choice('abcdefg')  
print(a)
# 随机从字符串，列表等对象中抽取多个不重复的元素
a = random.sample('abcdefg', 3) 
print(a)
# “随机洗牌”，比如打乱列表
items = [1, 2, 3, 4, 5, 6]  
random.shuffle(items)
print(items)
# dir()函数查看一个模块，看看它里面有什么变量、函数、类、类方法
print(dir(random))
# dir(x)，可以查询到x相关的函数，x可以是模块，也可以是任意一种对象
a = ''  # 设置一个字符串
print('字符串：')
print(dir(a))    # 把字符串相关的函数展示出来
