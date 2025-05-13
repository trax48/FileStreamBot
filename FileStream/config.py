from os import environ as env
from dotenv import load_dotenv

load_dotenv()

class Telegram:
    API_ID = int(env.get("API_ID", '23790461'))
    API_HASH = str(env.get("API_HASH", '2d0a7fb85f06246e93948bf7afc05fb3'))
    BOT_TOKEN = str(env.get("BOT_TOKEN", '8125069376:AAGS-8bKxsZb3kOsxufp3I3D2nsbFTQz__w'))
    OWNER_ID = int(env.get('OWNER_ID', '929048904'))
    WORKERS = int(env.get("WORKERS", "6"))  # 6 workers = 6 commands at once
    DATABASE_URL = str(env.get('DATABASE_URL', 'mongodb+srv://Rax:amit7001@cluster0.cintttk.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0'))
    UPDATES_CHANNEL = str(env.get('UPDATES_CHANNEL', "Ace_Files"))
    SESSION_NAME = str(env.get('SESSION_NAME', 'FileStream'))
    FORCE_SUB_ID = env.get('FORCE_SUB_ID', None)
    FORCE_SUB = env.get('FORCE_UPDATES_CHANNEL', False)
    FORCE_SUB = True if str(FORCE_SUB).lower() == "true" else False
    SLEEP_THRESHOLD = int(env.get("SLEEP_THRESHOLD", "60"))
    FILE_PIC = env.get('FILE_PIC', "https://i.ibb.co/DDbFRQBP/IMG-20250430-WA0267.jpg")
    START_PIC = env.get('START_PIC', "https://i.ibb.co/DDbFRQBP/IMG-20250430-WA0267.jpg")
    VERIFY_PIC = env.get('VERIFY_PIC', "https://i.ibb.co/DDbFRQBP/IMG-20250430-WA0267.jpg")
    MULTI_CLIENT = False
    FLOG_CHANNEL = int(env.get("FLOG_CHANNEL", None))   # Logs channel for file logs
    ULOG_CHANNEL = int(env.get("ULOG_CHANNEL", None))   # Logs channel for user logs
    MODE = env.get("MODE", "primary")
    SECONDARY = True if MODE.lower() == "secondary" else False
    AUTH_USERS = list(set(int(x) for x in str(env.get("AUTH_USERS", "")).split()))

class Server:
    PORT = int(env.get("PORT", 8080))
    BIND_ADDRESS = str(env.get("BIND_ADDRESS", "0.0.0.0"))
    PING_INTERVAL = int(env.get("PING_INTERVAL", "1200"))
    HAS_SSL = str(env.get("HAS_SSL", "0").lower()) in ("1", "true", "t", "yes", "y")
    NO_PORT = str(env.get("NO_PORT", "0").lower()) in ("1", "true", "t", "yes", "y")
    FQDN = str(env.get("FQDN", BIND_ADDRESS))
    URL = "http{}://{}{}/".format(
        "s" if HAS_SSL else "", FQDN, "" if NO_PORT else ":" + str(PORT)
    )



