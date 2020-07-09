from silbot import update
from silbot import botapi
import json


def startpool(bot : botapi.botApi,handlefunc):
    """ This is a builtin function to handle updates with getUpdates

    **Args:**

    - bot (`botApi`): botApi object
    - handlefunc (`function`): function **defined by the user**, that function has to accept there arguments:
        - `update` (`silbot.types.update`) : The object that rapresents the update
        - `bot` (`silbot.botapi.botApi`) : The botApi object for that bot,
    If this is not clear, check the examples
    """
    offset = -1
    while True:
        response = bot.getUpdates(offset)[1]
        js = response.decoded
        if js["ok"]:
            if len(js["result"]) > 0:
                for up in js["result"]:
                    offset = up["update_id"]+1
                    thread = update.update(up,bot,handlefunc)
                    thread.start()
        else :
            continue
