__version__ = '0.1.1'

# Core

# Local
from onde_dar_sangue.grab_data import GrabData

# Third-party
from flask import Flask


def start_app():
    app = Flask(__name__)

    @app.route('/l')
    def locals():
        grab = GrabData("http://dador.pt/onde-dar/lista-de-recolhas")
        return grab.get_data()

    return app
