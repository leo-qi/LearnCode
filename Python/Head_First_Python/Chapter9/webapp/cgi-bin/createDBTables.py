import os
import sqlite3

os.chdir("Python/Head_First_Python/Chapter9/webapp/")
connection = sqlite3.connect('cocahdata.sqlite')
cursor = connection.cursor()

cursor.execute("""CREATE TABLE athletes (
    id integer primary key autoincrement unique not null,
    name text not null,
    dob date not null)""")

cursor.execute("""CREATE TABLE timing_data (
    athlete_id integer not null,
    value text not null,
    foreign key (athlete_id) references athletes)""")

connection.commit()

connection.close()