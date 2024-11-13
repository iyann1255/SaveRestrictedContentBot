#Github.com/Vasusen-code

from pyrogram import Client

from telethon.sessions import StringSession
from telethon.sync import TelegramClient

from decouple import config
import logging, time, sys

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

# variables
API_ID = config("23765163", default=None, cast=int)
API_HASH = config("008d5313d9006539373c2513373778cd", default=None)
BOT_TOKEN = config("7249154151:AAG2_V_O3FcVexZUw4qsYWAnY-iKo6PpXnk", default=None)
SESSION = config("1BVtsOHwBuxB_9O541pVzRwZ-ch1e5xRN5yFdEuxzsDfttYwkAscMdPRurNuHYJU-6kKUXTysKlNV-63llzDKvu6qpP8AuLRXNLFZXRR7R_0Idq3Jw6reWbWzUlygd_SgwmS_fjBgaznXDiB1r3yCcW4hE3OahdsPjzdS3ocZPDCrxyDod9-JVsQuiZ3Otor5h6gj9mFWf8FrGNoLZEvqpBHXqOpoJRyKpO1Zpxsqk5pkLOUxBdPThAN8HMXwAxKlSRx2FD9pY9DeGSQ5fAD6jM24j70SqyEh5g9PTAGaEnUdmOPHY_Hh3JfEv73fbxvBsOWgMQk2nhug-A2fASdKJiOA3XwtNE4=", default=None)
FORCESUB = config("@", default=None)
AUTH = config(""6206131497, default=None, cast=int)

bot = TelegramClient('bot', API_ID, API_HASH).start(bot_token=BOT_TOKEN) 

userbot = Client("saverestricted", session_string=SESSION, api_hash=API_HASH, api_id=API_ID) 

try:
    userbot.start()
except BaseException:
    print("Userbot Error ! Have you added SESSION while deploying??")
    sys.exit(1)

Bot = Client(
    "SaveRestricted",
    bot_token=BOT_TOKEN,
    api_id=int(API_ID),
    api_hash=API_HASH
)    

try:
    Bot.start()
except Exception as e:
    print(e)
    sys.exit(1)
