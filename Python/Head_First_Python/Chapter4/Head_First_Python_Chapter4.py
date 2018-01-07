'''
第四章 持久存储:数据保存到文件
'''
import os

os.chdir('Python/Head_First_Python/Chapter4/')
print(os.getcwd())

man = []
other = []
try:
    data = open("sketch.txt")
    for each_item in data:
        try:
            (role, line_spoken) = each_item.split(':', 1)
            # strip()方法从字符串中去除不想要的空白符。
            line_spoken = line_spoken.strip()
            if role == 'Man':
                man.append(line_spoken)
            elif role == 'Other Man':
                other.append(line_spoken)
        except ValueError:
            pass
    data.close()
except IOError:
    print('The data file is missing!')

#print(man)
#print(other)
'''
使用open()BIF打开磁盘文件时，可以指定使用什么访问模式。
默认地，open()使用模式r表示读，
访问模式为w，打开文件完成写，如果文件已经存在，则清除现有内容，写入新内容。
访问模式为w+, 如果文件存在，追加内容。
''' 
try:
    man_file = open('man_data.txt', 'w')
    other_file = open('other_data.txt', 'w')
    print(man, file=man_file)
    print(other, file=other_file)

    man_file.close()
    other_file.close()
except IOError:
    print("File Error!")

# 使用 finally 语句
try:
    man_file = open('man_data.txt', 'w')
    other_file = open('other_data.txt', 'w')

    print(man, file=man_file)
    print(other, file=other_file)
except IOError:
    print('File Error')
finally:
    man_file.close()
    other_file.close()

# 运行时出现一个错误时，Python会产生一个特定类型的异常（如IOError ValueError等）
# Python会创建一个异常对象，它会作为一个参数传入except代码组
# 文件不存在时，数据文件对象并未创建，这样就不可能在数据对象上调用close()方法，所以最后会得到一个NameError错误。
# locals()BIF会返回当前作用域中定义的所有名的一个集合。如果能找到，说明文件已经成功打开。
try:
    missing_data = open("missing.txt")
    print(missing_data.readline())
except IOError as error:
    print('File Error' + str(error)) #str()BIF转化成一个字符串。
finally:
    if 'missing_dat' in locals():
        missing_data.close()
'''
 Python中的字符串是不可变的。元组、数值类型都是不可以改变的。

'''

# 用with处理文件
# 由于处理文件时try/except/finally模式相当常用，所有Python提供了一个语句抽象出相关的一些细节。
# 使用with时，不在需要操心关闭打开的文件。
try:
    with open('its.txt', 'w') as its_data:
        print('It\'s...', file=its_data)
except IOError as err:
    print('File Error: ' + str(err))

# with语句利用了一种名为上下文管理协议（context management protocl)的Python技术。
try:
    with open('man_data.txt', 'w') as man_file, open('other_data.txt', 'w') as other_file:
        print(man, file=man_file)
        print(other, file=other_file)
except IOError as err:
    print('File Error: ' + str(err))

import nester
man = []
other = []
try:
    data = open('sketch.txt')
    for each_item in data:
        try:
            (role, line_spoken) = each_item.split(':', 1)
            line_spoken = line_spoken.strip()
            if role == 'Man':
                man.append(line_spoken)
            elif role == 'Other Man':
                other.append(line_spoken)
        except ValueError:
            pass
    data.close()
except IOError as ioError:
    print('File Error: ' + str(ioError))
try:
    with open('man_data.txt', 'w') as man_file, open('other_data.txt', 'w') as other_file:
        nester.print_lol(man, fh=man_file)
        nester.print_lol(other, fh=other_file)
except IOError as ioError:
    print('File Error: ' + str(ioError))

# "腌制"数据
# Python提供了一个标准库，名为pickle，它可以保存和加载几乎任何Python数据对象，包括列表。
# 用dump保存，用load恢复。处理腌制数据时必须以二进制访问模式打开这些文件.
# 腌制或者解除数据时如果出现了问题，pickle模块会产生一个PickleError类型的异常
import pickle

try:
    # 文件访问模式‘wb': 可写二进制模式。
    with open('man_data.txt', 'wb') as man_file, open('other_data.txt', 'wb') as other_file:
        pickle.dump(man, man_file)
        pickle.dump(other, other_file)
except IOError as ioError:
    print('File Error: ' + str(ioError))

