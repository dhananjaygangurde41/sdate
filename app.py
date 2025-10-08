from flask import Flask, render_template
import os
from datetime import datetime

app = Flask(__name__)

PORT = os.environ.get('PORT',9000)

@app.route("/")
def index():
    env = dict(os.environ)

    return render_template('index.html',env = env)

@app.route("/api")
def date():
    now =  datetime.now()
    return render_template('date.html',time = now)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=PORT, debug=True)

