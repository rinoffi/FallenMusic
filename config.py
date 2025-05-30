from os import getenv

from dotenv import load_dotenv

load_dotenv()


API_ID = int(getenv("28015531"))
API_HASH = getenv("2ab4ba37fd5d9ebf1353328fc915ad28")

BOT_TOKEN = getenv("7277505434:AAErB4dH09Qq7EZWTp_anDdYsX4FkQUqhH8", None)
DURATION_LIMIT = int(getenv("90", "90"))

OWNER_ID = int(getenv("7874828505"))

PING_IMG = getenv("PING_IMG", "https://te.legra.ph/file/6f99c49bdb4679acad717.jpg")
START_IMG = getenv("START_IMG", "https://te.legra.ph/file/f8ba75bdbb9931cbc8229.jpg")

SESSION = getenv("SESSION", None)

SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/DevilsHeavenMF")
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/FallenAssociation")

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "1356469075").split()))


FAILED = "https://te.legra.ph/file/4c896584b592593c00aa8.jpg"
