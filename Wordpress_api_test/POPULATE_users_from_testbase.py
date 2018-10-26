
# coding: UTF-8 NO BOM

import requests
from requests.auth import HTTPBasicAuth
import MySQLdb


##### read from test data table/database ###############
##### and populate the main Wordpress database #########
db = MySQLdb.connect("localhost","root","","wordpress" )
db.autocommit(1)

cursor = db.cursor()
cursor.execute("USE wordpress")
cursor.execute("INSERT INTO wp_users(user_login, user_pass, user_email, user_registered, display_name)"
               "SELECT user_login, user_pass, user_email, user_registered, display_name FROM wp_users2add")
#################################################

db.commit

rows = cursor.fetchall()
print('Total Row(s):', cursor.rowcount)
for row in rows:
      print(row)


cursor.close
db.close
