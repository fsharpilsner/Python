
# coding: UTF-8 NO BOM

import requests
from requests.auth import HTTPBasicAuth
import MySQLdb


#db = MySQLdb.connect("localhost","tester","Tester@@@","wordpress" )
db = MySQLdb.connect("localhost","root","","wordpress" )
db.autocommit(1)

cursor = db.cursor()
cursor.execute("USE wordpress")

###### Check if post exists: Read back from post############
#cursor.execute("SELECT * FROM wp_posts WHERE post_title LIKE '%Gamla%'") 
cursor.execute("SELECT * FROM wp_posts WHERE post_title LIKE '%Gamla%';")
#cursor.execute("SELECT * FROM wp_posts WHERE post_title LIKE '%s'") % string
########################################

db.commit

rows = cursor.fetchall()
print('Total Row(s):', cursor.rowcount)
for row in rows:
      print(row)


cursor.close
db.close
