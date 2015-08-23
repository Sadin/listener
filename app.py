from flask import Flask, render_template, request, redirect, url_for, abort
import redis
app = Flask(__name__, static_path='/static')

r = redis.StrictRedis(host='localhost', port=6379, db=0)

r.set('foo', 'bar')
redis_response = r.get('foo').decode('utf-8')

@app.route('/')
def index():

    return render_template('index.html', payload=redis_response )

if __name__ == '__main__':
    app.run(debug=True)
