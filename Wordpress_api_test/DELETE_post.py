
# coding: UTF-8 NO BOM

import requests
from requests.auth import HTTPBasicAuth


url_del='http://localhost/mysite/wp-json/wp/v2/posts/27'


###DELETE a post###
ret_del=requests.delete(url_del)
print(ret_del.status_code)
###################
