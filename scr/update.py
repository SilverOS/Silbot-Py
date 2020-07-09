"""
## This module's purpose is to handle botApi updates with multithreading
"""

import json
from threading import Thread
from silbot import botapi
from silbot import types


class update(Thread):
    """
    Elaborates the update in another thread
    """
    def __init__(self,update,bot: botapi.botApi, function):
        """
        Sets some var

        **Args:**
        - update (`dict`): json_decoded update
        - bot (`botApi`): the current bot botApi object
        - function (`function`): function to call to elaborate the update
        """
        self.update = update
        self.bot = bot
        self.function = function
        Thread.__init__(self)
    def run(self):
        """
        This is callen when the thread starts, parses the update and calls the given function
        """
        self.parsed = types.Update(self.update)
        self.function(self.parsed,self.bot)





