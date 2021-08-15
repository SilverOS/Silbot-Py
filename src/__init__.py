"""
[![PyPI](https://img.shields.io/pypi/v/silbot.svg)](https://pypi.python.org/pypi/silbot)
[![Telegram Channel](https://img.shields.io/badge/telegram_channel-@silverosp-0d86d7.svg?style=flat)](https://t.me/SilverOSp)

This is a simple framework for [telegram bot API](https://core.telegram.org/bots/api).

- [__Examples__](https://github.com/SilverOS/Silbot-Py/tree/master/examples)
- [__Github__](https://github.com/SilverOS/Silbot-Py)
- [__Download__](https://github.com/SilverOS/Silbot-Py/archive/1.4.2.zip)

"""
from silbot import botapi, update


def GetUpdatesLoop(bot: botapi.BotApi, handlefunc, onUpdate=None, on_getUpdates=None):
    """ This is a builtin function to handle updates with getUpdates

    **Args:**

    - bot (`botApi`): botApi object
    - handlefunc (`function`): function **defined by the user**, that function has to accept there arguments:
        - `update` (`silbot.types.update`) : The object that rapresents the update
        - `bot` (`silbot.botapi.BotApi`) : The botApi object for that bot,
    - onUpdate (`function`, optional): a function that is called every update (non async)
    - on_getUpdates (`function`, optional): a function that is called everytime a getUpdates call is done (non async)
    If this is not clear, check the examples
    """
    offset = -1
    while True:
        response = bot.getUpdates(offset)[1]
        if on_getUpdates is not None:
            on_getUpdates()
        js = response.decoded
        if js["ok"]:
            if len(js["result"]) > 0:
                for up in js["result"]:
                    if onUpdate is not None:
                        onUpdate()
                    offset = up["update_id"] + 1
                    thread = update.update(up, bot, handlefunc)
                    thread.start()
        else:
            continue
