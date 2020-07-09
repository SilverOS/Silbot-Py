"""
## Here there are some extra methods for types objects
"""
from silbot import types


class InlineKeyboardMarkup:
    """types.InlineKeyboardMarkup will inherit this class' methods"""

    def __init__(self,inline_keyboard = []):
        self.inline_keyboard = inline_keyboard

    def addLine(self,line : list):
        """Adds a line to the given keyboard

        Args:

        - `line` (`list`): list of InlineKeyboardButtons
        """
        self.inline_keyboard.append(line)

    def removeLine(self,line_number : int):
        """Removes a line from the given keyboard

        Args:

        - `line_number` (`int`): Number of the line (from 0) to remove
        """
        self.inline_keyboard.pop(line_number)


class ReplyKeyboardMarkup:
    """types.KeyboardMarkup will inherit this class' methods"""

    def __init__(self,keyboard = []):
        self.keyboard = keyboard

    def addLine(self,line : list):
        """Adds a line to the given keyboard

        Args:

        - `line` (`list`): list of KeyboardButtons
        """
        self.keyboard.append(line)

    def removeLine(self,line_number):
        """Removes a line from the given keyboard

        Args:

        - `line_number` (`int`): Number of the line (from 0) to remove
        """
        self.keyboard.pop(line_number)
        
