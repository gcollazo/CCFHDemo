import os
import time

from flask import Flask
from flask import render_template

from store import redis

app = Flask(__name__)
app.debug = True


@app.route("/")
def hello():
    redis.rpush('thelist',
        'Hello: {} - {}'.format(os.uname()[1], time.time()))
    the_list = redis.lrange('thelist', 0, -1)
    return render_template('index.html', the_list=the_list)

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
