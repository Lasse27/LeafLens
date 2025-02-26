from flask import Flask, request, render_template
import os
from flaskwebgui import FlaskUI  # type: ignore
import cv2 as opencv

# Erstellen der Flask-App
app = Flask(__name__)
app.config["UPLOAD_FOLDER"] = os.path.join(
    os.path.dirname(os.path.dirname(__file__)), "DATA"
)


#


@app.route("/")
def index():
    """Zeigt die Hauptseite der Anwendung."""
    return render_template("index.html")


#


@app.route("/upload", methods=["POST"])
def upload_file():
    if "file" not in request.files:
        return render_template("index.html")

    file = request.files["file"]
    if file.filename == "":
        return render_template("index.html")

    if file:
        filepath = os.path.join(app.config["UPLOAD_FOLDER"], file.filename)
        if not os.path.exists(os.path.dirname(filepath)):
            os.makedirs(os.path.dirname(filepath))
        file.save(filepath)

        # Bildverarbeitung mit OpenCV
        result_text = process_image(filepath)

        return render_template("index.html", result=result_text)


#


def process_image(image_path):
    img = opencv.imread(image_path)
    gray = opencv.cvtColor(img, opencv.COLOR_BGR2GRAY)

    # Beispiel: Anzahl weißer Pixel zählen
    white_pixels = opencv.countNonZero(gray)
    return f"Anzahl der weißen Pixel im Bild: {white_pixels}"


#


def start() -> None:
    """Starts the applications ui."""
    FlaskUI(
        app=app, port=80, fullscreen=False, width=1280, height=800, server="flask"
    ).run()


#


if __name__ == "__main__":
    start()
