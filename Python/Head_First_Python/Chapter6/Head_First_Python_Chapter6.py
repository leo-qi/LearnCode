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
'''
总结:

'''