import sqlite3

con = sqlite3.connect('marksDB06.db')

cur = con.cursor()
data = cur.execute('''select * from MarksDB06 ''')

for row in data:
    rollno = row[0]
    studname = row[1]
    phymarks = row[2]

    print(str(rollno) + "  " + studname +"   "+ str(phymarks))

