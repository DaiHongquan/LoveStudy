'''
重复执行
continue 跳过当次循环
break 终止循环
pass 什么都不做
else 结束循环时没有碰到break语句，就会执行循环后面的else语句，否则就不会执行
for循环：循环的工作量确定
while：工作量不确定
for格式：for 元素名 in 数据集合
数据集合：序列、元组、字符串、列表、字典等
'''

# 打印从0至3（不包含3）的序列
for i in range(3):
    print(i,end='')
print()    
# 打印列表
for i in [3,2,1]:
    print(i,end='')
print()        
# 打印字典
for j,k in {'小明':88,'小红':97}.items():
    print(j)
    print(k)

# while循环
a = 0
while True:
    print(a)
    a += 1
    if a < 3:
        continue
    else:
        break