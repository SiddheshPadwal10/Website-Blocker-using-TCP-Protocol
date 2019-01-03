import socket                   # Import socket module
import os
#select directory
path = os.chdir('/home/pi/Desktop/')
port = 60000  # Reserve a port for your service.

#to check all the files present in the directory
import glob
files = glob.glob('*.txt')
import time 
from datetime import datetime as dt

s = socket.socket()             # Create a socket object
host = '10.5.15.131'             # Get local machine name
s.bind((host, port))            # Bind to the port
s.listen(5)                     # Now wait for client connection.
state = "S0"
print 'Server listening....'
#for send the url
w = "www."
c = ".com"
redirect = "amazon.com/s?field-keywords={}"

while 1:
    if state == "S0":
        while True:
            conn, addr = s.accept()     # Establish connection with client.
            print 'Got connection from', addr
            website = conn.recv(1024)
            print('Server received', repr(website))

            #Check the working hours

            if dt(dt.now().year, dt.now().month, dt.now().day,12)< dt.now() < dt(dt.now().year, dt.now().month, dt.now().day,14):
                print("Working hours...")
                #To check the restricted site
                with open( "mytext.txt",'r+') as file:
                    content = file.read()
                    if website in content:
                        conn.send("")

                    else:
                        #To check the sites which needs to be redirect
                        with open( "redirect.txt",'r+') as file:
                            content = file.read()
                            if website in content:
                                conn.send(w+redirect.format(website))

                        #If website is not in restricted or redirected file        
                        conn.send(w+website+c)

            else:
                #If it is not in working hour
                print("{} request sent".format(website))
                conn.send(w+website+c)
    
            conn.close()
    else:
        print("Problem...")
