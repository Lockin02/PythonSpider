import pymysql


db = pymysql.connect(host='localhost', user='root', password='000000', port=3306, db='spiders')
data = {
    'id': '201200004',
    'name': 'Jane',
    'age': 28
}
cursor = db.cursor()
table = 'students'
keys = ', '.join(data.keys())
values = ', '.join(['%s'] * len(data))
sql = 'INSERT INTO {table}({keys}) VALUES ({values}) ON DUPLICATE KEY UPDATE'.format(table=table, keys=keys, values=values)
update = ', '.join([" {key}=%s".format(key=key) for key in data])
sql += update
try:
    if cursor.execute(sql, tuple(data.values())*2):
        print('Successful')
        db.commit()
except TypeError:
    print('Failed')
    db.rollback()
db.close()

