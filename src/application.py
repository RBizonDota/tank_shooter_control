from app import sio, field

from config.const import HOST, PORT

from controllers.lazy_killer import LazyKillerController

controllers = {
    "lazy_killer": LazyKillerController
}

if __name__ == "__main__":
    sio.start_background_task(LazyKillerController().background_task, field)
    sio.connect(f'http://{HOST}:{PORT}', namespaces=['/field', '/tank_control'])