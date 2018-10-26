#http://localhost/wp-json/posts/?content=%enstaka
# coding: UTF-8 NO BOM
# author: kavep

# the json result is a dicttionary or multi dimentional arry
# it can be accessed by indeces or strings. if Python says it
# must be integer then it is indexed by an integer and hence
# refered so. Otherwise is is refered by 'String' in the Endpoints.


import requests
from requests.auth import HTTPBasicAuth
import MySQLdb



#url_users_base='http://localhost/wp-json/users'
#url_user_base='http://localhost/wp-json/users/'
#url_user_base_to_delete='http://localhost/wp-json/users/69'
#url_del='http://localhost/wp-json/posts/39'

url_posts_base='http://localhost/mysite/wp-json/wp/v2/posts'

####GET######
#ret_get=requests.get(url_users_base, auth=HTTPBasicAuth('elev','elev'))
ret_get=requests.get(url_posts_base, auth=HTTPBasicAuth('elev','elev'))

#for x in range(0, 10):
#      print(ret_get.json()[x]['ID'])

#print(ret_get.json()[1]['ID'])
#print(ret_get.json()['modified'])
#print(ret_get.json()['author']['username'])
#print(ret_get.status_code)
###########################

###POST create a post###
payload_a_post = {
           'author': '1',
           'title': 'Hej Gamla Brogatan4!',
           'content': 'Den här fungerar',
           'status': 'publish'
           }

ret_post = requests.post(url_posts_base, auth=HTTPBasicAuth('elev','elev'),data=payload_a_post)
print ret_post.status_code
###########################


###POST create a user###
#payload_a_user = {
#           'username': 'snorre', 
#           'email': 'snorre@di.se',
#           'password': '@@snurr'
#          }
#ret_user = requests.post(url_user_base, auth=HTTPBasicAuth('elev','elev'),data=payload_a_user)
#print ret_user.status_code
############################


###DELETE a user###
#payload_a_user = {
#           'force':'true'
#          }
#ret_user = requests.delete(url_user_base_to_delete, auth=HTTPBasicAuth('elev','elev'),data=payload_a_user)
#print ret_user.status_code
############################




###DELETE a post###
#ret_del=requests.delete(url_del)
#print(ret_del.status_code)
###################



##### read from test data table/database ###############
##### and populate the main Wordpress database #########
#db = MySQLdb.connect("localhost","tester","Tester@@@","wordpress" )
#db.autocommit(1)

#cursor = db.cursor()
#cursor.execute("USE wordpress")


#cursor.execute("INSERT INTO wp_users(user_login, user_pass, user_email, user_registered)"
#               "SELECT user_login, user_pass, user_email, user_registered FROM wp_users2add")
#################################################

###### Check if post exists: Read back from post############
#cursor.execute("SELECT * FROM wp_posts WHERE post_title LIKE '%Gamla%'") 
#cursor.execute("SELECT * FROM wp_posts WHERE post_title LIKE 'Nedåt%';") 
#cursor.execute("SELECT * FROM wp_posts WHERE post_title LIKE '%s'") % string
########################################

#rows = cursor.fetchall()
#print('Total Row(s):', cursor.rowcount)
#for row in rows:
#      print(row)



#db.commit
#cursor.close
#db.close
