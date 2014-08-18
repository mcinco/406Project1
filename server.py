import socket

TCP_IP = '0.0.0.0'
TCP_PORT = 5950
BUFFER_SIZE = 10000


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((TCP_IP, TCP_PORT))
s.listen(1)

conn, addr = s.accept()
print 'Connection address: ', addr
while 1:
	data = conn.recv(BUFFER_SIZE)
	if not data: break
	print "Received data: ", data
	file = open("file.txt", "w")
	file.write(data)
	file.close()
	print "Received data saved in file"
	conn.send('Data received, thanks.')
conn.close()

