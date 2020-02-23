from pymongo import MongoClient
import commons as com
import error

client = MongoClient("mongodb://localhost/apiProject")
db = client.get_database()

def existsByUserName(username):
    query = {"userName": username}
    projection = {"_id": 0, "userName": 1}
    result = db["user"].find(query, projection)
    if len(list(result)) == 0:
        return True
    else:
        raise error.ExistsUserName()

def existsById(user_id):
    query = {"user_id": user_id}
    result = db["user"].find(query)
    if result.count() == 1:
        return True
    else:
        raise error.NoExist()

def createUser(username):
    existsByUserName(username)
    maximo = com.idAutoIncremental(db, "user")
    db["user"].insert(
        {
            "user_id": maximo,
            "userName": username
        }
    )
    return maximo

def userInfo(*users):
    projection = {"_id": 0, "user_id": 1, "userName": 1}
    usersInfo = [list(db["user"].find({"user_id": i}, projection)) for i in users]
    return [e for i in usersInfo for e in i]

def listMenssagesUser(user_id):
    info = com.toInt(user_id)
    result = db["chat"].aggregate([
        {
            "$project": {
                "messages": {
                    "$filter": {
                        "input": "$messages",
                        "as": "messages",
                        "cond": {
                            "$eq": [
                                "$$messages.user_id", info[0]
                            ]
                        }
                    }
                }
            }
        },
        {
            "$project": {
                "_id": 0,
                "messages.message": 1
            }
        }
    ])
    mensaggesUser = []
    for i in list(result):
        mensagges = i.get("messages", 0)
        if mensagges == 0:
            pass
        else:
            mensaggesUser.append([i.get("message") for i in mensagges])
    return [e for i in mensaggesUser for e in i]

def listUsers():
    result = db["user"].find({}, {"_id": 0, "user_id": 1})
    return [i.get("user_id") for i in list(result)]
