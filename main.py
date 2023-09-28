from system_module_2 import create_app
from config import HOST, PORT, DEBUG

if __name__ == '__main__':
    app = create_app()
    #Applying threading module for handle concurrency in the app definition
    app.run(host=HOST, port=int(PORT), debug=DEBUG, threaded=True)