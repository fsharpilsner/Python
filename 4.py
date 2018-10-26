
#min_c_re min_c_im max_c_re max_c_im max_n x y divisions list-of-servers
#-1 -1.5 2 1.5 1024 10000 10000 4 localhost:4444 localhost:3333 192.168.33.3:4444

import sys
import subprocess
import threading
from ipaddress import ip_address

min_c_re = float(sys.argv[1])
min_c_im = float(sys.argv[2])
max_c_re = float(sys.argv[3])
max_c_im = float(sys.argv[4])
max_n = float(sys.argv[5])
x = int(sys.argv[6])
y = int(sys.argv[7])
divisions = int(sys.argv[8])

server1= sys.argv[9]
server2= sys.argv[10]
server3= sys.argv[11]

ip, separator, port = server1.rpartition(':')
assert separator 
server1_adress= "./3.py " + port


ip, separator, port = server2.rpartition(':')
assert separator 
server2_adress= "./3.py " + port



ip, separator, port = server3.rpartition(':')
assert separator 
server3_adress= "./3.py " + port

def Render_Server_1():
       s= subprocess.call([server1_adress], shell=True)
def Render_Server_2():
       s= subprocess.call([server2_adress], shell=True)
def Render_Server_3():
       s= subprocess.call([server3_adress], shell=True)


t1 = threading.Thread(target=Render_Server_1)
t1.start()

t2 = threading.Thread(target=Render_Server_2)
t2.start()

t3 = threading.Thread(target=Render_Server_3)
t3.start()


if len (sys.argv) != 12 :
    print("usage: " , sys.argv[0], "min_c_re min_c_im max_c_re max_c_im max_n x y divisions list-of-servers")
    sys.exit (1)
