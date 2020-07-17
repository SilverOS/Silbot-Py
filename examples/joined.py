import silbot
from silbot.helper import *

"""
This is an example of how to use new methods added with silbot 1.1
This is a simple bot that will check if a user is in a channel or is admin of that channel
"""
token = "123234234:fdsiojfiosdjf"  # Put bot token here
channelid = -1001086416281  # Change the channel ID, the but must be admin of the channel

bot = silbot.botapi.BotApi(token, "HTML")

r, response = bot.getMe()

if not response.ok:
    print("Error, wrong bot Token")
    exit()
else:
    print("Bot @" + r.username + " started")


def updateH(update: silbot.types.Update, bot: silbot.botapi.BotApi):
    if hasattr(update, "message"):
        message = update.message
        chat = message.chat

        if message.text == "/start":
            kb = InlineKBMarkup(
                inlineKBRow(
                    inlineKBData("Join Check", "/join"),
                    inlineKBData("Admin Check", "/admin")
                )
            )
            bot.sendMessage(chat.id,
                            "<b>Silbot Py Example</b>\n\nClick the button to check if you are admin/member of the channel defined in the config",
                            kb)

    elif hasattr(update, "callback_query"):

        callback = update.callback_query
        user = callback.user

        if callback.data == "/join":
            r = user.isMember(bot, channelid)
            if r:
                callback.answer(bot, "You joined the channel")
            elif not r:
                callback.answer(bot, "You have not joined the channel")
        elif callback.data == "/admin":
            r = user.isAdmin(bot, channelid)
            if r:
                callback.answer(bot, "You are an admin of the channel")
            elif not r:
                callback.answer(bot, "You are not an admin of the channel")


silbot.startpool(bot, updateH)
