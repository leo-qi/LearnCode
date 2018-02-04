import pickle
from AthleteList import AthleteList
import sqlite3

#os.chdir('Python/Head_First_Python/Chapter7')

db_name = 'cocahdata.sqlite'

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

def get_name_from_store():
    '''
    获取选手名字列表
    Android使用，目前没有写Android，此功能没有测试
    '''
    connection = sqlite3.connect(db_name)
    cursor = connection.cursor()
    result = cursor.execute("SELECT name FROM athletes")
    response = [row[0] for row in result.fetchall()]
    connection.close()
    return response

def get_athlete_from_id(athlete_id):
    '''
    Android使用，目前没有写Android，此功能没有测试
    '''
    connection = sqlite3.connect(db_name)
    cursor = connection.cursor()
    result = cursor.execute("SELECT name, dob from athletes where id=?", athlete_id)
    (name, dob) = result.fetchone()
    result = cursor.execute("SELECT value from timing_data WHERE athlete_id=?", athlete_id)
    data = [row[0] for row in result.fetchall()]

    response = {'name': name,'DOB': dob, 'data': data, 'top3': data[0:3]}
    connection.close()
    return response

def get_namesID_from_store():
    connection = sqlite3.connect(db_name)
    cursor = connection.cursor()
    result = cursor.execute("select name, id from athletes")
    response = result.fetchall()
    connection.close()
    return response