import pymysql

db = pymysql.connect(host='localhost', user='root', password='971229',
db = 'IncheonNational', charset='utf8')

cur = db.cursor()
cur.execute("SELECT * FROM student")

rows = cur.fetchall()
print(rows)
db.close