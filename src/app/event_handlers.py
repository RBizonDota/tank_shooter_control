from .conf import sio, field

# connect
@sio.event(namespace='/tank_control')
def connect():
    print("I'm connected!")
    sio.emit('init', {"Hello world!":1}, namespace='/tank_control', callback=lambda x: field.set_tank_id(x["id"]))
    # print("RESP", resp)

@sio.event
def connect_error(data):
    print("The connection failed!")

@sio.event
def disconnect():
    print("I'm disconnected!")

# /field

@sio.event(namespace='/field')
def field_data(data):
    # print("FIELD_DATA", data)
    # pass
    field.update_data(data)

# /tank_control

# @sio.event(namespace='/tank_control')
# def tank_control(data):
#     print("TANK_CONTROL", data)

# @sio.event(namespace='/tank_control')
# def init(data):
#     print("YOUR_TANK", data)