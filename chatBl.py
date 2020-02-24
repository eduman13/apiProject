import chatDl
from nltk.sentiment.vader import SentimentIntensityAnalyzer

def createChat(users):
    return chatDl.createChat(users)

def addUser(chat_id, user_id):
    return chatDl.addUser(chat_id, user_id)

def addMessage(chat_id, user_id, message):
    return chatDl.addMessage(chat_id, user_id, message)

def listMessages(chat_id):
    return chatDl.listMessages(chat_id)

def sentiments(chat_id):
    messages = chatDl.listMessages(chat_id)
    return analysisMessages(messages, "sentiments")

def analysisMessages(messages, function):
    sia = SentimentIntensityAnalyzer()
    if function == "sentiments":
        sentimientos = [sia.polarity_scores(i.get("message")) for i in messages]
        return list(zip(messages, sentimientos))
    if function == "recommender":
        sentimientos = [
            {
                "message": i,
                "sentiment": sia.polarity_scores(i)
            }
        for i in messages]
        return sentimientos

    if function == "messages":
        sentimientos = sia.polarity_scores(messages)
        return sentimientos