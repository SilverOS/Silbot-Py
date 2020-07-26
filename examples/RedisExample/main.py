import silbot
from CustomDBManager import RedisDBManager
import redis

token = "1180749940:AAFQh2WOLqM5_4Y3anFL_jge3LB0RBtp8R8"  # Put bot token here
bot = silbot.botapi.BotApi(token, "HTML")
r, response = bot.getMe()
if response.ok is False:
    print("Error, wrong bot Token")
    exit()
else:
    print("Bot @" + r.username + " started")

connection = redis.StrictRedis(host='127.0.0.1', port=6379, password='', db=1)  # Create Redis connection
db = RedisDBManager(connection)


def HandleUpdate(update: silbot.types.Update, bot: silbot.botapi.BotApi):
    db.fromUpdate(update)
    if hasattr(update, "message"):
        message = update.message
        chat = message.chat
        if hasattr(message, "text"):
            if message.text == "/start":
                bot.sendMessage(chat.id, "<b>Silbot Redis Example</b>\n\nThis bot will count all text messages (excluding this bot's commands) sent in  a chat, send /count to check how many messages have been sent")
            elif message.text.startswith("/count"):
                bot.sendMessage(chat.id, "The number of text messages send in this chat is " + chat.db.count)
            else:
                messages = int(chat.db.count) + 1
                chat.setColumn("count", messages)


silbot.GetUpdatesLoop(bot, HandleUpdate)
