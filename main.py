import io
import imghdr
from flask import Flask, request, Response
from server.processing import image_processing, audio_processing
from flask_cors import CORS
import sys

sys.path.append("/home/Sk7/Documents/python/ai_project")

app = Flask(__name__)
# CORS(app)

@app.route("/")
def index():
    "Webpage"
    with open("server/homepage.html", "r", encoding="utf8") as file:
        return file.read()


@app.route("/upload", methods=["POST"])
def upload_file():
    if "file" not in request.files:
        return Response("No file part", status=400)

    file = request.files["file"]

    if file.filename == "":
        return Response("No selected file", status=400)

    if file:
        recieved = io.BytesIO(file.read())
        if imghdr.what(None, h=recieved.read()) == "png":
            recieved.seek(0)                    #yk why we need to do this
            a = image_processing(recieved, request.form["model"])
            return Response(a, 200)
        else:
            recieved.seek(0)
            a = audio_processing(recieved, request.form["model"])
            return Response(a, 200)

    return Response("Suffered an error!", status=500)


if __name__ == "__main__":
    app.run(debug=True)
