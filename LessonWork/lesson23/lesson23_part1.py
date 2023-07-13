import sqlite3 as sq

conn = sq.connect('db_1.db')
cur = conn.cursor()

cur.execute("select * from T1")
# cur.execute("select distinct Doljnost from T1")
# cur.execute("select doljnost, fname, ZP "
#             "from T1 "
#             "ORDER BY doljnost, fname, ZP")
# cur.execute("select * from T1")
# cur.execute("select * from T1")

rows = cur.fetchall()

for row in rows:
    print(rows)

conn.close()
