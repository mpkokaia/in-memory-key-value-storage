import zmq
import pickle
import sys

class UserInterface:
    def __init__(self):
        context = zmq.Context()
        self.socket = context.socket(zmq.REQ)
        self.socket.connect('tcp://127.0.0.1:9999')

    def get(self, key):
        self.socket.send(pickle.dumps(('get', key, None)))
        return pickle.loads(self.socket.recv())

    def set(self, key, data):
        self.socket.send(pickle.dumps(('set', key, data)))
        return self.socket.recv()

    def delete(self, key):
        self.socket.send(pickle.dumps(('delete', key, None)))
        return self.socket.recv()

    def get_keys(self):
        self.socket.send(pickle.dumps(('get_keys', None, None)))
        return pickle.loads(self.socket.recv())


data = None
user_interface = UserInterface()
while data != 'q':
    data = raw_input('>>')
    data = data.split()
    if data[0] == 'set':
        try:
            print user_interface.set(data[1], data[2])
        except IndexError:
            print 'Method takes exactly 2 arguments'
    elif data[0] == 'get':
        try:
            print user_interface.get(data[1])
        except IndexError:
            print 'Key undefined'
    elif data[0] == 'delete':
        try:
            print user_interface.delete(data[1])
        except IndexError:
            print 'Key undefined'
    elif data[0] == 'get_keys':
        keys = user_interface.get_keys()
        for i in keys: print i
    elif data[0] == 'q':
        sys.exit()

