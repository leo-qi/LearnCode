import sqlite3
import glob
import athletemodel

connection = sqlite3.connect('cocahdata.sqlite')
cursor = connection.cursor()



data_files = glob.glob('Python/Head_First_Python/Chapter9/webapp/data/*.txt')
athletes = athletemodel.put_to_store(data_files)

for each_ath in athletes:
    name = athletes[each_ath].name
    dob = athletes[each_ath].dob
    cursor.execute("insert into athletes (name, dob) values (?, ?)", (name, dob))
    connection.commit()

connection.close()
