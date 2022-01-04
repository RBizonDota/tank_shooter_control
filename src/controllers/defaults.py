from app.conf import sio

class ABSController:
    def __init__(self):
        # pass
        self.active = True
        self.prev = None

    def background_task(self, field):
        while self.active:
            if field.my_tank_id:
                resp = self.control(field)
                if resp!=self.prev:
                    sio.emit('tank_control', resp, namespace='/tank_control')
                    self.prev = resp
            
            sio.sleep(0.02)


    def control(self, field):
        raise NotImplementedError("Trying to use method of abstract class ABSController")