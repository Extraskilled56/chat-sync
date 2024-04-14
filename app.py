from flask import Flask, request


app = Flask(__name__)

@app.route('/')
def main():
    index = open("index.html", "rb")
    return index.read()
@app.route('/chat', methods=['GET', 'POST'])
def chat():
    sendm = open("globalchat.txt", "a")
    if request.method == 'POST':
        message = request.form['message']
        username = request.form['username']
        sendm = open("globalchat.txt", "a")
        sendm.write("<" + username + ">:" + message + "\n") 
    return open("chat.html", "rb")
@app.route('/test', methods=['get'])
def test():
    return open("test.html", "rb")
@app.route('/globalchat', methods=['get'])
def globalchat():
    return open("globalchat.txt", "r")
@app.route('/chat.html', methods=['GET', 'POST'])
def login():
    sendm = open("globalchat.txt", "a")
    if request.method == 'POST':
        message = request.form['message']
        username = request.form['username']
        sendm = open("globalchat.txt", "a")
        sendm.write("<" + username + ">:" + message + "\n") 
    return open("chat.html", "rb")
if __name__ == '__main__':
    app.run(debug=False)
