#http://localhost/wp-json/posts/?content=%enstaka
# coding: UTF-8 NO BOM

# the json result is a dicttionary or multi dimentional arry
# it can be accessed by indeces or strings. if Python says it
# must be integer then it is indexed by an integer and hence
# refered so. Otherwise is is refered by 'String' in the Endpoints.


import requests
from requests.auth import HTTPBasicAuth

url_users_base='http://localhost/mysite/wp-json/wp/v2/users'
url_post_base='http://localhost/mysite/wp-json/wp/v2/posts/'


####GET######
ret_get=requests.get(url_users_base, auth=HTTPBasicAuth('elev','elev'))

#user_list=[0]

for x in range(0, 7):
      Author_ID=ret_get.json()[x]['id']
      Author_name= ret_get.json()[x]['name']
      #user_list.append(Author)
      ###POST create a post###
      payload_a_post = {
            'content-Type': 'application/json',
            'content': '\nText: ' + Author_name,
            'author': Author_ID,
            'title': 'Hej Gamla Brogatan! '+ Author_name,
            'status': 'publish'
            }
      ret_post = requests.post(url_post_base , auth=HTTPBasicAuth('elev','elev') , data=payload_a_post)
      print Author_name + ' posted'
      print ret_post.status_code
###########################


#print(ret_get.json()[1]['ID'])
#print(ret_get.json()['modified'])
#print(ret_get.json()['author']['username'])
#print(ret_get.status_code)
#print(user_list)
###########################








