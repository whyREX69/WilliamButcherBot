from os import environ

from dotenv import load_dotenv

load_dotenv("config.env")

HEROKU = bool(
    environ.get("DYNO")
)  # NOTE Make it false if you're not deploying on heroku or docker.

if HEROKU:

    BOT_TOKEN = environ.get("BOT_TOKEN", 5189246830:AAEVwFNM_4jtpYSrAw0ntw8oFfXJy0kYNsY)
    API_ID = int(environ.get("API_ID", 12388301))
    API_HASH = environ.get("API_HASH", "f08f8caff5aac56229e9f02bd67e48ea")
    SESSION_STRING = environ.get("SESSION_STRING", BQC9B80AETUMNFvJCPlO-aVaIF1qDttqGlFzvUn-7d9dSOVtLV9zyx41EzJND5v3sRGYRzweqqe4PykqWcJehmL0HECodWSGJ39htm3hSDuB1RNqAIryMhJvhgjGVyJBHQMF4X4QCAK2hlWi0r4zeGDlbYG2DKYFrdu8gyJMwYwzhCODwfZKWSCly-q6_jHDgFbaTmiX-QHykoCNYd_cg55N44wioAeMaR_VbLi2TD57y9XXlllpzJ-PqEcB1iy12rERzyjTzgNlGtA6Cd7twH3W4xLxQhDOKzNlWqby9PVyso6tjkRKMXa29MZs31W9pFJp6ata1AyQujbnA2y_k6UdvVdZKwAAAAE0XDV5AA)
    USERBOT_PREFIX = environ.get("USERBOT_PREFIX", ".")
    SUDO_USERS_ID = [int(x) for x in environ.get("SUDO_USERS_ID", "1943696216").split()]
    LOG_GROUP_ID = int(environ.get("LOG_GROUP_ID", -1001706596784))
    GBAN_LOG_GROUP_ID = int(environ.get("GBAN_LOG_GROUP_ID", -1001706596784))
    MESSAGE_DUMP_CHAT = int(environ.get("MESSAGE_DUMP_CHAT", -1001706596784))
    WELCOME_DELAY_KICK_SEC = int(environ.get("WELCOME_DELAY_KICK_SEC", 300))
    MONGO_URL = environ.get("MONGO_URL", mongodb+srv://vcbot:vcbot@cluster0.dnn8y.mongodb.net/myFirstDatabase?retryWrites=true&w=majority)
    ARQ_API_URL = environ.get("ARQ_API_URL", https://arq.hamker.in)
    ARQ_API_KEY = environ.get("ARQ_API_KEY", CENWFE-IQFMCB-VGTHJX-SNQRXR-ARQ)
    LOG_MENTIONS = bool(int(environ.get("LOG_MENTIONS", 1)))
    RSS_DELAY = int(environ.get("RSS_DELAY", 300))
    PM_PERMIT = bool(int(environ.get("PM_PERMIT", 1)))
else:
   

BOT_TOKEN=5189246830:AAEVwFNM_4jtpYSrAw0ntw8oFfXJy0kYNsY # Get it from @botfather

API_ID=12388301

API_HASH=f08f8caff5aac56229e9f02bd67e48ea

SESSION_STRING=BQC9B80AETUMNFvJCPlO-aVaIF1qDttqGlFzvUn-7d9dSOVtLV9zyx41EzJND5v3sRGYRzweqqe4PykqWcJehmL0HECodWSGJ39htm3hSDuB1RNqAIryMhJvhgjGVyJBHQMF4X4QCAK2hlWi0r4zeGDlbYG2DKYFrdu8gyJMwYwzhCODwfZKWSCly-q6_jHDgFbaTmiX-QHykoCNYd_cg55N44wioAeMaR_VbLi2TD57y9XXlllpzJ-PqEcB1iy12rERzyjTzgNlGtA6Cd7twH3W4xLxQhDOKzNlWqby9PVyso6tjkRKMXa29MZs31W9pFJp6ata1AyQujbnA2y_k6UdvVdZKwAAAAE0XDV5AA # Check Readme to generate sessions

USERBOT_PREFIX=/

SUDO_USERS_ID=1943696216 # Sudo users have full access to everythin, don't trust anyone

LOG_GROUP_ID=-1001706596784

GBAN_LOG_GROUP_ID=-1001706596784

MESSAGE_DUMP_CHAT=-1001706596784

WELCOME_DELAY_KICK_SEC=300 # Edit if u want

MONGO_URL=mongodb+srv://vcbot:vcbot@cluster0.dnn8y.mongodb.net/myFirstDatabase?retryWrites=true&w=majority

ARQ_API_URL=https://arq.hamker.in # Leave it like this

ARQ_API_KEY=CENWFE-IQFMCB-VGTHJX-SNQRXR-ARQ # Get it from @ARQRobot

LOG_MENTIONS=0 # Make it 1 if you want to enable it

RSS_DELAY=300 # In seconds

PM_PERMIT=1 # fill 0 to disable it
