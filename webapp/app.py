"""
app.py — Porta Musical Cipher web demo
Flask serves a single page; all cipher logic runs in the browser via JS + abcjs.
"""

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True, port=5000)
