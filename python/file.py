# 读
# 打开文件=>读文件=>关闭文件

# 第一个参数是文件的保存地址,第二个参数是读写模式，第三个参数是编码
file1 = open('./src/abc.txt','r',encoding='utf-8') 
filecontent = file1.read() 
print(filecontent)
file1.close() 

# 写
#打开文件=>写文件=>关闭文件
file1 = open('D:/study/visualStudioFile/LoveStudy/python/src/abc.txt','a',encoding='utf-8') 
file1.write('张无忌\n')     
file1.write('宋青书\n')     
file1.close()   

# 避免忘记关闭文件，可以使用 with as
#with open('文件地址','读写模式') as 变量名:
with open('./src/abc.txt','a',encoding='utf-8') as file1:
    #格式：冒号不能丢
    file1.write('张无忌') 
    #格式：对文件的操作要缩进
    #格式：无需用close()关闭

# file1.read() 读取全文
# file1.read(n) 读取n字节，可以连续读取，每读取一次，指针停留在读取后的位置
# file1.readline() 读取行,指针停留在读取后的位置
# file1.readlines() 读取所有行,返回一个列表，每个值是文本每一行
with open('./src/abc.txt','r',encoding='utf-8') as file1:
    #读取行，指针停留在读取后的位置。在读取时会跳过已读的这一行
    file_line = file1.readline()
    #读取所有行，在读取时会跳过已读的行
    file_lines = file1.readlines()
    # 遍历所有行
    for i in file_lines:
        # 将行数据按空格拆分
        data =i.split()  
    print(file_line)
    print(file_lines)
# file1.write(fileStr) 写全文
# file1.writeline(fileStr) 写一行,指针停留在写后的位置
# file1.writelines() 以列表形式写所有行,列表的每个值是文本每一行