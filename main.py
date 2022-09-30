# http://192.168.1.72:6788/HelloWorld.html
#from socket import *
import socket
import sys

serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Assign a port number

serverPort = 6788

# Bind the socket to server address and server port

serverSocket.bind(("", serverPort))

serverSocket.listen(1)

# Server should be up and running and listening to the incoming connections

while True:

    print ('Ready to serve...')
    connectionSocket, addr = serverSocket.accept()

    try:
        message = connectionSocket.recv(1024)

        print ('Message is: ', message)

        filename = message.split()[1]

        print ('File name is: ', filename)

# Because the extracted path of the HTTP request includes

        f = open(filename[1:])

        outputdata = f.read()

# Send the HTTP response header line to the connection socket

        connectionSocket.send("HTTP/1.1 200 OK\r\n\r\n")

# Send the content of the requested file to the connection socket

        for i in range(0, len(outputdata)):

            connectionSocket.send(outputdata[i])

        connectionSocket.send("\r\n")

# Close the client connection socket

        connectionSocket.close()

    except IOError:

# Send HTTP response message for file not found

        connectionSocket.send("HTTP/1.1 404 Not Found\r\n\r\n")

        connectionSocket.send("<html><head></head><body><h1>404 Not Found</h1></body></html>\r\n")

# Close the client connection socket

connectionSocket.close()

serverSocket.close()
sys.exit()