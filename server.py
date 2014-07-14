import pickle
import json
import zmq

memory = {}
context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind('tcp://127.0.0.1:9999')
    
while True:
    command, key, data = pickle.loads(socket.recv())
    if command == 'set':
        memory[key] = data
        socket.send(b'ok')
    elif command == 'get':
        result = memory.get(key, None)
        socket.send(pickle.dumps(result))
    elif command == 'delete':
        try:
            del memory[key]
            socket.send(b'ok')
        except KeyError:
            socket.send(None)
    elif command == 'get_keys':
        socket.send(pickle.dumps(memory.keys()))

