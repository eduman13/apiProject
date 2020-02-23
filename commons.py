def idAutoIncremental(db, collection):
    projection = {f"{collection}_id": 1, "_id": 0}
    result = db[collection].find({}, projection)
    if result.count() == 0:
        return 1
    maximo = max([i[f"{collection}_id"] for i in result])
    return maximo + 1

def toInt(*ints):
    return [int(i) for i in ints]

