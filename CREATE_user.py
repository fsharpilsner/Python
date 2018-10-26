

# coding: UTF-8 NO BOM

import requests
from requests.auth import HTTPBasicAuth


url_user_base='http://localhost/mysite/wp-json/wp/v2/users'


###POST create a user###
payload_a_user = {
           'username': 'znorre',
           'email': 'znorre@di.se',
           'password': '@@@snurr'
          }
ret_user = requests.post(url_user_base, auth=HTTPBasicAuth('elev','elev'),data=payload_a_user)
print ret_user.status_code
############################


