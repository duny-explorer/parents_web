from flask import render_template, request, session
from DBManager import *


@app.route('/', methods=["GET"])
def main():
    return render_template('13.html')


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
