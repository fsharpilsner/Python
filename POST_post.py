
# coding: UTF-8 NO BOM

import requests
from requests.auth import HTTPBasicAuth


url_post_base='http://localhost/wp-json/posts/'


###POST create a post###
payload_a_post = {
           'author': '60',
           'title': 'Hej Gamla Brogatan3!',
           'content': 'Den här fungerar', 
           'status': 'publish'
           }

ret_post = requests.post(url_post_base, auth=HTTPBasicAuth('elev','elev'),data=payload_a_post)
print ret_post.status_code
###########################
