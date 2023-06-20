import sqlite3 as sq

conn = sq.connect('db_2.db')
cur = conn.cursor()

# cur.execute('''
#             alter table zakaz
#             rename column kod to Saller
#             ''')

# cur.execute('''
#             alter table zakaz
#             add column new Integer
#             ''')

# cur.execute('''
#             alter table zakaz
#             drop column new
#             ''')
cur.execute("select * from zakaz")
rows = cur.fetchall()

for row in rows:
    print(row)

conn.close()
