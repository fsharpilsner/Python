
# coding: UTF-8 NO BOM

import requests
from requests.auth import HTTPBasicAuth



url_post_base='http://localhost/mysite/wp-json/wp/v2/posts'


####GET posts######
ret_get=requests.get(url_post_base, auth=HTTPBasicAuth('elev','elev'))
print(ret_get.content)
print(ret_get.status_code)
###########################
