""" This module should manage the database of the bot
**You are supposed to write your own DatabaseManager class that extends this**, you can find some examples
in the [examples folder](https://github.com/SilverOS/Silbot-Py/tree/master/examples) with Redis and MySQL.

Setting a DatabaseManager class you can use specific methods in Chat and User objects"""


class DatabaseManager:
    """
    This function has to be overriden by your own DatabaseManager class
    """

    def __init__(self, connection):
        """Set the connection var

        Args:

        - connection (any): object of the database
        """

        self.db = connection

    def addUser(self, user, *additional_arguments):
        """This function has to add a user to the database

        **Args:**

        - user (types.user): User object to add to the database
        - *additional_arguments (any): Any additional argument that can be useful

        **Returns:**

        - `any type` to assign to user.db on success or `False` on failiture
        Raises:
        - NotImplementedError: if you don't override this method
        """
        raise NotImplementedError

    def addChat(self, chat, *additional_arguments):
        """This function has to add a chat to the database

        **Args:**

        - chat (types.chat): Chat object to add to the database
        - *additional_arguments (any): Any additional argument that can be useful

        **Returns:**

        - `any type` to assign to chat.db on success or `False` on failiture
        Raises:
        - NotImplementedError: if you don't override this method
        """
        raise NotImplementedError

    def getInfo(self, chat):
        """Get user's information from the db

        **Args:**

        - `chat` (`types.Chat`or `types.User`): Chat to get info

        **Returns:**

        - `any type` to assign to chat.db on success or `False` on failiture
        """
        raise NotImplementedError

    def setColumn(self, chat, column, value):
        """Edits database's column for a user

        **Args:**

        - `chat` (`types.Chat`or `types.User`): Chat to edit a column in database
        - `column` (`str`): Name of the column to edit
        - `value` (`str`): Value to set
        """
        raise NotImplementedError
