from os import getenv

from dotenv import load_dotenv

load_dotenv()


API_ID = int(getenv("28015531"))
API_HASH = getenv("2ab4ba37fd5d9ebf1353328fc915ad28")

BOT_TOKEN = getenv("7277505434:AAErB4dH09Qq7EZWTp_anDdYsX4FkQUqhH8")
DURATION_LIMIT = int(getenv("100000", "90"))

OWNER_ID = int(getenv("7874828505"))

PING_IMG = getenv("https://te.legra.ph/file/6f99c49bdb4679acad717.jpg")
START_IMG = getenv("https://te.legra.ph/file/f8ba75bdbb9931cbc8229.jpg")

SESSION = getenv("SESSION")

SUPPORT_CHAT = getenv("https://t.me/+b7ZuDQ3sPdE3ZTll")
SUPPORT_CHANNEL = getenv("https://t.me/KHOLI_THIRUDAN_GROUP")

SUDO_USERS = list(map(int, getenv("SUDO_USERS").split()))


FAILED = "https://te.legra.ph/file/4c896584b592593c00aa8.jpg"
