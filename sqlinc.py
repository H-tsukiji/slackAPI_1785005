import MySQLdb

connection = MySQLdb.connect(
    host='localhost', user='root', passwd='', db='test')
cursor = connection.cursor()

cursor.execute("DROP TABLE IF EXISTS `sample`")
cursor.execute("""CREATE TABLE IF NOT EXISTS `sample` (
    `id` int(11) ,
    `name` varchar(128) ,
    PRIMARY KEY (id)
  )""")

cursor.execute("INSERT INTO sample VALUES (1, '佐藤')")


connection.close()