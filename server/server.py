import socket

soc=socket.socket()
host=socket.gethostname()
port=8080
soc.bind((host,port))
soc.listen(1)
print(host)
print("Waiting for the incoming connections ......")

conn,addr=soc.accept()
print(addr,"Is successfully connected to the server")


fname=input("enter the file name: ")
file=open(fname,'rb')
file_content=file.read(1024)
conn.send(file_content)
print("File has been transmitted successfully")
