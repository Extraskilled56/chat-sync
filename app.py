from flask import Flask, request


app = Flask(__name__)

@app.route('/')
def main():
    index = open("index.html", "rb")
    return index.read()
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        return open("chat.html", "rb")
    return open("login.html", "rb")
@app.route('/chat', methods=['get'])
def chat():
    return open("chat.html", "rb")

if __name__ == '__main__':
    app.run()
