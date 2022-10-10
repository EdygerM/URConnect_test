import socket, struct

HOST = '172.31.0.101'
PORT = 30001

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
print('Connected')
while True:
    data = s.recv(4096)
    offset = 0
    if data:
        messageSize = struct.unpack_from('!i', data)[0]
        offset += 4
        messageType = struct.unpack_from('!B', data, offset)[0]
        offset += 1
        if messageType == 20:
            timestamp = struct.unpack_from('!Q', data, offset)[0]
            offset += 8
            source = struct.unpack_from('!c', data, offset)[0]
            offset += 1
            robotMessageType = struct.unpack_from('!c', data, offset)[0]
            offset += 1
            print(ord(robotMessageType))
            if robotMessageType == '2':
                requestId = struct.unpack_from('!I', data, offset)[0]
                offset += 4
                requestedType = struct.unpack_from('!I', data, offset)[0]
                offset += 4
                warning = struct.unpack_from('!?', data, offset)[0]
                offset += 1
                error = struct.unpack_from('!?', data, offset)[0]
                offset += 1
                blocking = struct.unpack_from('!?', data, offset)[0]
                offset += 1
                popupMessageTitleSize = struct.unpack_from('!B', data, offset)[0]
                offset += 1
                popupMessageTitle = struct.unpack_from('!s', data, offset)[0]
                offset += popupMessageTitleSize
                popupTextMessage = struct.unpack_from('!s', data, offset)[0]
                print(popupTextMessage)
            elif robotMessageType == 7:
                robotMessageCode = struct.unpack_from('!i', data, offset)[0]
                offset += 4
                robotMessageArgument = struct.unpack_from('!i', data, offset)[0]
                offset += 4
                popupMessageTitleSize = struct.unpack_from('!B', data, offset)[0]
                offset += 1
                popupMessageTitle = struct.unpack_from('!s', data, offset)[0]
                offset += popupMessageTitleSize
                popupTextMessage = struct.unpack_from('!s', data, offset)[0]
                print(popupTextMessage)

#packageSize = struct.unpack_from('!i', data, 5)[0]
#packageType = struct.unpack_from('!B', data, 9)[0]
#if packageType == :




