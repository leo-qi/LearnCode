'''
第七章 Web开发:集成在一起
'''
import os
import pickle
from AthleteList import AthleteList

os.chdir('Python/Head_First_Python/Chapter7')

def get_coach_data(filename):
    '''
    从文件获得数据
    '''
    try:
        with open(filename) as f:
            data = f.readline()
        templ = data.strip().split(',')
        return(AthleteList(templ.pop(0), templ.pop(0), templ))
    except IOError as error:
        print("File Error: " + str(error))
        return None

def put_to_store(files_list):
    '''
    提供一个文件名列表，用文件中的数据填充字典，保存到一个pickle中
    '''
    all_athletes = {}
    for each_file in files_list:
        ath = get_coach_data(each_file)
        all_athletes[ath.name] = ath
    try:
        with open('athletes.pickle', 'wb') as athf:
            pickle.dump(all_athletes, athf)
    except IOError as error:
        print("File Error(put_and_store): " + str(error))
    return all_athletes

def get_from_store():
    '''
    从文件中得到字典，并返回
    '''
    all_athletes = {}
    try:
        with open('athletes.pickle', 'rb') as athf:
            all_athletes = pickle.load(athf)
    except IOError as error:
        print("File Error(get_from_store): " + str(error))
    return all_athletes

the_files = ['james.txt','julie.txt','mikey.txt','sarah.txt']
data = put_to_store(the_files)
print(data)