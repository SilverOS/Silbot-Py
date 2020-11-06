from silbot import database
from silbot import types
from silbot.helper import Generic_Json
import pymysql


class MySQLDBManager(database.DatabaseManager):
    """This is an example of a DB manager using pymysql

    Args:

    - database (pymysql.Connection): MySQL connection to the Database via pymysql
    """
    def __init__(self, host, username, password, database):
        """With this function you can create a connection to the mysql database using pymysql

        Args:
            host (str): Host of MySQL Server
            username (str): Username of MySQL Server
            password (str): Password of MySQL Server
            database (str): Database to use
        """
        self.host = host
        self.username = username
        self.password = password
        self.database = database
        self.reconnect()

    def updateConnection(self):
        """This function opens a new connection to the database if the old connection is not opened
        """
        if not self.db.open:
            self.db.ping(reconnect=True)

    def reconnect(self):
        """This function opens a new connection to the database
        """
        self.db = pymysql.connect(self.host, self.username, self.password, self.database)

    def installDB(self, table_name: str):
        """Creates the table for the current database

        Args:

        - table_name: name of the table for this bot
        """
        self.table_name = table_name
        cursor = self.db.cursor()
        query = """CREATE TABLE IF NOT EXISTS `{}` (
                `chat_id` bigint(20) NOT NULL,
                `first_name` text NOT NULL DEFAULT '',
                `last_name` text NOT NULL DEFAULT '',
                `title` text NOT NULL DEFAULT '',
                `username` varchar(32) NOT NULL DEFAULT '',
                `state` varchar(200) NOT NULL DEFAULT '',
                `count` bigint(20) NOT NULL DEFAULT 0,
                PRIMARY KEY (chat_id)
            ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
        """.format(table_name)
        cursor.execute(query)

    def addChat(self, chat: types.Chat, *args):
        """Adds chat's information into the database with this structure:

        - chat_id: chat's id
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
        cursor = self.db.cursor()
        # Set values to put in the database
        last_name = chat.last_name if chat.last_name is not None else ""
        first_name = chat.first_name if chat.first_name is not None else ""
        username = chat.username if chat.username is not None else ""
        title = chat.title if hasattr(chat, "title") else ""

        info = self.getInfo(chat)
        if not info:
            # If the chat is not already in the database, then add it to the database
            q = "INSERT INTO " + self.table_name + " (chat_id,first_name,last_name,username,title,state,count) VALUES (%s,%s,%s,%s,%s,'',0)"
            cursor.execute(q, (chat.id, first_name, last_name, username, title))
        else:
            # If the chat is in the database, then update Telegram information
            if username != info.username:
                chat.setColumn("username", username)
            if first_name != info.first_name:
                chat.setColumn("first_name", first_name)
            if last_name != info.last_name:
                chat.setColumn("last_name", last_name)
            if title != info.title:
                chat.setColumn("title", title)
        self.db.commit()
        return self.getInfo(chat)

    def addUser(self, user: types.User, *args):
        """Adds chat's information into the database with this structure:

        - chat_id: chat's id
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
        return self.addChat(user)

    def getInfo(self, chat):
        """Get chat's information from the database:

        Args:

        - chat (types.Chat or types.User)

        Returns:
        - Generic_Json object: a Generic_Json object of a dict containing chat's information in {'key' : 'value'}
        """
        cursor = self.db.cursor()
        cursor.execute("SELECT * FROM " + self.table_name + " WHERE chat_id = %s LIMIT 1", (chat.id))
        if cursor.rowcount == 0:
            return False

        columns = cursor.description
        values = cursor.fetchone()
        result = dict()
        for index, value in enumerate(values):
            result[columns[index][0]] = value
        return Generic_Json(result)

    def setColumn(self, chat, column: str, value: str):
        """Edits database's column for a user

        **Args:**

        - `chat` (`types.Chat`or `types.User`): Chat to edit a column in database
        - `column` (`str`): Name of the column to edit
        - `value` (`str`): Value to set
        """
        cursor = self.db.cursor()
        cursor.execute("UPDATE " + self.table_name + " SET " + column + " = %s WHERE chat_id = %s", (value, chat.id))
        self.db.commit()

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
        elif update.callback_query:
            user = update.callback_query.user
            user.setDBManager(self)
            user.save()
        elif update.edited_message:
            chat = update.edited_message.chat
            chat.setDBManager(self)
            chat.save()
        elif update.channel_post:
            chat = update.channel_post.chat
            chat.setDBManager(self)
            chat.save()
        elif update.chosen_inline_result:
            user = update.chosen_inline_result.user
            user.setDBManager(self)
            user.save()
        elif update.inline_query:
            user = update.inline_query.user
            user.setDBManager(self)
            user.save()
        elif update.shipping_query:
            user = update.shipping_query.user
            user.setDBManager(self)
            user.save()
