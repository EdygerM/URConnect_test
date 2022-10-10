import socket, struct

HOST = '172.31.0.101'
PORT = 30011

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
            if ord(robotMessageType) == 9:
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
                popupMessageTitle = struct.unpack_from('!%ds' % popupMessageTitleSize, data, offset)[0]
                offset += popupMessageTitleSize
                print(popupMessageTitle)
                popupTextMessage = struct.unpack_from('!8s', data, offset)[0]
                print(popupTextMessage)
            elif ord(robotMessageType) == 7:
                robotMessageCode = struct.unpack_from('!i', data, offset)[0]
                offset += 4
                robotMessageArgument = struct.unpack_from('!i', data, offset)[0]
                offset += 4
                robotMessageTitleSize = struct.unpack_from('!B', data, offset)[0]
                offset += 1
                robotMessageTitle = struct.unpack_from('!%ds' % robotMessageTitleSize, data, offset)[0]
                offset += robotMessageTitleSize
                print(robotMessageTitle)
                keyTextMessage = struct.unpack_from('!8s', data, offset)[0]
                print(keyTextMessage)

#packageSize = struct.unpack_from('!i', data, 5)[0]
#packageType = struct.unpack_from('!B', data, 9)[0]
#if packageType == :




