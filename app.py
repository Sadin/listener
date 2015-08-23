from flask import Flask, render_template, request, redirect, url_for, abort
import redis
app = Flask(__name__, static_path='/static')

@app.route('/')
def index():
    return render_template('index.html', )

if __name__ == "__main__":
    app.run()
