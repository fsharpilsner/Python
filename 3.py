#!/usr/bin/python

from flask import Flask
from  flask_socketio import socketio
import sys

app = Flask(__name__)
@app.route('/')
def api_root():
    return 'Welcome'

#min_c_re min_c_im max_c_re max_c_im max_n x y divisions list-of-servers
#-1 -1.5 2 1.5 1024 10000 10000 4 localhost:4444 localhost:3333 192.168.33.3:4444

@app.route('/articles/<min_c_re>/<min_c_im>/<max_c_re>/<max_c_im>/<max_n>/<x>/<y>/<inf_n>')
def api_article(min_c_re, min_c_im, max_c_re , max_c_im , max_n, x , y, inf_n):
  return 'You are reading ' + min_c_re + ' ' + min_c_im + ' ' + max_c_re + ' ' + max_c_im +  \
    ' ' + max_n + ' ' + x + ' ' + y + ' ' +inf_n

port_nr=int(sys.argv[1])

if __name__ == '__main__':
    #app.run(host='localhost', port=port_nr, threaded=True)
    app.run(port=port_nr, threaded=True)
    

#TODO: what to do with app routes now?
# The picture file is a location on the disk not an actual picture send to server.
