from os import environ 

class Config:
    API_ID = environ.get("API_ID", "22911014")
    API_HASH = environ.get("API_HASH", "bdf50bb3057917988dff629a18f8bdb0")
    BOT_TOKEN = environ.get("BOT_TOKEN", "8293483747:AAH-6jZxL4K45OwqMVGVy6kGU7oWamzZ_fk") 
    BOT_SESSION = environ.get("BOT_SESSION", "bot") 
    DATABASE_URI = environ.get("DATABASE", "mongodb+srv://anonymousguywas:12345Trials@cluster0.t4nmrtp.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
    DATABASE_NAME = environ.get("DATABASE_NAME", "forward-bot")
    BOT_OWNER_ID = [int(id) for id in environ.get("BOT_OWNER_ID", '5962658076').split()]

class temp(object): 
    lock = {}
    CANCEL = {}
    forwardings = 0
    BANNED_USERS = []
    IS_FRWD_CHAT = []
    
