from silbot import database
from silbot import types
from silbot.helper import Generic_Json


class RedisDBManager(database.DatabaseManager):
    """This is an example of a DB manager using redis

    Args:

    - database (Redis): Redis connection to the Database
    """
    def addUser(self, user: types.User, *args):
        """Adds user's information into the database with this structure:

        - fist_name: user's first name
        - last_name: user's last name
        - username: user's username
        - state: default to "", this is just an example column
        - count: useful for the example, is the number of messages sent, default to 0

        Args:

        - user (types.User): user to add

        Returns:
        - Generic_Json object: a Generic_Json object of a dict containing user's information in {'key' : 'value'}
        """
        # If the user is already in the database, then don't overwrite the state and count column
        if self.db.exists(user.id) == 0:
            self.db.hset(user.id, "state", "")
            self.db.hset(user.id, "count", 0)

        # Overwrite user's Telegram information
        if user.first_name is not None:
            self.db.hset(user.id, "first_name", user.first_name)
        if user.last_name is not None:
            self.db.hset(user.id, "last_name", user.first_name)
        if user.username is not None:
            self.db.hset(user.id, "username", user.username)

        # Return user's info
        return self.getInfo(user)

    def addChat(self, chat: types.Chat, *args):
        """Adds chat's information into the database with this structure:

        - fist_name: chat's first name
        - last_name: chat's last name
        - username: chat's username
        - title: chat's title
        - state: default to "", this is just an example column
        - count: useful for the example, is the number of messages sent, default to 0

        Args:

        - chat (types.Chat): Chat to add

        Returns:
        - Generic_Json object: a Generic_Json object of a dict containing user's information in {'key' : 'value'}
        """
        # If the chat is already in the database, then don't overwrite the state column
        if self.db.exists(chat.id) == 0:
            self.db.hset(chat.id, "state", "")
            self.db.hset(chat.id, "count", 0)

        # Overwrite chat's Telegram information
        if chat.first_name is not None:
            self.db.hset(chat.id, "first_name", chat.first_name)
        if chat.last_name is not None:
            self.db.hset(chat.id, "last_name", chat.first_name)
        if chat.username is not None:
            self.db.hset(chat.id, "username", chat.username)
        if chat.title is not None:
            self.db.hset(chat.id, "title", chat.title)

        # Return chat's info
        return self.getInfo(chat)

    def getInfo(self, chat):
        """Get chat's information from the database:

        Args:

        - chat (types.Chat or types.User)

        Returns:
        - Generic_Json object: a Generic_Json object of a dict containing chat's information in {'key' : 'value'}
        """
        if self.db.exists(chat.id):
            response = self.db.hgetall(chat.id)
            dictionary = {i.decode("utf8"): j.decode("utf8") for i, j in response.items()}
            return Generic_Json(dictionary)
        else:
            return False

    def setColumn(self, chat, column: str, value: str):
        """Edits database's column for a user

        **Args:**

        - `chat` (`types.Chat`or `types.User`): Chat to edit a column in database
        - `column` (`str`): Name of the column to edit
        - `value` (`str`): Value to set
        """
        self.db.hset(chat.id, column, value)

    def fromUpdate(self, update: types.Update):
        """This function is optional: given the update it saves all the important information

        Args:

        - update (types.Update): update to save users from
        """
        if update.message is not None:
            user = update.message.user
            chat = update.message.chat
            user.setDBManager(self)
            user.save()
            chat.setDBManager(self)
            chat.save()
        elif update.callback_query is not None:
            user = update.callback_query.user
            user.setDBManager(self)
            user.save()
        elif update.edited_message is not None:
            chat = update.edited_message.chat
            chat.setDBManager(self)
            chat.save()
        elif update.channel_post is not None:
            chat = update.channel_post.chat
            chat.setDBManager(self)
            chat.save()
        elif update.chosen_inline_result is not None:
            user = update.chosen_inline_result.user
            user.setDBManager(self)
            user.save()
        elif update.inline_query is not None:
            user = update.inline_query.user
            user.setDBManager(self)
            user.save()
        elif update.shipping_query is not None:
            user = update.shipping_query.user
            user.setDBManager(self)
            user.save()
