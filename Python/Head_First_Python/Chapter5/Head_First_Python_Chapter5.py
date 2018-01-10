'''
第五章 推导数据:处理数据
'''
import os
os.chdir("Python/Head_First_Python/Chapter5")
print(os.getcwd())
with open('james.txt') as james_file:
    data = james_file.readline()
james = data.strip().split(',')

with open('julie.txt') as julie_file:
    data = julie_file.readline()
julie = data.strip().split(',')

with open('mikey.txt') as mikey_file:
    data = mikey_file.readline()
mikey = data.strip().split(',')

with open('sarah.txt') as sarah_file:
    data = sarah_file.readline()
sarah = data.strip().split(',')

print(james)
print(julie)
print(mikey)
print(sarah)

# 排序的两种方式
# 原地排序是指按你指定的顺序排列数据，然后用排序后的数据替换原来的数据。原来的数据会丢失。
# 对于列表，sort()方法会提供原地排序，默认升序，使用参数reverse=True降序
data = [6, 3, 1, 2, 4, 5]
print(data)
data.sort()
print(data)

# 复制排序是指按你指定的顺序排列数据，然后返回原数据的一个有序副本。原数据的顺序依然保留，只是对一个副本排序。
# 在Python中，sorted()BIF支持复制排序，默认升序，使用参数reverse=True降序
data = [6, 3, 1, 2, 4, 5]
data2 = sorted(data)
print(data)
print(data2)

print(sorted(james))
print(sorted(julie))
print(sorted(mikey))
print(sorted(sarah))
'''
def sanitize(time_string):
    if '-' in time_string:
        time_string = time_string.replace('-', '.')
    elif ':' in time_string:
        time_string = time_string.replace(':', '.')
    return time_string
'''
def sanitize(time_string):
    if '-' in time_string:
        splitter = '-'
    elif ':' in time_string:
        splitter = ':'
    else:
        return(time_string)
    (mins,secs) = time_string.split(splitter)
    return (mins + '.' + secs)

clean_james = []
clean_julie = []
clean_mikey = []
clean_sarah = []

for each_t in james:
    clean_james.append(sanitize(each_t))
for each_t in julie:
    clean_julie.append(sanitize(each_t))
for each_t in mikey:
    clean_mikey.append(sanitize(each_t))
for each_t in sarah:
    clean_sarah.append(sanitize(each_t))

print(sorted(clean_james))
print(sorted(clean_julie))
print(sorted(clean_mikey))
print(sorted(clean_sarah))

# 列表推导（list comprebension)，为了减少讲一个列表转换为另一个列表所需编写的代码量
mins = [1, 2, 3]
# 秒转换分钟
secs = [m * 60 for m in mins]
print(secs)

# 米转换英尺
meters = [1, 10, 3]
feet = [m * 3.281 for m in meters]
print(feet)

# 转换成大写
lower = ['I', "don't", "like", "spam"]
upper = [s.upper() for s in lower]
print(upper)

print(sorted([sanitize(t) for t in james]))
print(sorted([sanitize(t) for t in julie]))
print(sorted([sanitize(t) for t in mikey]))
print(sorted([sanitize(t) for t in sarah]))

# 迭代删除重复项
james = sorted([sanitize(t) for t in james])
julie = sorted([sanitize(t) for t in julie])
mikey = sorted([sanitize(t) for t in mikey])
sarah = sorted([sanitize(t) for t in sarah])
unique_james = []
for each_t in james:
    if each_t not in unique_james:
        unique_james.append(each_t)

print(unique_james[0:3])
unique_julie = []
for each_t in julie:
    if each_t not in unique_julie:
        unique_julie.append(each_t)
# 分片
print(unique_julie[0:3])

unique_mikey = []
for each_t in mikey:
    if each_t not in unique_mikey:
        unique_mikey.append(each_t)
print(unique_mikey[0:3])

unique_sarah = []
for each_t in sarah:
    if each_t not in unique_sarah:
        unique_sarah.append(each_t)
print(unique_sarah[0:3])

# 用集合删除重复项
# python中的集合中的数据项是无序且不允许重复。
# 使用set()BIF创建一个空集合
distances = set()
print(distances)
# 使用大括号完成集合的创建和填充
distances = {10.6, 11 ,8, 10.6, "tow", 7}
print(distances)
# 使用set()完成集合的创建和填充
distances = set(james)
print(distances)

# 工厂函数：工厂函数用于创建某种类型的新的数据项

def get_each_data(filename):
    try:
        with open(filename) as f:
            data = f.readline()
        return(data.strip().split(','))
    except IOError as ioerr:
        print('File Error: ' + str(ioerr))
        return(None)

james = get_each_data('james.txt')
julie = get_each_data('julie.txt')
mikey = get_each_data('mikey.txt')
sarah = get_each_data('sarah.txt')

print(sorted(set([sanitize(t) for t in james]))[0:3])
print(sorted(set([sanitize(t) for t in julie]))[0:3])
print(sorted(set([sanitize(t) for t in mikey]))[0:3])
print(sorted(set([sanitize(t) for t in sarah]))[0:3])