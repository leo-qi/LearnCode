import cgi
import sqlite3
import yate

print(yate.start_respone('text/plain'))

form = cgi.FieldStorage()
the_id = form['Athlete'].value
the_time = form['Time'].value
connection = sqlite3.connect('coachdata.sqlite')
cursor = connection.cursor()
cursor.execute("insert into timing_data (athlete_id, value) values (?, ?)", (the_id, the_time))
connection.commit()
connection.close()
print('OK.')