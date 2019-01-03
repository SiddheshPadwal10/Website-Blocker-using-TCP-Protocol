import socket                   # Import socket module
#directory where file need to store
import os
import webbrowser
os.chdir('/Users/Sanket/Desktop/')

s = socket.socket()             # Create a socket object
host = '10.5.15.131'
port = 60000                    # Reserve a port for your service.
# STATE VARIABLES
state = "S0"
#send request to connect
s.connect((host, port))

#html code for restricted page

with open('restricted.html','a') as f:
                     f.write(
                             "<html>\n"
                             "<head>\n"
                              "Access Denied\n"
                             "</head>\n"
                             "<body>\n"
                              "cant access.\n"
                             "</body>\n"
                             "</html>\n"
                             )
                     f.close()

packet = raw_input("Enter Filename: ")

if state == "S0":
   
        s.send(packet)
        data = s.recv(1024)
        
        if data == '':
             #show restricted page
             webbrowser.open('restricted.html')

        else:
                #show the site redirected one or the actual searched page
                webbrowser.open(data)

                
        s.close()
        print('connection closed')

else:
    print("Problem...")
