'''
第三章 文件与异常:处理错误
'''
import os

print("当前工作目录：", end="")
print(os.getcwd())

os.chdir("Python/Head_First_Python/Chapter3")

print("切换工作目录为：", end="")
print(os.getcwd())

# 打开文件
data = open("sketch.txt")
print("第一行数据：")
print(data.readline())
print("第二行数据：")
print(data.readline(), end='')

#退回到文件起始位置，对于Python文件也可以使用tell()
data.seek(0)
print("-----使用for语句处理数据：------")
for each_item in data:
    print(each_item, end='')
print("-----for循环完毕-----")

# 关闭文件
data.close()
# 文件已关闭，不能使用
#data.read()

'''
Python有两种类型列表；一种是可以改变的列表（用中括号包围）另一种一旦创建就不能改变（用小括号包围），又称为元组。
Python中不可改变的常量列表称为元祖，一旦列表数据赋至一个元组，就不能再改变。元组是不可改变的。
'''

data = open("sketch.txt")
for each_item in data:

    # find()方法，找出一个字符串的一个字串，返回字串在原字符串中的索引，不存在返回-1
    # 数据中可能没有‘:’
    if not each_item.find(':') == -1:
        # split()方法返回一个字符串列表，这会赋至一个目标标识列表。称为多重赋值
        #(role, line_spoken) = each_item.split(":")
        # split()的第二个可选参数为分割成几个部分，0代表一个部分。
        (role, line_spoken) = each_item.split(':', 1)
        print(role, end='')
        print(' said: ', end='')
        print(line_spoken, end='')
data.close()

# 异常处理
data = open("sketch.txt")
for each_item in data:
    try:
        (role, line_spoken) = each_item.split(':', 1)
        print(role, end='')
        print(' said: ', end='')
        print(line_spoken, end='')
    except:
        pass #空语句
data.close()

# 不使用异常处理，需要增加更多错误检查代码
if os.path.exists("sketch.txt"):
    data = open("sketch.txt")
    for each_item in data:
        if not each_item.find(':') == -1:
            (role, line_spoken) = each_item.split(':', 1)
            print(role, end='')
            print(' said: ', end='')
            print(line_spoken, end='')
    data.close()
else:
    print('The data file is missing!')

# 使用异常处理机制，关注代码真正需要做什么，而不必操心哪里可能出现问题，让代码更容易读，容易写。
try:
    data = open("sketch.txt")
    for each_item in data:
        try:
            (role, line_spoken) = each_item.split(':', 1)
            print(role, end='')
            print(' said: ', end='')
            print(line_spoken, end='')
        except ValueError:
            pass
    data.close
except IOError:
    print("The data file is missing!")

'''
“异常”因运行时错误而出现，会产生一个Traceback
“Trackback”是出现的运行时错误的一个详细描述
'''