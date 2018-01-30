'''
第九章 管理你的数据:输入处理
'''

'''
利用Python的数据库API
1、连接：建立与数据库的连接
2、创建：创建一个游标，通过连接与数据通信
3、交互：利用游标，是用SQL管理数据
4、提交\回滚
5、关闭：撤销与数据库后台的连接（游标也会撤销）
'''
import sqlite3

connection = sqlite3.connect('test.sqlite')

cursor = connection.cursor()

cursor.execute("""SELECT DATE('NOW')""")
# 大多数数据库系统并不需要提交，不过SQLLite要求提交
connection.commit()

connection.close()

'''
coachdata.sqlite
create table athletes (
    id integer primary key autoincrement unique not null,
    name text not null,
    dob date not null
)

create table timing_data(
    athlete_id integer not null,
    value text not null,
    foreign key (athlete_id) references athletes
)
'''

connection = sqlite3.connect('cocahdata.sqlite')
cursor = connection.cursor()
cursor.execute("""CREATE TABLE athletes (
    id integer primary key autoincrement unique not null,
    name text not null,
    dob date not null)""")

#cursor.execute("INSERT INTO athletes (name, dob) VALUES (?, ?)", (name, dob))
cursor.execute("""CREATE TABLE timing_data (
    athlete_id integer not null,
    value text not null,
    foreign key (athlete_id) references athletes)""")
connection.commit()
connection.close()