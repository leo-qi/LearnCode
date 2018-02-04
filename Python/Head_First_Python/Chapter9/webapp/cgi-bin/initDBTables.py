import os
import sqlite3
import glob
import athletemodel
os.chdir("Python/Head_First_Python/Chapter9/webapp/")
connection = sqlite3.connect('cocahdata.sqlite')
cursor = connection.cursor()

data_files = glob.glob('data/*.txt')
athletes = athletemodel.put_to_store(data_files)

for each_ath in athletes:
    name = athletes[each_ath].name
    dob = athletes[each_ath].dob
    cursor.execute("insert into athletes (name, dob) values (?, ?)", (name, dob))
    connection.commit()
    cursor.execute("SELECT id FROM athletes WHERE name=? AND dob=?", (name, dob))
    athletes_id = cursor.fetchone()[0]
    for each_time in athletes[each_ath].clean_data():
        cursor.execute("INSERT INTO timing_data (athlete_id, value) VALUES (?, ?)", (athletes_id, each_time))

connection.commit()

connection.close()
