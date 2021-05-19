#!/usr/bin/env python
from flask import Flask, json, Response, render_template
import time
from numpy import random
app = Flask(__name__)

def sse_encode(obj, id=None):
    return "data: %s\n\n" % json.dumps(obj)

counter = 0
def eventgen():
    global counter
    counter += 1    
    local_id = counter
    msg_count = 0
    while True:
        msg_count += 1
        data = {
        'msg': msg_count, 
        'airspeed': random.random(), 
        'local_id': local_id}
        data = json.dumps(data)
        yield 'data: ' + data + '\n\n'
        time.sleep(0.02)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/stream/', methods=['GET', 'POST'])
def stream():
    return Response(eventgen(), mimetype="text/event-stream")

if __name__ == '__main__':
    app.run(host="0.0.0.0")