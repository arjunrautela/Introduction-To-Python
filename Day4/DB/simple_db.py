import sqlite3

conn = sqlite3.connect('music.sqlite3')

cur = conn.cursor()

cur.execute('DROP TABLE IF EXISTS Tracks')

cur.execute('CREATE TABLE Tracks (title TEXT, plays INTEGER)')
insert_command = 'INSERT INTO Tracks (title, plays) VALUES ({}, {})'.format( "'Thunderstruck'", 20 )

#print(insert_command)
#cur.execute('INSERT INTO Tracks (title, plays) VALUES ( ?, ? )',( 'Thunderstruck', 20 ) )

cur.execute(insert_command )

cur.execute('INSERT INTO Tracks (title, plays) VALUES ( ?, ? )',( 'My Way', 15 ) )

conn.commit()

cur.execute('Select title, plays from Tracks ')
print (cur.fetchall())
for row in cur:
    print (row)
    

#cur.execute('DELETE FROM Tracks WHERE plays < 100')
#UPDATE Tracks SET plays = 16 WHERE title = 'My Way'

#conn.commit()

conn.close()