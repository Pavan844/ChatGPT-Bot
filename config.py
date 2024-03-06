import re
from os import getenv, environ

id_pattern = re.compile(r'^.\d+$')
def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default

API_ID = int(environ.get("API_ID", "26009823"))
API_HASH = environ.get("API_HASH", "e545fc56028ee9404ef5b5bec64503ca")
BOT_TOKEN = environ.get("BOT_TOKEN", "7028805440:AAG0FOMfbFQt2FLtApKKP60KVxmKzFS_DTQ")
LOG_CHANNEL = int(environ.get("LOG_CHANNEL", "2061267081"))
ADMINS = int(environ.get("ADMINS", "5289659053,6059507751"))
DB_URI = environ.get("DB_URI", "mongodb+srv://domedi9438:<password>@cluster0.edbujoi.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
DB_NAME = environ.get("DB_NAME", "chatgptvjbot")
OPENAI_API = environ.get("OPENAI_API", "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")
AI = is_enabled((environ.get("AI","True")), False)
