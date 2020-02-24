class ExistsUserName(Exception):
    def __init__(self):
        Exception.__init__(self, "El usuario ya existe")

class NoExistUser(Exception):
    def __init__(self):
        Exception.__init__(self, "El usuario no existe")

class NoExistChat(Exception):
    def __init__(self):
        Exception.__init__(self, "El chat no existe")