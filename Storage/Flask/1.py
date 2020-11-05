
from flask import Flask, render_template
app = Flask(__name__)
@app.route("/")
def video_game():
    return render_template("index.html")