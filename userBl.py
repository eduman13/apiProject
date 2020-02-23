import pandas as pd
from scipy.spatial.distance import pdist, squareform
import userDl
import chatBl

def createUser(username):
    return userDl.createUser(username)

def recommender(message):
    users = userDl.listUsers()
    userMessages = list(zip([userDl.userInfo(i) for i in users], [userDl.listMenssagesUser(i) for i in users]))
    allMessages = [
        {
            "user_id": i[0][0].get("user_id"),
            "userName": i[0][0].get("userName"),
            "messages": i[1]

        }
    for i in userMessages]
    sentimientos = []
    for i in allMessages:
        messages = i.get("messages")
        if len(messages) > 0:
            sentimientos.append(
                {
                 "user": i.get("userName"),
                 "analysis": chatBl.analysisMessages(messages, "recommender")
                })
    stats = analysisStats(sentimientos)
    usersRecommender = {"users": [i for i in recomendationSystem(stats, message)]}
    return usersRecommender

def analysisStats(sentimientos):
    neg = 0
    neu = 0
    pos = 0
    compound = 0
    means = []
    for i in sentimientos:
        user = i.get("user")
        for e in i.get("analysis"):
            sentiment = e.get("sentiment")
            neg += sentiment.get("neg")
            neu += sentiment.get("neu")
            pos += sentiment.get("pos")
            compound += sentiment.get("compound")
        mean = {
            "user": user,
            "neg": neg,
            "neu": neu,
            "pos": pos,
            "compound": compound
        }
        neg = 0
        neu = 0
        pos = 0
        compound = 0
        means.append(mean)
    for i in means:
        messages = [len(e.get("analysis")) for e in sentimientos if e.get("user") == i["user"]][0]
        neg = i.get("neg")
        i["neg"] = neg / messages
        pos = i.get("pos")
        i["pos"] = pos / messages
        neu = i.get("neu")
        i["neu"] = neu / messages
        compound = i.get("compound")
        i["compound"] = compound / messages
    return means

def recomendationSystem(stats, message):
    data = pd.DataFrame(stats)
    data.set_index("user", inplace=True)
    newAnalysis = chatBl.analysisMessages(message, "messages")
    newUser = pd.DataFrame([{
        "user": "newUser",
        "neg": newAnalysis["neg"],
        "neu": newAnalysis["neu"],
        "pos": newAnalysis["pos"],
        "compound": newAnalysis["compound"]
    }])
    newData = pd.DataFrame(newUser)
    newData.set_index("user", inplace=True)
    data = data.append(newData)
    distance = pd.DataFrame(squareform(pdist(data, "euclidean")), columns=data.index,
                            index=data.index)
    distance = 1 / (1 + distance)
    return distance["newUser"].sort_values(ascending=False)[1:].head(3).index.tolist()


