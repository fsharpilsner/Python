
# coding: UTF-8 NO BOM

import requests
from requests.auth import HTTPBasicAuth


url_user_base_to_delete='http://localhost/mysite/wp-json/wp/v2/users/14'


###DELETE a user###
payload_a_user = {
           'force': 'true',
            'reassign': '1'
          }
ret_user = requests.delete(url_user_base_to_delete, auth=HTTPBasicAuth('elev','elev'),data=payload_a_user)
print ret_user.status_code
############################

