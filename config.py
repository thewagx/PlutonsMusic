from os import getenv

from dotenv import load_dotenv

load_dotenv()


API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")

BOT_TOKEN = getenv("BOT_TOKEN", None)
MONGO_URL = getenv("MONGO_URL", "mongodb+srv://userbot:userbot@cluster0.yyijp36.mongodb.net/?retryWrites=true&w=majority")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "90"))

OWNER_ID = int(getenv("OWNER_ID"))

PING_IMG = getenv("PING_IMG", "https://telegra.ph/file/2030bea6c41b37ec65a8d.jpg")
START_IMG = getenv("START_IMG", "https://telegra.ph/file/b30b497dd011204136373.jpg")

SESSION = getenv("SESSION", None)

SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/destekgroup")
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/PlutoKanal")
PLAYLIST = getenv("PLAYLIST", "https://t.me/PlutoFm")

PLAYLIST_ID = int(getenv("PLAYLIST_ID", ""))


FAILED = "https://te.legra.ph/file/4c896584b592593c00aa8.jpg"
