from flask import Flask, redirect, url_for,  render_template
import os
app = Flask(__name__)


picture = os.path.join('static','photo')
app.config['UPLOAD_FOLDER'] = picture

@app.route("/")
def index():
    return render_template("index1.html")

@app.route("/product")
def product():
    offer = os.path.join(app.config['UPLOAD_FOLDER'], 'offer.jpg')
    return render_template("index.html", user_image = offer)

@app.route("/complain")
def complain():
    return render_template("index2.html")


if __name__ =="__main__":
    app.run(port=8888)
