import socket
soc=socket.socket()
host=input(str("Enter the host address of the sender :"))
port=8080
soc.connect((host,port))
print("CONNECTED . . .")

fname=input("enter the file name that is to be recieved: ")
file=open(fname,'wb')
file_content=soc.recv(1024)
file.write(file_content)
file.close()
print("File has been recieved successfully")
