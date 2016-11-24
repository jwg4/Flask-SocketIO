from gevent import monkey
monkey.patch_all()

from flask import Flask, request
from flask_socketio import SocketIO

socketio = SocketIO()

def create_app():
    app = Flask(__name__)

    # The test succeeds with the following line:
    #socketio.init_app(app)
    # The test fails with the following line:
    socketio.init_app(app, message_queue='redis://pgsql-dev-vm:6379/', channel='foo_test')

    @app.route('/admin', methods = ['GET', 'POST'])
    def admin_page():
        socketio.emit('reboot', None)

        return 'Hello'

    return app

if __name__ == '__main__':
    app = create_app()
    socketio.run(app, host='0.0.0.0', port=5021)
