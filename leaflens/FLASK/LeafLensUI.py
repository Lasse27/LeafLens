from flask import Flask, render_template
from flaskwebgui import FlaskUI  # type: ignore


#
#

# Erstellen der Flask-App
app = Flask(__name__)

#
#


@app.route("/")
def index():
    """Zeigt die Hauptseite der Anwendung."""
    return render_template("index.html")


#
#


def start() -> None:
    """Starts the applications ui."""
    FlaskUI(
        app=app, port=80, fullscreen=False, width=1280, height=800, server="flask"
    ).run()


#
#

if __name__ == "__main__":
    start()