from socket import *
from datetime import *

serverPort = 12000
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))
serverSocket.listen(1)
print('W0123456 server is ready to receive')

def get_ip():
    s = socket(AF_INET, SOCK_DGRAM)
    try:
        # doesn't even have to be reachable
        s.connect(('10.255.255.255', 1))
        IP = s.getsockname()[0]
    except:
        IP = '127.0.0.1'
    finally:
        s.close()
    return IP

ip = get_ip()

while True:
    connectionSocket, addr = serverSocket.accept()
    sentence = connectionSocket.recv(1024).decode()
    capitalizedSentence = sentence.upper()
    # Region for Echo Filter
    filteredSentence = sentence.replace("ECHO ","",1)
    filteredSentenceCap = filteredSentence.upper()
    #Region for Hello
    helloSentence = sentence + ', Pleased to meet you'
    helloSentenceCap = helloSentence.upper()

    if "HELO" in sentence:
        print('W0123456 Server: Got HELO')
        connectionSocket.send(helloSentence.encode())
        connectionSocket.send(helloSentenceCap.encode())
    if sentence == "REQTIME":
        print('W0123456 Server: Got REQTIME')
        tim = datetime.now().strftime('%H:%M:%S')
        connectionSocket.send(tim.encode())
        connectionSocket.send(capitalizedSentence.encode())
    elif sentence == 'REQDATE':
        print('W0123456 Server: Got REQDATE')
        date = datetime.now().strftime('%Y-%m-%d')
        connectionSocket.send(date.encode())
        connectionSocket.send(capitalizedSentence.encode())
    elif "ECHO" in sentence :
        print ('W0123456 Server: Got ECHO')
        connectionSocket.send(filteredSentence.encode())
        connectionSocket.send(filteredSentenceCap.encode())
    elif sentence == 'REQIP':
        print('W0123456 Server: Got REQIP')
        connectionSocket.send(ip.encode())
        connectionSocket.send(capitalizedSentence.encode())
    elif sentence == 'BYE':
        print('W0123456 Server: Got BYE')
        connectionSocket.send('See ya Later'.encode())
        connectionSocket.send(capitalizedSentence.encode())
connectionSocket.close()





