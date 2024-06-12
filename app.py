from flask import Flask, request, jsonify, send_file
import json
def create_app():
    return app
app = Flask(__name__)

admincode = "1234"
def clear_chat():
    clearc = open("globalchat.txt", "w")
    clearc.write("")
    clearc.close()
    return "chat cleared"
@app.route('/')
def main():
    index = open("index.html", "rb")
    return index.read()
@app.route('/chat/', methods=['GET', 'POST'])
def chat():
    sendm = open("globalchat.txt", "a")
    if request.method == 'POST':
        message = request.form['message']
        username = request.form['username']
        sendm = open("globalchat.txt", "a")
        sendm.write("<" + username + ">:" + message + "\n") 
    return open("chat.html", "rb")
@app.route('/admin/', methods=['GET', 'POST'])
def login():
    if request.method == "POST":
        username = request.form['username']
        password = request.form['password']
        if username == "admin" and password == admincode:
            login = True
            return open("admin-panel.html", "rb")
        else:
            login = False
            print("login Failed at ip, " + request.remote_addr)
            return "login failed"
    else:
        return open("admin-login.html", "rb")


@app.route('/test/', methods=['get'])
def test():
    return open("test.html", "rb")
@app.route('/globalchat/', methods=['get'])
def globalchat():
    return open("globalchat.txt", "r")
@app.route('/chat.html', methods=['GET', 'POST'])
def message():
    sendm = open("globalchat.txt", "a")
    if request.method == 'POST':
        message = request.form['message']
        username = request.form['username']
        sendm = open("globalchat.txt", "a")
        sendm.write("<" + username + ">:" + message + "\n") 
    return open("chat.html", "rb")
@app.route('/index.css/', methods=['GET'])
def css():
    return send_file("index.css")
@app.route('/api/clear_chat/', methods=['GET'])
def clear_chat_api():
    api_key = request.args.get("api-key")
    if api_key == None:
        return {"response" : "no api key"}
    elif api_key == admincode:
        clear_chat()
        return {"response" : "chat cleared"}
    else:
        return {"response" : "Invalid api key"}, 403 
@app.route('/api/send_msg/', methods=['POST', 'GET'])
def send_msg():
    if request.method == 'POST':
        rawdata = request.get_json()
        data = json.loads(rawdata)
        message = data['message']
        username = data['username']
        print(data)
        sendm = open("globalchat.txt", "a")
        sendm.write("<" + username + ">:" + message + "\n")
        return {"response" : "message sent"}
    else:
        return 'invalid method', 400
@app.route('/api/get_msgs/', methods=["GET"])
def get_msgs():
    return send_file("globalchat.txt")
    
    
if __name__ == '__main__':
    app.run(debug=True , port=5066)