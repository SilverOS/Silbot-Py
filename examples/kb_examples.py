import silbot
from silbot.helper import InlineKBMarkup, inlineKBRow, inlineKBData, inlineKBUrl, replyKeyboard, replyKBRow, replyKBbutton

token = "12345:sadsfsdfsdfsd"  # Put bot token here
bot = silbot.botapi.BotApi(token, "HTML")

r, response = bot.getMe()

if not response.ok:
    print("Error, wrong bot Token")
    exit()
else:
    print("Bot @" + r.username + " started")


def updateH(update: silbot.types.Update, bot: silbot.botapi.BotApi):
    if update.message is not None:
        message = update.message
        chat = message.chat
        if message.text == "/start":
            kb = InlineKBMarkup(
                inlineKBRow(
                    inlineKBData("editMessageText + answerCallbackData", "/edit"),
                ),
                inlineKBRow(
                    inlineKBData("Reply Keyboard", "/reply")
                ),
                inlineKBRow(
                    inlineKBUrl("Documentation", "https://silbot.silveros.it"),
                    inlineKBUrl("GitHub", "https://github.com/SilverOS/Silbot-Py")
                ),
            )
            bot.sendMessage(chat.id, "This is a message with <b>inline keyboard</b>", kb)
        elif message.text == "Remove Keyboard":
            bot.sendMessage(chat.id, "Keyboard removed", silbot.types.ReplyKeyboardRemove({"remove_keyboard": True}))
    elif update.callback_query is not None:
        callback = update.callback_query
        chat = update.callback_query.user
        if callback.data == "/edit":
            bot.editMessageText("This is an edited message", chat.id, callback.message.message_id)
            bot.answerCallbackQuery(callback.id, "Alert", False)
        elif callback.data == "/reply":
            kb = replyKeyboard(
                replyKBRow(
                    replyKBbutton("/start"),
                    replyKBbutton("Remove Keyboard"),
                )
            )
            bot.deleteMessage(chat.id, callback.message.message_id)
            bot.sendMessage(chat.id, "Reply Keyboard", kb)


silbot.GetUpdatesLoop(bot, updateH)
