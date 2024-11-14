# devggn
# Note if you are trying to deploy on vps then directly fill values in ("")

from os import getenv

API_ID = int(getenv("API_ID", "27692015"))
API_HASH = getenv("API_HASH", "25278a8394b5914ee1b8d6a6c79d572d")
BOT_TOKEN = getenv("BOT_TOKEN", "7568316298:AAH6TjD379wtsfVSn02qjBO7hBV35GnbRFs")
OWNER_ID = list(map(int, getenv("OWNER_ID", "6218454099").split()))
MONGO_DB = getenv("MONGO_DB", "mongodb+srv://Premium:aloksingh@cluster0.4ykpo.mongodb.net/?retryWrites=true&w=majority")
LOG_GROUP = getenv("LOG_GROUP", "-1002376972792")
CHANNEL_ID = int(getenv("CHANNEL_ID", "-1002308991006"))
