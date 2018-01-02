'''
第一章 初识Python:人人都爱列表
'''

# 列表的定义
movies = ["The Holy Grail", "The Life of Brian", "The Meaning of Life"]
print(movies[1])

cast = ["Cleese", "Palin", "Jones", "Idle"]
print(cast)

# len()BIF得出列表中数据个数
print(len(cast))
print(cast[1])

# append()在列表末尾增加数据
cast.append("Gilliam")
print(cast)

# pop()从列表末尾删除数据
cast.pop()
print(cast)

# extend() 在列表末尾增加一个列表
cast.extend(["Gilliam", "Chapman"])
print(cast)

# remove()在列表中找到并删除一个特定的数据项
cast.remove("Chapman")
print(cast)
# cast.remove("Chapman") # 再次移除 ValueError: list.remove(x): x not in list

# insert()在某个特定的位置前面增加一个数据项
cast.insert(0, "Chapman")
print(cast)

# 练习：向列表中增加更多的数据
# movies = ['The Holy Grail', 1975, 'The Life of Brian', 1979, 'The Meaning of Life', 1983]
movies.insert(1, 1975)
movies.insert(3, 1979)
movies.append(1983)
print(movies)

# 处理列表数据
# 迭代
fav_movies = ["The Holy Grail", "The Life of Brian", "The Meaning of Life"]
# for
for each_flick in fav_movies:
    print(each_flick)

# while 无特殊原因不会使用while
count = 0
while count < len(fav_movies):
    print(fav_movies[count])
    count = count + 1

# 试图访问一个不存在的数据项，Python会给出一个IndexError错误，代表"越界"

# 在列表中存储列表
movies = ["The Holy Grail", 1975, "Terry Jones & Terry Gilliam", 91,
          ["Graham Chapman",
           ["Micheal Palin", "John Cleese", "Terry Gilliam", "Eric Idle", "Terry Jones"]]]
print(movies[4][1][3])
# 只能循环一层列表
for each_item in movies:
    print(each_item)

# 在列表中查找列表
# isinstance() 检查某个特定标识符是否包含某个特定类型的数据
names = ["Michael", "Terry"]
print(isinstance(names, list))

num_names = len(names)
print(isinstance(num_names, list))

# 不能处理复杂的列表，列表中的列表中的列表
for each_item in movies:
    if isinstance(each_item, list):
        for nested_item in each_item:
            print(nested_item)
    else:
        print(each_item)
print("========= 递归 ========")
# 递归
def print_lol(the_list):
    for each_item in the_list:
        if isinstance(each_item, list):
            print_lol(each_item)
        else:
            print(each_item)
print_lol(movies)

'''
总结:
    内置函数（BIF）：
        print() 在屏幕上显示一个消息
        len() 得出列表中数据个数
        isinstance() 检查某个特定标识符是否包含某个特定类型的数据

    列表函数：
        append()在列表末尾增加数据
        pop()从列表末尾删除数据
        extend() 在列表末尾增加一个列表
        remove()在列表中找到并删除一个特定的数据项
        extend() 在列表末尾增加一个列表

    控制语句
        for 目标标识符 in 列表:
            列表处理代码

        while 循环条件:
            循环组

        if 某个条件满足:
            "True"组
        else:
            "False"组

    函数定义
        def 函数名([参数]):
            函数代码组
'''