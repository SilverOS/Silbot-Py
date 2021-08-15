"""
## Here there are some functions that can be useful
"""
import json

from silbot import types


def setBvar(value):
    """If `value` is a dict returns a generic_json object, otherwise it returns the value

    - - - - -
    **Args**:

    - `value` (any type): value to assing

    **Returns**
    - `generic_json` if value is a dict, otherwise it returns the value
    """
    if type(value) == dict:
        return Generic_Json(value)
    else:
        return value


class Generic_Json:
    """
    Converts a `dict` into an objects where keys are attributes, ex. self.key = value
    """

    def __init__(self, d):
        """Creates a generic_json objects

        Sets attributes and creates new generic_json objects from dicts
        - - - - -
        **Args**:

        - `d` (`dict`): dictionary to convert
        """
        self.d = d
        for index, value in self.d.items():
            if type(index) == str:
                if type(value) == dict:
                    setattr(self, index, Generic_Json(value))
                else:
                    setattr(self, index, value)


def toDict(obj, dump=False):
    """Converts silbot.types Objects into dictionary, the main utility of this function is internal

    If `obj` is a silbot object, this function turns it into a dict, else returns it
    If `dump` is true, it returns the json encoded value if `obj` is an object, a list or a dict
    - - - - -
    **Args**:

    - `obj` (`silbot.types` object or any value): object to turn into a dict
    - `dump` (`bool`): if the result should be json encoded

    **Returns**
    - `obj` if value is not a silbot object or a list or a dict
    - `dict` if the value given was already a dict or it was a silbot.types object
    - `json string` if `dump` is `True`
    """
    dictionary = {}
    attributes = dir(obj)
    if obj.__class__.__module__ == "builtins":
        if type(obj) == dict or type(obj) == list:
            if dump:
                return json.dumps(obj)
            else:
                return obj
        else:
            return obj
    for attribute in attributes:
        if attribute.startswith("__") or attribute == "dict":
            continue
        else:
            value = getattr(obj, attribute, None)
            if value is None or str(type(value)) == "<class 'method'>":
                continue
            if type(value) == list:
                dictionary[attribute] = dictList(value)
            elif value.__class__.__module__ == "silbot.types":
                dictionary[attribute] = toDict(value)
            else:
                dictionary[attribute] = value
    if dump:
        return json.dumps(dictionary)
    else:
        return dictionary


def dictList(oldlist):
    """Converts lists of silbot.types Objects into list of dictionaries, the main utility of this function is internal

    - - - - -
    **Args**:

    - `l` (`list`): listo of objects to convert

    **Returns**
    - `list` of decoded objects
    """
    newlist = list()
    for i in oldlist:
        if type(i) == list:
            newlist.append(dictList(i))
        elif i.__class__.__module__ == "silbot.types":
            newlist.append(toDict(i))
        else:
            newlist.append(i)
    return newlist


def inlineKBData(text, callback_data=""):
    """
    Returns an `InlineKeyboardButton` with `callback_data` field

    Arguments:

    - `text` (`string`): Text of the button
    - `callback_data` (`string`): Callback Data of the button
    """
    return types.InlineKeyboardButton({"text": text, "callback_data": callback_data})


def inlineKBUrl(text, url):
    """
    Returns an `InlineKeyboardButton` with `url` field

    Arguments:

    - `text` (`string`): Text of the button
    - `url` (`string`): Url of the button
    """
    return types.InlineKeyboardButton({"text": text, "url": url})


def inlineKBSwitch(text, switch_par):
    """
    Returns an `InlineKeyboardButton` with `switch_inline_query` field

    Arguments:

    - `text` (`string`): Text of the button
    - `swtich_par` (`string`): Text to show when switched to inline query
    """
    return types.InlineKeyboardButton({"text": text, "switch_inline_query": switch_par})


def inlineKBSwitchCurrent(text, switch_par):
    """
    Returns an `InlineKeyboardButton` with `switch_inline_query_current_chat` field

    Arguments

    - `text` (`string`): Text of the button
    - `swtich_par` (`string`): Text to show when switched to inline query
    """
    return types.InlineKeyboardButton({"text": text, "switch_inline_query_current_chat": switch_par})


def inlineKBRow(*argv) -> list:
    """
    Row of inline Keyboard buttons

    - *`argv` (`list`): Pass InlineKeyboardButton objects to generate a list (This is unuseful, you an use [button1,button2] with the same result)
    """
    result = list()
    for arg in argv:
        result.append(arg)
    return result


def InlineKBMarkup(*argv):
    """
    Returns an `InlineKeyboardmarkup` with the given `inlineKBRow`

    - *`argv` (`list`): Pass lists of InlineKeyboardButton or use the InlineKBRow to generate them
    """
    result = list()
    for arg in argv:
        result.append(arg)
    return types.InlineKeyboardMarkup({"inline_keyboard": dictList(result)})


def replyKBbutton(text, request_contact=None, request_location=None, request_poll=None):
    """
    Returns a `KeyboardButton` for reply keyboards

    Arguments:

    - `text` (`string`): Text of the button
    - `request_contact` (`optional`)
    - `request_location` (`optional`):
    - `request_poll` (`optional`)
    """
    r = types.KeyboardButton(
        {"text": text, "requests_contact": request_contact, "request_location": request_location,
         "request_poll": request_poll})
    if request_poll is None:
        del r.request_poll
    return r


def replyKBRow(*argv) -> list:
    """
    Row of reply Keyboard buttons

    - *`argv` (`list`): Pass KeyboardButton objects to generate a list (This is unuseful, you an use [button1,button2] with the same result)
    """
    result = list()
    for arg in argv:
        result.append(arg)
    return result


def replyKeyboard(*argv):
    """
    Returns an `ReplyKeyboardMarkup` with the given `replyKBRow`

    - *`argv` (`list`): Pass lists of KeyboardButton or use the replyKBRow to generate them
    """
    result = list()
    for arg in argv:
        result.append(arg)
    return types.ReplyKeyboardMarkup({"keyboard": dictList(result)})
