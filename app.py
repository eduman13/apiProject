from flask import Flask
from flask import request
import os
import userBl
import chatBl

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World'

@app.route("/user/create/<userName>")
def createUser(userName):
    return {
        "user_id": userBl.createUser(userName)
    }

@app.route("/chat/create/")
def createChat():
    users = request.get_json(force=True).get("users")
    return {
        "chat_id": chatBl.createChat(users)
    }

@app.route("/chat/<chat_id>/adduser")
def addUser(chat_id):
    user_id = request.args.get("userr_id")
    return {
        "chat_id": chatBl.addUser(chat_id, user_id)
    }

@app.route("/chat/<chat_id>/addmessage")
def addMessage(chat_id):
    user_id = request.args.get("user_id")
    message = request.get_json(force=True).get("message")
    return {
        "message": chatBl.addMessage(chat_id, user_id, message)
    }

@app.route("/chat/<chat_id>/list")
def listMessages(chat_id):
    return {
        f"messages_from_chat_{chat_id}": chatBl.listMessages(chat_id)
    }

@app.route("/chat/<chat_id>/sentiment")
def sentiment(chat_id):
    sentimientos = chatBl.sentiments(chat_id)
    respuesta = [{
        "message": i[0],
        "sentiment": i[1]
    } for i in sentimientos]
    return {
        "analysis": [i for i in respuesta]
    }

@app.route("/user/recommend")
def recommender():
    message = request.get_json(force=True).get("messages")
    return userBl.recommender(message)

@app.errorhandler(500)
def handleException(e):
    original = getattr(e, "original_exception", None)
    return {
        "error": str(original)
    }, 400

if __name__ == '__main__':
    app.run("0.0.0.0", os.getenv("PORT"))
