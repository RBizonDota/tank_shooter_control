from .conf import sio

def send_control(data):
    sio.emit('tank_control', data, namespace='/tank_control')