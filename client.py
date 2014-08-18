import socket

MICAH = '54.79.34.242'
PETE = '54.191.244.34'
BEN = '54.191.165.12'
JOHN = '54.79.29.105'
SRIRAM = '54.191.241.93'
TCP_PORT = 5950
BUFFER_SIZE = 10000

#Open text file to read the received data
file = open("file.txt", "r")
data = file.read()
file.close()

#Prompt user what they want to append
print 'Data received: ', data
print "Enter what you want to append:"
temp = raw_input()
new_data = " ".join((data, temp)) 

#Check who the recipient is
print "\nEnter recipient:"
recipient = raw_input()
if recipient.lower()=='micah':
	TCP_IP = MICAH
elif recipient.lower()=='pete':
	TCP_IP = PETE
elif recipient.lower()=='ben':
	TCP_IP = BEN
elif recipient.lower()=='john':
	TCP_IP = JOHN
elif recipient.lower()=='sriram':
	TCP_IP = SRIRAM
else: 
	print "Recipient you entered is unknown."
	exit()

#Open socket and send new_data to the next recipient
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))
s.send(new_data)
print 'Data sent.'
s.close()




