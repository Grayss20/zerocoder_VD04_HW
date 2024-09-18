from flask import Flask, render_template
import time

app = Flask(__name__)

@app.route('/')
def current_time():
    return time.ctime()


if __name__ == '__main__':
    app.run()