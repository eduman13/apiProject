import datetime
import commons as com
import userDl
import error
from config import db

db = db

def existsChatById(chat_id):
    query = {"chat_id": chat_id}
    result = db["chat"].find(query)
    if result.count() == 1:
        return True
    else:
        raise error.NoExistChat()

def createChat(users):
    maximo = com.idAutoIncremental(db, "chat")
    usersInsert = userDl.userInfo(*users)
    print(usersInsert)
    db["chat"].insert(
        {
            "chat_id": maximo,
            "users": [i for i in usersInsert]
        }
    )
    return maximo

def addUser(chat_id, user_id):
    info = com.toInt(chat_id, user_id)
    userDl.existsById(info[1])
    existsChatById(info[0])
    result = db["user"].find({"user_id": user_id})
    userName = list(result)[0]["userName"]
    db["chat"].update(
        {
            "chat_id": info[0]
        },
        {
            "$push": {
                "users": {
                    "user_id": info[1],
                    "userName": userName
                }
            }
        }
    )
    return info[0]

def addMessage(chat_id, user_id, message):
    info = com.toInt(chat_id, user_id)
    existsChatById(info[0])
    userDl.existsById(info[1])
    db["chat"].update(
        {
            "chat_id": info[0]
        },
        {
            "$push": {
                "messages": {
                    "user_id": info[1],
                    "userName": userDl.userInfo(info[1])[0].get("userName"),
                    "message": message,
                    "time": datetime.datetime.now()
                }
            }
        }
    )
    return message

def listMessages(chat_id):
    info = com.toInt(chat_id)
    existsChatById(info[0])
    projection = {"_id": 0, "messages.message": 1, "messages.userName": 1}
    result = db["chat"].find(
        {
            "chat_id": info[0]
        }
    , projection)
    return [
        {
            "message": i.get("message"),
            "userName": i.get("userName")

         }
        for i in list(result)[0].get("messages")]