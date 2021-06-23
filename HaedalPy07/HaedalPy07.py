from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def hello():
    return '컴퓨터학부 2021111849 송혜경입니다!'


@app.route('/me/')
def me():
    return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)