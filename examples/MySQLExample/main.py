import silbot
from CustomDBManager import MySQLDBManager

# Create a connection to the database
db = MySQLDBManager("localhost", "root", "password", "database")
db.installDB("silbotpy")

token = "12345:dsjfsodkjfodsos"  # Put bot token here
bot = silbot.botapi.BotApi(token, "HTML")
r, response = bot.getMe()
if response.ok is False:
    print("Error, wrong bot Token")
    exit()
else:
    print("Bot @" + r.username + " started")


def HandleUpdate(update: silbot.types.Update, bot: silbot.botapi.BotApi):
    db.updateConnection()
    db.fromUpdate(update)
    if update.message is not None:
        message = update.message
        chat = message.chat
        if message.text is not None:
            if message.text == "/start":
                bot.sendMessage(chat.id, "<b>Silbot MySQL Example</b>\n\nThis bot will count all text messages (excluding this bot's commands) sent in  a chat, send /count to check how many messages have been sent")
            elif message.text.startswith("/count"):
                bot.sendMessage(chat.id, "The number of text messages send in this chat is " + str(chat.db.count))
            else:
                messages = int(chat.db.count) + 1
                chat.setColumn("count", messages)


silbot.GetUpdatesLoop(bot, HandleUpdate)
