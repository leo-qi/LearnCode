'''
第六章 定制数据对象:打包代码与数据
'''
import os
os.chdir('Python/Head_First_Python/Chapter6')
print(os.getcwd())
def sanitize(time_string):
    if "-" in time_string:
        splitter = '-'
    elif ':' in time_string:
        splitter = ':'
    else:
        return time_string

    (mins, secs) = time_string.split(splitter)

    return mins + '.' + secs

# 后续使用字典做更改
def get_coach_data(filename):
    try:
        with open(filename) as f:
            data = f.readline()
        return data.strip().split(',')
    except IOError as ioerror:
        print("File Error: " + str(ioerror))
        return None

sarah = get_coach_data('sarah2.txt')
(sarah_name, sarah_dob) = sarah.pop(0), sarah.pop(0)
print(sarah_name + "'s fastest times are: " + str(sorted(set([sanitize(t) for t in sarah]))[0:3]))

# 字典：是一个内置的数据结构（内置于Python），允许将数据与键而不是数字关联。
# 这样可以使内存中的数据与实际数据的结构保持一致。
# 创建字典
cleese = {}
# 使用工厂函数创建
palin = dict()
print(type(cleese))
print(type(palin))

cleese['Name'] = 'John Cleese'
cleese['Occupations'] = ['actor', 'comedian', 'writer', 'file producer']
palin = {'Name': 'Michael Palin', 'Occupations': ['comedian', 'actor', 'writer', 'tv']}
print(cleese['Name'])
print(cleese['Occupations'][-1])
palin['Birthplace'] = 'Broomhill, Sheffield, England'
cleese['Birthplace'] = "Weston-super-Mare, North Somerset, England"
print(palin)
print(cleese)

sarah_data = {}
sarah_data['Name'] = sarah.pop(0)
sarah_data["DOB"] = sarah.pop(0)
sarah_data['Times'] = sarah
print(sarah_data['Name'] + "'s fastest times are: " + str(sorted(set([sanitize(t) for t in sarah_data['Times']]))[0:3]))

def get_coach_data_new(filename):
    try:
        with open(filename) as f:
            data = f.readline()
        templ = data.strip().split(',')
        return {'Name':templ.pop(0),
                'DOB':templ.pop(0),
                # 不同意书中的写法
                #'Times': str(sorted(set([sanitize(t) for t in templ]))[0:3]})
                'Times': sorted(set([sanitize(t) for t in templ]))[0:3]}
    except IOError as ioerror:
        print("File Error: " + str(ioerror))
        return None

james = get_coach_data_new('james2.txt')
julie = get_coach_data_new('julie2.txt')
mikey = get_coach_data_new('mikey2.txt')
sarah = get_coach_data_new('sarah2.txt')
print(james['Name'] + "'s fastest times are: " + str(james['Times']))
print(julie['Name'] + "'s fastest times are: " + str(julie['Times']))
print(mikey['Name'] + "'s fastest times are: " + str(mikey['Times']))
print(sarah['Name'] + "'s fastest times are: " + str(sarah['Times']))

# 类：使用class创建类，每个定义的类都有一个特殊的方法，名为__init__(),可以通过这个方法控制如何初始化对象。
class Athlete:
    def __init__(self):
        # The code to initialize a "Athlete" object.
        pass
# 类实例
a = Athlete()

# self
# 定义一个类时，实际上是在定义一个定制工厂函数，然后可以在你的代码中使用这个工厂函数创建实例
# Python处理这行代码时，它把工厂函数调用转换为一下调用，明确了类、方法（自动设置为__init()__）和所处理的对象实例:
#  a = Athlete() ----> Athlete().__init__(a)
# 目标标识赋至self参数
# Python类中每个方法的第一个参数为self——调用对象实例。
class Athlete1():
    def __init__(self, value=0):
        self.thing = value
    def how_big(self):
        return(len(self.thing))
# 在一个对象实例上调用类方法时，Python要求第一个参数是调用对象实例，这往往赋至各方法的self参数。
d = Athlete1("Holy Grail") # --->Athlete1.__init__(d, "Holy Grail")
d.how_big() # ---> Athlete1.how_big(d)

class Athlete2:
    def __init__(self, a_name, a_dob=None, a_times =[]):
        self.name = a_name
        self.dob = a_dob
        self.times = a_times

sarah = Athlete2('Sarah Sweeney', '2002-6-17', ['2:58', '2.58', '1.56'])
james = Athlete2('James Jones')
print(type(sarah))
print(type(james))
print(sarah.name)
print(james.dob)

class Athlete3:
    def __init__(self, a_name, a_dob=None, a_times=[]):
        self.name = a_name
        self.dob = a_dob
        self.times = a_times
    def top3(self):
        return(sorted(set([sanitize(t) for t in self.times]))[0:3])
    def add_time(self, time_value):
        self.times.append(time_value)
    def add_times(self, times):
        self.times.extend(times)
    
def get_coach_data3(filename):
    try:
        with open(filename) as f:
            data = f.readline()
        templ = data.strip().split(',')
        return Athlete3(templ.pop(0), templ.pop(0), templ)
    except IOError as ioerror:
        print('File error: ' + str(ioerror))
        return None
    
james = get_coach_data3('james2.txt')
julie = get_coach_data3('julie2.txt')
mikey = get_coach_data3('mikey2.txt')
sarah = get_coach_data3('sarah2.txt')
print(james.name + "'s fastest times are: " + str(james.top3()))
print(julie.name + "'s fastest times are: " + str(julie.top3()))
print(mikey.name  + "'s fastest times are: " + str(mikey.top3()))
print(sarah.name  + "'s fastest times are: " + str(sarah.top3()))

vera = Athlete3('Vera Vi')
vera.add_time('1.31')
print(vera.top3())
vera.add_times(['2.22', '1-21', '2.22'])
print(vera.top3())
'''
总结:

'''