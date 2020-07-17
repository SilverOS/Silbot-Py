from silbot import objects, helper


class Update:
    """This object represents an incoming update.At most one of the optional parameters can be present in any given update.[See on Telegram API](https://core.telegram.org/bots/api#update)

    - - - - -
    **Fields**:

    - `update_id`: `int` - The update‘s unique identifier. Update identifiers start from a certain positive number and increase sequentially. This ID becomes especially handy if you’re using Webhooks, since it allows you to ignore repeated updates or to restore the correct update sequence, should they get out of order. If there are no new updates for at least a week, then identifier of the next update will be chosen randomly instead of sequentially.
    - `message`: `Message` - Optional. New incoming message of any kind — text, photo, sticker, etc.
    - `edited_message`: `Message` - Optional. New version of a message that is known to the bot and was edited
    - `channel_post`: `Message` - Optional. New incoming channel post of any kind — text, photo, sticker, etc.
    - `edited_channel_post`: `Message` - Optional. New version of a channel post that is known to the bot and was edited
    - `inline_query`: `InlineQuery` - Optional. New incoming inline query
    - `chosen_inline_result`: `ChosenInlineResult` - Optional. The result of an inline query that was chosen by a user and sent to their chat partner. Please see our documentation on the feedback collecting for details on how to enable these updates for your bot.
    - `callback_query`: `CallbackQuery` - Optional. New incoming callback query
    - `shipping_query`: `ShippingQuery` - Optional. New incoming shipping query. Only for invoices with flexible price
    - `pre_checkout_query`: `PreCheckoutQuery` - Optional. New incoming pre-checkout query. Contains full information about checkout
    - `poll`: `Poll` - Optional. New poll state. Bots receive only updates about stopped polls and polls, which are sent by the bot
    - `poll_answer`: `PollAnswer` - Optional. A user changed their answer in a non-anonymous poll. Bots receive new votes only in polls that were sent by the bot itself.
    """

    def __init__(self, dictionary=None):
        if dictionary is None:
            dictionary = {}
        self.dict = dictionary
        for index, value in self.dict.items():
            if index == "update_id" and value is not None:
                self.update_id = value
            elif index == "message" and value is not None:
                self.message = Message(value)
            elif index == "edited_message" and value is not None:
                self.edited_message = Message(value)
            elif index == "channel_post" and value is not None:
                self.channel_post = Message(value)
            elif index == "edited_channel_post" and value is not None:
                self.edited_channel_post = Message(value)
            elif index == "inline_query" and value is not None:
                self.inline_query = InlineQuery(value)
            elif index == "chosen_inline_result" and value is not None:
                self.chosen_inline_result = ChosenInlineResult(value)
            elif index == "callback_query" and value is not None:
                self.callback_query = CallbackQuery(value)
            elif index == "shipping_query" and value is not None:
                self.shipping_query = ShippingQuery(value)
            elif index == "pre_checkout_query" and value is not None:
                self.pre_checkout_query = PreCheckoutQuery(value)
            elif index == "poll" and value is not None:
                self.poll = Poll(value)
            elif index == "poll_answer" and value is not None:
                self.poll_answer = PollAnswer(value)
            else:
                setattr(self, index, helper.setBvar(value))


class WebhookInfo:
    """Contains information about the current status of a webhook.[See on Telegram API](https://core.telegram.org/bots/api#webhookinfo)

    - - - - -
    **Fields**:

    - `url`: `string` - Webhook URL, may be empty if webhook is not set up
    - `has_custom_certificate`: `bool` - True, if a custom certificate was provided for webhook certificate checks
    - `pending_update_count`: `int` - Number of updates awaiting delivery
    - `last_error_date`: `int` - Optional. Unix time for the most recent error that happened when trying to deliver an update via webhook
    - `last_error_message`: `string` - Optional. Error message in human-readable format for the most recent error that happened when trying to deliver an update via webhook
    - `max_connections`: `int` - Optional. Maximum allowed number of simultaneous HTTPS connections to the webhook for update delivery
    - `allowed_updates`: `string[]` - Optional. A list of update types the bot is subscribed to. Defaults to all update types
    """

    def __init__(self, dictionary=None):
        if dictionary is None:
            dictionary = {}
        self.dict = dictionary
        for index, value in self.dict.items():
            if index == "url" and value is not None:
                self.url = value
            elif index == "has_custom_certificate" and value is not None:
                self.has_custom_certificate = value
            elif index == "pending_update_count" and value is not None:
                self.pending_update_count = value
            elif index == "last_error_date" and value is not None:
                self.last_error_date = value
            elif index == "last_error_message" and value is not None:
                self.last_error_message = value
            elif index == "max_connections" and value is not None:
                self.max_connections = value
            elif index == "allowed_updates" and value is not None:
                self.allowed_updates = list()
                for i1 in value:
                    self.allowed_updates.append(i1)
            else:
                setattr(self, index, helper.setBvar(value))


class User(objects.User):
    """This object represents a Telegram user or bot.[See on Telegram API](https://core.telegram.org/bots/api#user)

    - - - - -
    **Fields**:

    - `id`: `int` - Unique identifier for this user or bot
    - `is_bot`: `bool` - True, if this user is a bot
    - `first_name`: `string` - User‘s or bot’s first name
    - `last_name`: `string` - Optional. User‘s or bot’s last name
    - `username`: `string` - Optional. User‘s or bot’s username
    - `language_code`: `string` - Optional. IETF language tag of the user's language
    - `can_join_groups`: `bool` - Optional. True, if the bot can be invited to groups. Returned only in getMe.
    - `can_read_all_group_messages`: `bool` - Optional. True, if privacy mode is disabled for the bot. Returned only in getMe.
    - `supports_inline_queries`: `bool` - Optional. True, if the bot supports inline queries. Returned only in getMe.
    """

    def __init__(self, dictionary=None):
        if dictionary is None:
            dictionary = {}
        self.dict = dictionary
        for index, value in self.dict.items():
            if index == "id" and value is not None:
                self.id = value
            elif index == "is_bot" and value is not None:
                self.is_bot = value
            elif index == "first_name" and value is not None:
                self.first_name = value
            elif index == "last_name" and value is not None:
                self.last_name = value
            elif index == "username" and value is not None:
                self.username = value
            elif index == "language_code" and value is not None:
                self.language_code = value
            elif index == "can_join_groups" and value is not None:
                self.can_join_groups = value
            elif index == "can_read_all_group_messages" and value is not None:
                self.can_read_all_group_messages = value
            elif index == "supports_inline_queries" and value is not None:
                self.supports_inline_queries = value
            else:
                setattr(self, index, helper.setBvar(value))


class Chat(objects.Chat):
    """This object represents a chat.[See on Telegram API](https://core.telegram.org/bots/api#chat)

    - - - - -
    **Fields**:

    - `id`: `int` - Unique identifier for this chat. This number may be greater than 32 bits and some programming languages may have difficulty/silent defects in interpreting it. But it is smaller than 52 bits, so a signed 64 bit integer or double-precision float type are safe for storing this identifier.
    - `type`: `string` - Type of chat, can be either “private”, “group”, “supergroup” or “channel”
    - `title`: `string` - Optional. Title, for supergroups, channels and group chats
    - `username`: `string` - Optional. Username, for private chats, supergroups and channels if available
    - `first_name`: `string` - Optional. First name of the other party in a private chat
    - `last_name`: `string` - Optional. Last name of the other party in a private chat
    - `photo`: `ChatPhoto` - Optional. Chat photo. Returned only in getChat.
    - `description`: `string` - Optional. Description, for groups, supergroups and channel chats. Returned only in getChat.
    - `invite_link`: `string` - Optional. Chat invite link, for groups, supergroups and channel chats. Each administrator in a chat generates their own invite links, so the bot must first generate the link using exportChatInviteLink. Returned only in getChat.
    - `pinned_message`: `Message` - Optional. Pinned message, for groups, supergroups and channels. Returned only in getChat.
    - `permissions`: `ChatPermissions` - Optional. Default chat member permissions, for groups and supergroups. Returned only in getChat.
    - `slow_mode_delay`: `int` - Optional. For supergroups, the minimum allowed delay between consecutive messages sent by each unpriviledged user. Returned only in getChat.
    - `sticker_set_name`: `string` - Optional. For supergroups, name of group sticker set. Returned only in getChat.
    - `can_set_sticker_set`: `bool` - Optional. True, if the bot can change the group sticker set. Returned only in getChat.
    """

    def __init__(self, dictionary=None):
        if dictionary is None:
            dictionary = {}
        self.dict = dictionary
        for index, value in self.dict.items():
            if index == "id" and value is not None:
                self.id = value
            elif index == "type" and value is not None:
                self.type = value
            elif index == "title" and value is not None:
                self.title = value
            elif index == "username" and value is not None:
                self.username = value
            elif index == "first_name" and value is not None:
                self.first_name = value
            elif index == "last_name" and value is not None:
                self.last_name = value
            elif index == "photo" and value is not None:
                self.photo = ChatPhoto(value)
            elif index == "description" and value is not None:
                self.description = value
            elif index == "invite_link" and value is not None:
                self.invite_link = value
            elif index == "pinned_message" and value is not None:
                self.pinned_message = Message(value)
            elif index == "permissions" and value is not None:
                self.permissions = ChatPermissions(value)
            elif index == "slow_mode_delay" and value is not None:
                self.slow_mode_delay = value
            elif index == "sticker_set_name" and value is not None:
                self.sticker_set_name = value
            elif index == "can_set_sticker_set" and value is not None:
                self.can_set_sticker_set = value
            else:
                setattr(self, index, helper.setBvar(value))


class Message:
    """This object represents a message.[See on Telegram API](https://core.telegram.org/bots/api#message)

    - - - - -
    **Fields**:

    - `message_id`: `int` - Unique message identifier inside this chat
    - `user`: `User` - Optional. Sender, empty for messages sent to channels
    - `date`: `int` - Date the message was sent in Unix time
    - `chat`: `Chat` - Conversation the message belongs to
    - `forward_from`: `User` - Optional. For forwarded messages, sender of the original message
    - `forward_from_chat`: `Chat` - Optional. For messages forwarded from channels, information about the original channel
    - `forward_from_message_id`: `int` - Optional. For messages forwarded from channels, identifier of the original message in the channel
    - `forward_signature`: `string` - Optional. For messages forwarded from channels, signature of the post author if present
    - `forward_sender_name`: `string` - Optional. Sender's name for messages forwarded from users who disallow adding a link to their account in forwarded messages
    - `forward_date`: `int` - Optional. For forwarded messages, date the original message was sent in Unix time
    - `reply_to_message`: `Message` - Optional. For replies, the original message. Note that the Message object in this field will not contain further reply_to_message fields even if it itself is a reply.
    - `edit_date`: `int` - Optional. Date the message was last edited in Unix time
    - `media_group_id`: `string` - Optional. The unique identifier of a media message group this message belongs to
    - `author_signature`: `string` - Optional. Signature of the post author for messages in channels
    - `text`: `string` - Optional. For text messages, the actual UTF-8 text of the message, 0-4096 characters
    - `entities`: `MessageEntity[]` - Optional. For text messages, special entities like usernames, URLs, bot commands, etc. that appear in the text
    - `caption_entities`: `MessageEntity[]` - Optional. For messages with a caption, special entities like usernames, URLs, bot commands, etc. that appear in the caption
    - `audio`: `Audio` - Optional. Message is an audio file, information about the file
    - `document`: `Document` - Optional. Message is a general file, information about the file
    - `animation`: `Animation` - Optional. Message is an animation, information about the animation. For backward compatibility, when this field is set, the document field will also be set
    - `game`: `Game` - Optional. Message is a game, information about the game. More about games »
    - `photo`: `PhotoSize[]` - Optional. Message is a photo, available sizes of the photo
    - `sticker`: `Sticker` - Optional. Message is a sticker, information about the sticker
    - `video`: `Video` - Optional. Message is a video, information about the video
    - `voice`: `Voice` - Optional. Message is a voice message, information about the file
    - `video_note`: `VideoNote` - Optional. Message is a video note, information about the video message
    - `caption`: `string` - Optional. Caption for the animation, audio, document, photo, video or voice, 0-1024 characters
    - `contact`: `Contact` - Optional. Message is a shared contact, information about the contact
    - `location`: `Location` - Optional. Message is a shared location, information about the location
    - `venue`: `Venue` - Optional. Message is a venue, information about the venue
    - `poll`: `Poll` - Optional. Message is a native poll, information about the poll
    - `dice`: `Dice` - Optional. Message is a dice with random value from 1 to 6
    - `new_chat_members`: `User[]` - Optional. New members that were added to the group or supergroup and information about them (the bot itself may be one of these members)
    - `left_chat_member`: `User` - Optional. A member was removed from the group, information about them (this member may be the bot itself)
    - `new_chat_title`: `string` - Optional. A chat title was changed to this value
    - `new_chat_photo`: `PhotoSize[]` - Optional. A chat photo was change to this value
    - `delete_chat_photo`: `True` - Optional. Service message: the chat photo was deleted
    - `group_chat_created`: `True` - Optional. Service message: the group has been created
    - `supergroup_chat_created`: `True` - Optional. Service message: the supergroup has been created. This field can‘t be received in a message coming through updates, because bot can’t be a member of a supergroup when it is created. It can only be found in reply_to_message if someone replies to a very first message in a directly created supergroup.
    - `channel_chat_created`: `True` - Optional. Service message: the channel has been created. This field can‘t be received in a message coming through updates, because bot can’t be a member of a channel when it is created. It can only be found in reply_to_message if someone replies to a very first message in a channel.
    - `migrate_to_chat_id`: `int` - Optional. The group has been migrated to a supergroup with the specified identifier. This number may be greater than 32 bits and some programming languages may have difficulty/silent defects in interpreting it. But it is smaller than 52 bits, so a signed 64 bit integer or double-precision float type are safe for storing this identifier.
    - `migrate_from_chat_id`: `int` - Optional. The supergroup has been migrated from a group with the specified identifier. This number may be greater than 32 bits and some programming languages may have difficulty/silent defects in interpreting it. But it is smaller than 52 bits, so a signed 64 bit integer or double-precision float type are safe for storing this identifier.
    - `pinned_message`: `Message` - Optional. Specified message was pinned. Note that the Message object in this field will not contain further reply_to_message fields even if it is itself a reply.
    - `invoice`: `Invoice` - Optional. Message is an invoice for a payment, information about the invoice. More about payments »
    - `successful_payment`: `SuccessfulPayment` - Optional. Message is a service message about a successful payment, information about the payment. More about payments »
    - `connected_website`: `string` - Optional. The domain name of the website on which the user has logged in. More about Telegram Login »
    - `passport_data`: `PassportData` - Optional. Telegram Passport data
    - `reply_markup`: `InlineKeyboardMarkup` - Optional. Inline keyboard attached to the message. login_url buttons are represented as ordinary url buttons.
    """

    def __init__(self, dictionary=None):
        if dictionary is None:
            dictionary = {}
        self.dict = dictionary
        for index, value in self.dict.items():
            if index == "message_id" and value is not None:
                self.message_id = value
            elif index == "from" and value is not None:
                self.user = User(value)
            elif index == "date" and value is not None:
                self.date = value
            elif index == "chat" and value is not None:
                self.chat = Chat(value)
            elif index == "forward_from" and value is not None:
                self.forward_from = User(value)
            elif index == "forward_from_chat" and value is not None:
                self.forward_from_chat = Chat(value)
            elif index == "forward_from_message_id" and value is not None:
                self.forward_from_message_id = value
            elif index == "forward_signature" and value is not None:
                self.forward_signature = value
            elif index == "forward_sender_name" and value is not None:
                self.forward_sender_name = value
            elif index == "forward_date" and value is not None:
                self.forward_date = value
            elif index == "reply_to_message" and value is not None:
                self.reply_to_message = Message(value)
            elif index == "edit_date" and value is not None:
                self.edit_date = value
            elif index == "media_group_id" and value is not None:
                self.media_group_id = value
            elif index == "author_signature" and value is not None:
                self.author_signature = value
            elif index == "text" and value is not None:
                self.text = value
            elif index == "entities" and value is not None:
                self.entities = list()
                for i1 in value:
                    self.entities.append(MessageEntity(i1))
            elif index == "caption_entities" and value is not None:
                self.caption_entities = list()
                for i1 in value:
                    self.caption_entities.append(MessageEntity(i1))
            elif index == "audio" and value is not None:
                self.audio = Audio(value)
            elif index == "document" and value is not None:
                self.document = Document(value)
            elif index == "animation" and value is not None:
                self.animation = Animation(value)
            elif index == "game" and value is not None:
                self.game = Game(value)
            elif index == "photo" and value is not None:
                self.photo = list()
                for i1 in value:
                    self.photo.append(PhotoSize(i1))
            elif index == "sticker" and value is not None:
                self.sticker = Sticker(value)
            elif index == "video" and value is not None:
                self.video = Video(value)
            elif index == "voice" and value is not None:
                self.voice = Voice(value)
            elif index == "video_note" and value is not None:
                self.video_note = VideoNote(value)
            elif index == "caption" and value is not None:
                self.caption = value
            elif index == "contact" and value is not None:
                self.contact = Contact(value)
            elif index == "location" and value is not None:
                self.location = Location(value)
            elif index == "venue" and value is not None:
                self.venue = Venue(value)
            elif index == "poll" and value is not None:
                self.poll = Poll(value)
            elif index == "dice" and value is not None:
                self.dice = Dice(value)
            elif index == "new_chat_members" and value is not None:
                self.new_chat_members = list()
                for i1 in value:
                    self.new_chat_members.append(User(i1))
            elif index == "left_chat_member" and value is not None:
                self.left_chat_member = User(value)
            elif index == "new_chat_title" and value is not None:
                self.new_chat_title = value
            elif index == "new_chat_photo" and value is not None:
                self.new_chat_photo = list()
                for i1 in value:
                    self.new_chat_photo.append(PhotoSize(i1))
            elif index == "delete_chat_photo" and value is not None:
                self.delete_chat_photo = value
            elif index == "group_chat_created" and value is not None:
                self.group_chat_created = value
            elif index == "supergroup_chat_created" and value is not None:
                self.supergroup_chat_created = value
            elif index == "channel_chat_created" and value is not None:
                self.channel_chat_created = value
            elif index == "migrate_to_chat_id" and value is not None:
                self.migrate_to_chat_id = value
            elif index == "migrate_from_chat_id" and value is not None:
                self.migrate_from_chat_id = value
            elif index == "pinned_message" and value is not None:
                self.pinned_message = Message(value)
            elif index == "invoice" and value is not None:
                self.invoice = Invoice(value)
            elif index == "successful_payment" and value is not None:
                self.successful_payment = SuccessfulPayment(value)
            elif index == "connected_website" and value is not None:
                self.connected_website = value
            elif index == "passport_data" and value is not None:
                self.passport_data = PassportData(value)
            elif index == "reply_markup" and value is not None:
                self.reply_markup = InlineKeyboardMarkup(value)
            else:
                setattr(self, index, helper.setBvar(value))


class MessageEntity:
    """This object represents one special entity in a text message. For example, hashtags, usernames, URLs, etc.[See on Telegram API](https://core.telegram.org/bots/api#messageentity)

    - - - - -
    **Fields**:

    - `type`: `string` - Type of the entity. Can be “mention” (@username), “hashtag” (#hashtag), “cashtag” ($USD), “bot_command” (/start@jobs_bot), “url” (https://telegram.org), “email” (do-not-reply@telegram.org), “phone_number” (+1-212-555-0123), “bold” (bold text), “italic” (italic text), “underline” (underlined text), “strikethrough” (strikethrough text), “code” (monowidth string), “pre” (monowidth block), “text_link” (for clickable text URLs), “text_mention” (for users without usernames)
    - `offset`: `int` - Offset in UTF-16 code units to the start of the entity
    - `length`: `int` - Length of the entity in UTF-16 code units
    - `url`: `string` - Optional. For “text_link” only, url that will be opened after user taps on the text
    - `user`: `User` - Optional. For “text_mention” only, the mentioned user
    - `language`: `string` - Optional. For “pre” only, the programming language of the entity text
    """

    def __init__(self, dictionary=None):
        if dictionary is None:
            dictionary = {}
        self.dict = dictionary
        for index, value in self.dict.items():
            if index == "type" and value is not None:
                self.type = value
            elif index == "offset" and value is not None:
                self.offset = value
            elif index == "length" and value is not None:
                self.length = value
            elif index == "url" and value is not None:
                self.url = value
            elif index == "user" and value is not None:
                self.user = User(value)
            elif index == "language" and value is not None:
                self.language = value
            else:
                setattr(self, index, helper.setBvar(value))


class PhotoSize:
    """This object represents one size of a photo or a file / sticker thumbnail.[See on Telegram API](https://core.telegram.org/bots/api#photosize)

    - - - - -
    **Fields**:

    - `file_id`: `string` - Identifier for this file, which can be used to download or reuse the file
    - `file_unique_id`: `string` - Unique identifier for this file, which is supposed to be the same over time and for different bots. Can't be used to download or reuse the file.
    - `width`: `int` - Photo width
    - `height`: `int` - Photo height
    - `file_size`: `int` - Optional. File size
    """

    def __init__(self, dictionary=None):
        if dictionary is None:
            dictionary = {}
        self.dict = dictionary
        for index, value in self.dict.items():
            if index == "file_id" and value is not None:
                self.file_id = value
            elif index == "file_unique_id" and value is not None:
                self.file_unique_id = value
            elif index == "width" and value is not None:
                self.width = value
            elif index == "height" and value is not None:
                self.height = value
            elif index == "file_size" and value is not None:
                self.file_size = value
            else:
                setattr(self, index, helper.setBvar(value))


class Audio:
    """This object represents an audio file to be treated as music by the Telegram clients.[See on Telegram API](https://core.telegram.org/bots/api#audio)

    - - - - -
    **Fields**:

    - `file_id`: `string` - Identifier for this file, which can be used to download or reuse the file
    - `file_unique_id`: `string` - Unique identifier for this file, which is supposed to be the same over time and for different bots. Can't be used to download or reuse the file.
    - `duration`: `int` - Duration of the audio in seconds as defined by sender
    - `performer`: `string` - Optional. Performer of the audio as defined by sender or by audio tags
    - `title`: `string` - Optional. Title of the audio as defined by sender or by audio tags
    - `mime_type`: `string` - Optional. MIME type of the file as defined by sender
    - `file_size`: `int` - Optional. File size
    - `thumb`: `PhotoSize` - Optional. Thumbnail of the album cover to which the music file belongs
    """

    def __init__(self, dictionary=None):
        if dictionary is None:
            dictionary = {}
        self.dict = dictionary
        for index, value in self.dict.items():
            if index == "file_id" and value is not None:
                self.file_id = value
            elif index == "file_unique_id" and value is not None:
                self.file_unique_id = value
            elif index == "duration" and value is not None:
                self.duration = value
            elif index == "performer" and value is not None:
                self.performer = value
            elif index == "title" and value is not None:
                self.title = value
            elif index == "mime_type" and value is not None:
                self.mime_type = value
            elif index == "file_size" and value is not None:
                self.file_size = value
            elif index == "thumb" and value is not None:
                self.thumb = PhotoSize(value)
            else:
                setattr(self, index, helper.setBvar(value))


class Document:
    """This object represents a general file (as opposed to photos, voice messages and audio files).[See on Telegram API](https://core.telegram.org/bots/api#document)

    - - - - -
    **Fields**:

    - `file_id`: `string` - Identifier for this file, which can be used to download or reuse the file
    - `file_unique_id`: `string` - Unique identifier for this file, which is supposed to be the same over time and for different bots. Can't be used to download or reuse the file.
    - `thumb`: `PhotoSize` - Optional. Document thumbnail as defined by sender
    - `file_name`: `string` - Optional. Original filename as defined by sender
    - `mime_type`: `string` - Optional. MIME type of the file as defined by sender
    - `file_size`: `int` - Optional. File size
    """

    def __init__(self, dictionary=None):
        if dictionary is None:
            dictionary = {}
        self.dict = dictionary
        for index, value in self.dict.items():
            if index == "file_id" and value is not None:
                self.file_id = value
            elif index == "file_unique_id" and value is not None:
                self.file_unique_id = value
            elif index == "thumb" and value is not None:
                self.thumb = PhotoSize(value)
            elif index == "file_name" and value is not None:
                self.file_name = value
            elif index == "mime_type" and value is not None:
                self.mime_type = value
            elif index == "file_size" and value is not None:
                self.file_size = value
            else:
                setattr(self, index, helper.setBvar(value))


class Video:
    """This object represents a video file.[See on Telegram API](https://core.telegram.org/bots/api#video)

    - - - - -
    **Fields**:

    - `file_id`: `string` - Identifier for this file, which can be used to download or reuse the file
    - `file_unique_id`: `string` - Unique identifier for this file, which is supposed to be the same over time and for different bots. Can't be used to download or reuse the file.
    - `width`: `int` - Video width as defined by sender
    - `height`: `int` - Video height as defined by sender
    - `duration`: `int` - Duration of the video in seconds as defined by sender
    - `thumb`: `PhotoSize` - Optional. Video thumbnail
    - `mime_type`: `string` - Optional. Mime type of a file as defined by sender
    - `file_size`: `int` - Optional. File size
    """

    def __init__(self, dictionary=None):
        if dictionary is None:
            dictionary = {}
        self.dict = dictionary
        for index, value in self.dict.items():
            if index == "file_id" and value is not None:
                self.file_id = value
            elif index == "file_unique_id" and value is not None:
                self.file_unique_id = value
            elif index == "width" and value is not None:
                self.width = value
            elif index == "height" and value is not None:
                self.height = value
            elif index == "duration" and value is not None:
                self.duration = value
            elif index == "thumb" and value is not None:
                self.thumb = PhotoSize(value)
            elif index == "mime_type" and value is not None:
                self.mime_type = value
            elif index == "file_size" and value is not None:
                self.file_size = value
            else:
                setattr(self, index, helper.setBvar(value))


class Animation:
    """This object represents an animation file (GIF or H.264/MPEG-4 AVC video without sound).[See on Telegram API](https://core.telegram.org/bots/api#animation)

    - - - - -
    **Fields**:

    - `file_id`: `string` - Identifier for this file, which can be used to download or reuse the file
    - `file_unique_id`: `string` - Unique identifier for this file, which is supposed to be the same over time and for different bots. Can't be used to download or reuse the file.
    - `width`: `int` - Video width as defined by sender
    - `height`: `int` - Video height as defined by sender
    - `duration`: `int` - Duration of the video in seconds as defined by sender
    - `thumb`: `PhotoSize` - Optional. Animation thumbnail as defined by sender
    - `file_name`: `string` - Optional. Original animation filename as defined by sender
    - `mime_type`: `string` - Optional. MIME type of the file as defined by sender
    - `file_size`: `int` - Optional. File size
    """

    def __init__(self, dictionary=None):
        if dictionary is None:
            dictionary = {}
        self.dict = dictionary
        for index, value in self.dict.items():
            if index == "file_id" and value is not None:
                self.file_id = value
            elif index == "file_unique_id" and value is not None:
                self.file_unique_id = value
            elif index == "width" and value is not None:
                self.width = value
            elif index == "height" and value is not None:
                self.height = value
            elif index == "duration" and value is not None:
                self.duration = value
            elif index == "thumb" and value is not None:
                self.thumb = PhotoSize(value)
            elif index == "file_name" and value is not None:
                self.file_name = value
            elif index == "mime_type" and value is not None:
                self.mime_type = value
            elif index == "file_size" and value is not None:
                self.file_size = value
            else:
                setattr(self, index, helper.setBvar(value))


class Voice:
    """This object represents a voice note.[See on Telegram API](https://core.telegram.org/bots/api#voice)

    - - - - -
    **Fields**:

    - `file_id`: `string` - Identifier for this file, which can be used to download or reuse the file
    - `file_unique_id`: `string` - Unique identifier for this file, which is supposed to be the same over time and for different bots. Can't be used to download or reuse the file.
    - `duration`: `int` - Duration of the audio in seconds as defined by sender
    - `mime_type`: `string` - Optional. MIME type of the file as defined by sender
    - `file_size`: `int` - Optional. File size
    """

    def __init__(self, dictionary=None):
        if dictionary is None:
            dictionary = {}
        self.dict = dictionary
        for index, value in self.dict.items():
            if index == "file_id" and value is not None:
                self.file_id = value
            elif index == "file_unique_id" and value is not None:
                self.file_unique_id = value
            elif index == "duration" and value is not None:
                self.duration = value
            elif index == "mime_type" and value is not None:
                self.mime_type = value
            elif index == "file_size" and value is not None:
                self.file_size = value
            else:
                setattr(self, index, helper.setBvar(value))


class VideoNote:
    """This object represents a video message (available in Telegram apps as of v.4.0).[See on Telegram API](https://core.telegram.org/bots/api#videonote)

    - - - - -
    **Fields**:

    - `file_id`: `string` - Identifier for this file, which can be used to download or reuse the file
    - `file_unique_id`: `string` - Unique identifier for this file, which is supposed to be the same over time and for different bots. Can't be used to download or reuse the file.
    - `length`: `int` - Video width and height (diameter of the video message) as defined by sender
    - `duration`: `int` - Duration of the video in seconds as defined by sender
    - `thumb`: `PhotoSize` - Optional. Video thumbnail
    - `file_size`: `int` - Optional. File size
    """

    def __init__(self, dictionary=None):
        if dictionary is None:
            dictionary = {}
        self.dict = dictionary
        for index, value in self.dict.items():
            if index == "file_id" and value is not None:
                self.file_id = value
            elif index == "file_unique_id" and value is not None:
                self.file_unique_id = value
            elif index == "length" and value is not None:
                self.length = value
            elif index == "duration" and value is not None:
                self.duration = value
            elif index == "thumb" and value is not None:
                self.thumb = PhotoSize(value)
            elif index == "file_size" and value is not None:
                self.file_size = value
            else:
                setattr(self, index, helper.setBvar(value))


class Contact:
    """This object represents a phone contact.[See on Telegram API](https://core.telegram.org/bots/api#contact)

    - - - - -
    **Fields**:

    - `phone_number`: `string` - Contact's phone number
    - `first_name`: `string` - Contact's first name
    - `last_name`: `string` - Optional. Contact's last name
    - `user_id`: `int` - Optional. Contact's user identifier in Telegram
    - `vcard`: `string` - Optional. Additional data about the contact in the form of a vCard
    """

    def __init__(self, dictionary=None):
        if dictionary is None:
            dictionary = {}
        self.dict = dictionary
        for index, value in self.dict.items():
            if index == "phone_number" and value is not None:
                self.phone_number = value
            elif index == "first_name" and value is not None:
                self.first_name = value
            elif index == "last_name" and value is not None:
                self.last_name = value
            elif index == "user_id" and value is not None:
                self.user_id = value
            elif index == "vcard" and value is not None:
                self.vcard = value
            else:
                setattr(self, index, helper.setBvar(value))


class Location:
    """This object represents a point on the map.[See on Telegram API](https://core.telegram.org/bots/api#location)

    - - - - -
    **Fields**:

    - `longitude`: `float` - Longitude as defined by sender
    - `latitude`: `float` - Latitude as defined by sender
    """

    def __init__(self, dictionary=None):
        if dictionary is None:
            dictionary = {}
        self.dict = dictionary
        for index, value in self.dict.items():
            if index == "longitude" and value is not None:
                self.longitude = value
            elif index == "latitude" and value is not None:
                self.latitude = value
            else:
                setattr(self, index, helper.setBvar(value))


class Venue:
    """This object represents a venue.[See on Telegram API](https://core.telegram.org/bots/api#venue)

    - - - - -
    **Fields**:

    - `location`: `Location` - Venue location
    - `title`: `string` - Name of the venue
    - `address`: `string` - Address of the venue
    - `foursquare_id`: `string` - Optional. Foursquare identifier of the venue
    - `foursquare_type`: `string` - Optional. Foursquare type of the venue. (For example, “arts_entertainment/default”, “arts_entertainment/aquarium” or “food/icecream”.)
    """

    def __init__(self, dictionary=None):
        if dictionary is None:
            dictionary = {}
        self.dict = dictionary
        for index, value in self.dict.items():
            if index == "location" and value is not None:
                self.location = Location(value)
            elif index == "title" and value is not None:
                self.title = value
            elif index == "address" and value is not None:
                self.address = value
            elif index == "foursquare_id" and value is not None:
                self.foursquare_id = value
            elif index == "foursquare_type" and value is not None:
                self.foursquare_type = value
            else:
                setattr(self, index, helper.setBvar(value))


class PollOption:
    """This object contains information about one answer option in a poll.[See on Telegram API](https://core.telegram.org/bots/api#polloption)

    - - - - -
    **Fields**:

    - `text`: `string` - Option text, 1-100 characters
    - `voter_count`: `int` - Number of users that voted for this option
    """

    def __init__(self, dictionary=None):
        if dictionary is None:
            dictionary = {}
        self.dict = dictionary
        for index, value in self.dict.items():
            if index == "text" and value is not None:
                self.text = value
            elif index == "voter_count" and value is not None:
                self.voter_count = value
            else:
                setattr(self, index, helper.setBvar(value))


class PollAnswer:
    """This object represents an answer of a user in a non-anonymous poll.[See on Telegram API](https://core.telegram.org/bots/api#pollanswer)

    - - - - -
    **Fields**:

    - `poll_id`: `string` - Unique poll identifier
    - `user`: `User` - The user, who changed the answer to the poll
    - `option_ids`: `int[]` - 0-based identifiers of answer options, chosen by the user. May be empty if the user retracted their vote.
    """

    def __init__(self, dictionary=None):
        if dictionary is None:
            dictionary = {}
        self.dict = dictionary
        for index, value in self.dict.items():
            if index == "poll_id" and value is not None:
                self.poll_id = value
            elif index == "user" and value is not None:
                self.user = User(value)
            elif index == "option_ids" and value is not None:
                self.option_ids = list()
                for i1 in value:
                    self.option_ids.append(i1)
            else:
                setattr(self, index, helper.setBvar(value))


class Poll:
    """This object contains information about a poll.[See on Telegram API](https://core.telegram.org/bots/api#poll)

    - - - - -
    **Fields**:

    - `id`: `string` - Unique poll identifier
    - `question`: `string` - Poll question, 1-255 characters
    - `options`: `PollOption[]` - List of poll options
    - `total_voter_count`: `int` - Total number of users that voted in the poll
    - `is_closed`: `bool` - True, if the poll is closed
    - `is_anonymous`: `bool` - True, if the poll is anonymous
    - `type`: `string` - Poll type, currently can be “regular” or “quiz”
    - `allows_multiple_answers`: `bool` - True, if the poll allows multiple answers
    - `correct_option_id`: `int` - Optional. 0-based identifier of the correct answer option. Available only for polls in the quiz mode, which are closed, or was sent (not forwarded) by the bot or to the private chat with the bot.
    - `explanation`: `string` - Optional. Text that is shown when a user chooses an incorrect answer or taps on the lamp icon in a quiz-style poll, 0-200 characters
    - `explanation_entities`: `MessageEntity[]` - Optional. Special entities like usernames, URLs, bot commands, etc. that appear in the explanation
    - `open_period`: `int` - Optional. Amount of time in seconds the poll will be active after creation
    - `close_date`: `int` - Optional. Point in time (Unix timestamp) when the poll will be automatically closed
    """

    def __init__(self, dictionary=None):
        if dictionary is None:
            dictionary = {}
        self.dict = dictionary
        for index, value in self.dict.items():
            if index == "id" and value is not None:
                self.id = value
            elif index == "question" and value is not None:
                self.question = value
            elif index == "options" and value is not None:
                self.options = list()
                for i1 in value:
                    self.options.append(PollOption(i1))
            elif index == "total_voter_count" and value is not None:
                self.total_voter_count = value
            elif index == "is_closed" and value is not None:
                self.is_closed = value
            elif index == "is_anonymous" and value is not None:
                self.is_anonymous = value
            elif index == "type" and value is not None:
                self.type = value
            elif index == "allows_multiple_answers" and value is not None:
                self.allows_multiple_answers = value
            elif index == "correct_option_id" and value is not None:
                self.correct_option_id = value
            elif index == "explanation" and value is not None:
                self.explanation = value
            elif index == "explanation_entities" and value is not None:
                self.explanation_entities = list()
                for i1 in value:
                    self.explanation_entities.append(MessageEntity(i1))
            elif index == "open_period" and value is not None:
                self.open_period = value
            elif index == "close_date" and value is not None:
                self.close_date = value
            else:
                setattr(self, index, helper.setBvar(value))


class Dice:
    """This object represents a dice with a random value from 1 to 6 for currently supported base emoji. (Yes, we're aware of the “proper” singular of die. But it's awkward, and we decided to help it change. One dice at a time!)[See on Telegram API](https://core.telegram.org/bots/api#dice)

    - - - - -
    **Fields**:

    - `emoji`: `string` - Emoji on which the dice throw animation is based
    - `value`: `int` - Value of the dice, 1-6 for currently supported base emoji
    """

    def __init__(self, dictionary=None):
        if dictionary is None:
            dictionary = {}
        self.dict = dictionary
        for index, value in self.dict.items():
            if index == "emoji" and value is not None:
                self.emoji = value
            elif index == "value" and value is not None:
                self.value = value
            else:
                setattr(self, index, helper.setBvar(value))


class UserProfilePhotos:
    """This object represent a user's profile pictures.[See on Telegram API](https://core.telegram.org/bots/api#userprofilephotos)

    - - - - -
    **Fields**:

    - `total_count`: `int` - Total number of profile pictures the target user has
    - `photos`: `PhotoSize[][]` - Requested profile pictures (in up to 4 sizes each)
    """

    def __init__(self, dictionary=None):
        if dictionary is None:
            dictionary = {}
        self.dict = dictionary
        for index, value in self.dict.items():
            if index == "total_count" and value is not None:
                self.total_count = value
            elif index == "photos" and value is not None:
                self.photos = list()
                for i1 in value:
                    sublist = list()
                    for i2 in i1:
                        sublist.append(PhotoSize(i2))
                    self.photos.append(sublist)
            else:
                setattr(self, index, helper.setBvar(value))


class File:
    """This object represents a file ready to be downloaded. The file can be downloaded via the link https://api.telegram.org/file/bot<token>/<file_path>. It is guaranteed that the link will be valid for at least 1 hour. When the link expires, a new one can be requested by calling getFile.[See on Telegram API](https://core.telegram.org/bots/api#file)

    - - - - -
    **Fields**:

    - `file_id`: `string` - Identifier for this file, which can be used to download or reuse the file
    - `file_unique_id`: `string` - Unique identifier for this file, which is supposed to be the same over time and for different bots. Can't be used to download or reuse the file.
    - `file_size`: `int` - Optional. File size, if known
    - `file_path`: `string` - Optional. File path. Use https://api.telegram.org/file/bot<token>/<file_path> to get the file.
    """

    def __init__(self, dictionary=None):
        if dictionary is None:
            dictionary = {}
        self.dict = dictionary
        for index, value in self.dict.items():
            if index == "file_id" and value is not None:
                self.file_id = value
            elif index == "file_unique_id" and value is not None:
                self.file_unique_id = value
            elif index == "file_size" and value is not None:
                self.file_size = value
            elif index == "file_path" and value is not None:
                self.file_path = value
            else:
                setattr(self, index, helper.setBvar(value))


class ReplyKeyboardMarkup(objects.ReplyKeyboardMarkup):
    """This object represents a custom keyboard with reply options (see Introduction to bots for details and examples).[See on Telegram API](https://core.telegram.org/bots/api#replykeyboardmarkup)

    - - - - -
    **Fields**:

    - `keyboard`: `KeyboardButton[][]` - Array of button rows, each represented by an Array of KeyboardButton objects
    - `resize_keyboard`: `bool` - Optional. Requests clients to resize the keyboard vertically for optimal fit (e.g., make the keyboard smaller if there are just two rows of buttons). Defaults to false, in which case the custom keyboard is always of the same height as the app's standard keyboard.
    - `one_time_keyboard`: `bool` - Optional. Requests clients to hide the keyboard as soon as it's been used. The keyboard will still be available, but clients will automatically display the usual letter-keyboard in the chat – the user can press a special button in the input field to see the custom keyboard again. Defaults to false.
    - `selective`: `bool` - Optional. Use this parameter if you want to show the keyboard to specific users only. Targets: 1) users that are @mentioned in the text of the Message object; 2) if the bot's message is a reply (has reply_to_message_id), sender of the original message.Example: A user requests to change the bot‘s language, bot replies to the request with a keyboard to select the new language. Other users in the group don’t see the keyboard.
    """

    def __init__(self, dictionary=None):
        if dictionary is None:
            dictionary = {}
        self.dict = dictionary
        for index, value in self.dict.items():
            if index == "keyboard" and value is not None:
                self.keyboard = list()
                for i1 in value:
                    sublist = list()
                    for i2 in i1:
                        sublist.append(KeyboardButton(i2))
                    self.keyboard.append(sublist)
            elif index == "resize_keyboard" and value is not None:
                self.resize_keyboard = value
            elif index == "one_time_keyboard" and value is not None:
                self.one_time_keyboard = value
            elif index == "selective" and value is not None:
                self.selective = value
            else:
                setattr(self, index, helper.setBvar(value))


class KeyboardButton:
    """This object represents one button of the reply keyboard. For simple text buttons String can be used instead of this object to specify text of the button. Optional fields request_contact, request_location, and request_poll are mutually exclusive.[See on Telegram API](https://core.telegram.org/bots/api#keyboardbutton)

    - - - - -
    **Fields**:

    - `text`: `string` - Text of the button. If none of the optional fields are used, it will be sent as a message when the button is pressed
    - `request_contact`: `bool` - Optional. If True, the user's phone number will be sent as a contact when the button is pressed. Available in private chats only
    - `request_location`: `bool` - Optional. If True, the user's current location will be sent when the button is pressed. Available in private chats only
    - `request_poll`: `KeyboardButtonPollType` - Optional. If specified, the user will be asked to create a poll and send it to the bot when the button is pressed. Available in private chats only
    """

    def __init__(self, dictionary=None):
        if dictionary is None:
            dictionary = {}
        self.dict = dictionary
        for index, value in self.dict.items():
            if index == "text" and value is not None:
                self.text = value
            elif index == "request_contact" and value is not None:
                self.request_contact = value
            elif index == "request_location" and value is not None:
                self.request_location = value
            elif index == "request_poll" and value is not None:
                self.request_poll = KeyboardButtonPollType(value)
            else:
                setattr(self, index, helper.setBvar(value))


class KeyboardButtonPollType:
    """This object represents type of a poll, which is allowed to be created and sent when the corresponding button is pressed.[See on Telegram API](https://core.telegram.org/bots/api#keyboardbuttonpolltype)

    - - - - -
    **Fields**:

    - `type`: `string` - Optional. If quiz is passed, the user will be allowed to create only polls in the quiz mode. If regular is passed, only regular polls will be allowed. Otherwise, the user will be allowed to create a poll of any type.
    """

    def __init__(self, dictionary=None):
        if dictionary is None:
            dictionary = {}
        self.dict = dictionary
        for index, value in self.dict.items():
            if index == "type" and value is not None:
                self.type = value
            else:
                setattr(self, index, helper.setBvar(value))


class ReplyKeyboardRemove:
    """Upon receiving a message with this object, Telegram clients will remove the current custom keyboard and display the default letter-keyboard. By default, custom keyboards are displayed until a new keyboard is sent by a bot. An exception is made for one-time keyboards that are hidden immediately after the user presses a button (see ReplyKeyboardMarkup).[See on Telegram API](https://core.telegram.org/bots/api#replykeyboardremove)

    - - - - -
    **Fields**:

    - `remove_keyboard`: `True` - Requests clients to remove the custom keyboard (user will not be able to summon this keyboard; if you want to hide the keyboard from sight but keep it accessible, use one_time_keyboard in ReplyKeyboardMarkup)
    - `selective`: `bool` - Optional. Use this parameter if you want to remove the keyboard for specific users only. Targets: 1) users that are @mentioned in the text of the Message object; 2) if the bot's message is a reply (has reply_to_message_id), sender of the original message.Example: A user votes in a poll, bot returns confirmation message in reply to the vote and removes the keyboard for that user, while still showing the keyboard with poll options to users who haven't voted yet.
    """

    def __init__(self, dictionary=None):
        if dictionary is None:
            dictionary = {}
        self.dict = dictionary
        for index, value in self.dict.items():
            if index == "remove_keyboard" and value is not None:
                self.remove_keyboard = value
            elif index == "selective" and value is not None:
                self.selective = value
            else:
                setattr(self, index, helper.setBvar(value))


class InlineKeyboardMarkup(objects.InlineKeyboardMarkup):
    """This object represents an inline keyboard that appears right next to the message it belongs to.[See on Telegram API](https://core.telegram.org/bots/api#inlinekeyboardmarkup)

    - - - - -
    **Fields**:

    - `inline_keyboard`: `InlineKeyboardButton[][]` - Array of button rows, each represented by an Array of InlineKeyboardButton objects
    """

    def __init__(self, dictionary=None):
        if dictionary is None:
            dictionary = {}
        self.dict = dictionary
        for index, value in self.dict.items():
            if index == "inline_keyboard" and value is not None:
                self.inline_keyboard = list()
                for i1 in value:
                    sublist = list()
                    for i2 in i1:
                        sublist.append(InlineKeyboardButton(i2))
                    self.inline_keyboard.append(sublist)
            else:
                setattr(self, index, helper.setBvar(value))


class InlineKeyboardButton:
    """This object represents one button of an inline keyboard. You must use exactly one of the optional fields.[See on Telegram API](https://core.telegram.org/bots/api#inlinekeyboardbutton)

    - - - - -
    **Fields**:

    - `text`: `string` - Label text on the button
    - `url`: `string` - Optional. HTTP or tg:// url to be opened when button is pressed
    - `login_url`: `LoginUrl` - Optional. An HTTP URL used to automatically authorize the user. Can be used as a replacement for the Telegram Login Widget.
    - `callback_data`: `string` - Optional. Data to be sent in a callback query to the bot when button is pressed, 1-64 bytes
    - `switch_inline_query`: `string` - Optional. If set, pressing the button will prompt the user to select one of their chats, open that chat and insert the bot‘s username and the specified inline query in the input field. Can be empty, in which case just the bot’s username will be inserted.Note: This offers an easy way for users to start using your bot in inline mode when they are currently in a private chat with it. Especially useful when combined with switch_pm… actions – in this case the user will be automatically returned to the chat they switched from, skipping the chat selection screen.
    - `switch_inline_query_current_chat`: `string` - Optional. If set, pressing the button will insert the bot‘s username and the specified inline query in the current chat’s input field. Can be empty, in which case only the bot's username will be inserted.This offers a quick way for the user to open your bot in inline mode in the same chat – good for selecting something from multiple options.
    - `callback_game`: `CallbackGame` - Optional. Description of the game that will be launched when the user presses the button.NOTE: This type of button must always be the first button in the first row.
    - `pay`: `bool` - Optional. Specify True, to send a Pay button.NOTE: This type of button must always be the first button in the first row.
    """

    def __init__(self, dictionary=None):
        if dictionary is None:
            dictionary = {}
        self.dict = dictionary
        for index, value in self.dict.items():
            if index == "text" and value is not None:
                self.text = value
            elif index == "url" and value is not None:
                self.url = value
            elif index == "login_url" and value is not None:
                self.login_url = LoginUrl(value)
            elif index == "callback_data" and value is not None:
                self.callback_data = value
            elif index == "switch_inline_query" and value is not None:
                self.switch_inline_query = value
            elif index == "switch_inline_query_current_chat" and value is not None:
                self.switch_inline_query_current_chat = value
            elif index == "callback_game" and value is not None:
                self.callback_game = CallbackGame(value)
            elif index == "pay" and value is not None:
                self.pay = value
            else:
                setattr(self, index, helper.setBvar(value))


class LoginUrl:
    """This object represents a parameter of the inline keyboard button used to automatically authorize a user. Serves as a great replacement for the Telegram Login Widget when the user is coming from Telegram. All the user needs to do is tap/click a button and confirm that they want to log in:
Telegram apps support these buttons as of version 5.7.[See on Telegram API](https://core.telegram.org/bots/api#loginurl)

    - - - - -
    **Fields**:

    - `url`: `string` - An HTTP URL to be opened with user authorization data added to the query string when the button is pressed. If the user refuses to provide authorization data, the original URL without information about the user will be opened. The data added is the same as described in Receiving authorization data.NOTE: You must always check the hash of the received data to verify the authentication and the integrity of the data as described in Checking authorization.
    - `forward_text`: `string` - Optional. New text of the button in forwarded messages.
    - `bot_username`: `string` - Optional. Username of a bot, which will be used for user authorization. See Setting up a bot for more details. If not specified, the current bot's username will be assumed. The url's domain must be the same as the domain linked with the bot. See Linking your domain to the bot for more details.
    - `request_write_access`: `bool` - Optional. Pass True to request the permission for your bot to send messages to the user.
    """

    def __init__(self, dictionary=None):
        if dictionary is None:
            dictionary = {}
        self.dict = dictionary
        for index, value in self.dict.items():
            if index == "url" and value is not None:
                self.url = value
            elif index == "forward_text" and value is not None:
                self.forward_text = value
            elif index == "bot_username" and value is not None:
                self.bot_username = value
            elif index == "request_write_access" and value is not None:
                self.request_write_access = value
            else:
                setattr(self, index, helper.setBvar(value))


class CallbackQuery(objects.CallbackQuery):
    """This object represents an incoming callback query from a callback button in an inline keyboard. If the button that originated the query was attached to a message sent by the bot, the field message will be present. If the button was attached to a message sent via the bot (in inline mode), the field inline_message_id will be present. Exactly one of the fields data or game_short_name will be present.[See on Telegram API](https://core.telegram.org/bots/api#callbackquery)

    - - - - -
    **Fields**:

    - `id`: `string` - Unique identifier for this query
    - `user`: `User` - Sender
    - `message`: `Message` - Optional. Message with the callback button that originated the query. Note that message content and message date will not be available if the message is too old
    - `inline_message_id`: `string` - Optional. Identifier of the message sent via the bot in inline mode, that originated the query.
    - `chat_instance`: `string` - Global identifier, uniquely corresponding to the chat to which the message with the callback button was sent. Useful for high scores in games.
    - `data`: `string` - Optional. Data associated with the callback button. Be aware that a bad client can send arbitrary data in this field.
    - `game_short_name`: `string` - Optional. Short name of a Game to be returned, serves as the unique identifier for the game
    """

    def __init__(self, dictionary=None):
        if dictionary is None:
            dictionary = {}
        self.dict = dictionary
        for index, value in self.dict.items():
            if index == "id" and value is not None:
                self.id = value
            elif index == "from" and value is not None:
                self.user = User(value)
            elif index == "message" and value is not None:
                self.message = Message(value)
            elif index == "inline_message_id" and value is not None:
                self.inline_message_id = value
            elif index == "chat_instance" and value is not None:
                self.chat_instance = value
            elif index == "data" and value is not None:
                self.data = value
            elif index == "game_short_name" and value is not None:
                self.game_short_name = value
            else:
                setattr(self, index, helper.setBvar(value))


class ForceReply:
    """Upon receiving a message with this object, Telegram clients will display a reply interface to the user (act as if the user has selected the bot‘s message and tapped ’Reply'). This can be extremely useful if you want to create user-friendly step-by-step interfaces without having to sacrifice privacy mode.[See on Telegram API](https://core.telegram.org/bots/api#forcereply)

    - - - - -
    **Fields**:

    - `force_reply`: `True` - Shows reply interface to the user, as if they manually selected the bot‘s message and tapped ’Reply'
    - `selective`: `bool` - Optional. Use this parameter if you want to force reply from specific users only. Targets: 1) users that are @mentioned in the text of the Message object; 2) if the bot's message is a reply (has reply_to_message_id), sender of the original message.
    """

    def __init__(self, dictionary=None):
        if dictionary is None:
            dictionary = {}
        self.dict = dictionary
        for index, value in self.dict.items():
            if index == "force_reply" and value is not None:
                self.force_reply = value
            elif index == "selective" and value is not None:
                self.selective = value
            else:
                setattr(self, index, helper.setBvar(value))


class ChatPhoto:
    """This object represents a chat photo.[See on Telegram API](https://core.telegram.org/bots/api#chatphoto)

    - - - - -
    **Fields**:

    - `small_file_id`: `string` - File identifier of small (160x160) chat photo. This file_id can be used only for photo download and only for as long as the photo is not changed.
    - `small_file_unique_id`: `string` - Unique file identifier of small (160x160) chat photo, which is supposed to be the same over time and for different bots. Can't be used to download or reuse the file.
    - `big_file_id`: `string` - File identifier of big (640x640) chat photo. This file_id can be used only for photo download and only for as long as the photo is not changed.
    - `big_file_unique_id`: `string` - Unique file identifier of big (640x640) chat photo, which is supposed to be the same over time and for different bots. Can't be used to download or reuse the file.
    """

    def __init__(self, dictionary=None):
        if dictionary is None:
            dictionary = {}
        self.dict = dictionary
        for index, value in self.dict.items():
            if index == "small_file_id" and value is not None:
                self.small_file_id = value
            elif index == "small_file_unique_id" and value is not None:
                self.small_file_unique_id = value
            elif index == "big_file_id" and value is not None:
                self.big_file_id = value
            elif index == "big_file_unique_id" and value is not None:
                self.big_file_unique_id = value
            else:
                setattr(self, index, helper.setBvar(value))


class ChatMember:
    """This object contains information about one member of a chat.[See on Telegram API](https://core.telegram.org/bots/api#chatmember)

    - - - - -
    **Fields**:

    - `user`: `User` - Information about the user
    - `status`: `string` - The member's status in the chat. Can be “creator”, “administrator”, “member”, “restricted”, “left” or “kicked”
    - `custom_title`: `string` - Optional. Owner and administrators only. Custom title for this user
    - `until_date`: `int` - Optional. Restricted and kicked only. Date when restrictions will be lifted for this user; unix time
    - `can_be_edited`: `bool` - Optional. Administrators only. True, if the bot is allowed to edit administrator privileges of that user
    - `can_post_messages`: `bool` - Optional. Administrators only. True, if the administrator can post in the channel; channels only
    - `can_edit_messages`: `bool` - Optional. Administrators only. True, if the administrator can edit messages of other users and can pin messages; channels only
    - `can_delete_messages`: `bool` - Optional. Administrators only. True, if the administrator can delete messages of other users
    - `can_restrict_members`: `bool` - Optional. Administrators only. True, if the administrator can restrict, ban or unban chat members
    - `can_promote_members`: `bool` - Optional. Administrators only. True, if the administrator can add new administrators with a subset of their own privileges or demote administrators that he has promoted, directly or indirectly (promoted by administrators that were appointed by the user)
    - `can_change_info`: `bool` - Optional. Administrators and restricted only. True, if the user is allowed to change the chat title, photo and other settings
    - `can_invite_users`: `bool` - Optional. Administrators and restricted only. True, if the user is allowed to invite new users to the chat
    - `can_pin_messages`: `bool` - Optional. Administrators and restricted only. True, if the user is allowed to pin messages; groups and supergroups only
    - `is_member`: `bool` - Optional. Restricted only. True, if the user is a member of the chat at the moment of the request
    - `can_send_messages`: `bool` - Optional. Restricted only. True, if the user is allowed to send text messages, contacts, locations and venues
    - `can_send_media_messages`: `bool` - Optional. Restricted only. True, if the user is allowed to send audios, documents, photos, videos, video notes and voice notes
    - `can_send_polls`: `bool` - Optional. Restricted only. True, if the user is allowed to send polls
    - `can_send_other_messages`: `bool` - Optional. Restricted only. True, if the user is allowed to send animations, games, stickers and use inline bots
    - `can_add_web_page_previews`: `bool` - Optional. Restricted only. True, if the user is allowed to add web page previews to their messages
    """

    def __init__(self, dictionary=None):
        if dictionary is None:
            dictionary = {}
        self.dict = dictionary
        for index, value in self.dict.items():
            if index == "user" and value is not None:
                self.user = User(value)
            elif index == "status" and value is not None:
                self.status = value
            elif index == "custom_title" and value is not None:
                self.custom_title = value
            elif index == "until_date" and value is not None:
                self.until_date = value
            elif index == "can_be_edited" and value is not None:
                self.can_be_edited = value
            elif index == "can_post_messages" and value is not None:
                self.can_post_messages = value
            elif index == "can_edit_messages" and value is not None:
                self.can_edit_messages = value
            elif index == "can_delete_messages" and value is not None:
                self.can_delete_messages = value
            elif index == "can_restrict_members" and value is not None:
                self.can_restrict_members = value
            elif index == "can_promote_members" and value is not None:
                self.can_promote_members = value
            elif index == "can_change_info" and value is not None:
                self.can_change_info = value
            elif index == "can_invite_users" and value is not None:
                self.can_invite_users = value
            elif index == "can_pin_messages" and value is not None:
                self.can_pin_messages = value
            elif index == "is_member" and value is not None:
                self.is_member = value
            elif index == "can_send_messages" and value is not None:
                self.can_send_messages = value
            elif index == "can_send_media_messages" and value is not None:
                self.can_send_media_messages = value
            elif index == "can_send_polls" and value is not None:
                self.can_send_polls = value
            elif index == "can_send_other_messages" and value is not None:
                self.can_send_other_messages = value
            elif index == "can_add_web_page_previews" and value is not None:
                self.can_add_web_page_previews = value
            else:
                setattr(self, index, helper.setBvar(value))


class ChatPermissions:
    """Describes actions that a non-administrator user is allowed to take in a chat.[See on Telegram API](https://core.telegram.org/bots/api#chatpermissions)

    - - - - -
    **Fields**:

    - `can_send_messages`: `bool` - Optional. True, if the user is allowed to send text messages, contacts, locations and venues
    - `can_send_media_messages`: `bool` - Optional. True, if the user is allowed to send audios, documents, photos, videos, video notes and voice notes, implies can_send_messages
    - `can_send_polls`: `bool` - Optional. True, if the user is allowed to send polls, implies can_send_messages
    - `can_send_other_messages`: `bool` - Optional. True, if the user is allowed to send animations, games, stickers and use inline bots, implies can_send_media_messages
    - `can_add_web_page_previews`: `bool` - Optional. True, if the user is allowed to add web page previews to their messages, implies can_send_media_messages
    - `can_change_info`: `bool` - Optional. True, if the user is allowed to change the chat title, photo and other settings. Ignored in public supergroups
    - `can_invite_users`: `bool` - Optional. True, if the user is allowed to invite new users to the chat
    - `can_pin_messages`: `bool` - Optional. True, if the user is allowed to pin messages. Ignored in public supergroups
    """

    def __init__(self, dictionary=None):
        if dictionary is None:
            dictionary = {}
        self.dict = dictionary
        for index, value in self.dict.items():
            if index == "can_send_messages" and value is not None:
                self.can_send_messages = value
            elif index == "can_send_media_messages" and value is not None:
                self.can_send_media_messages = value
            elif index == "can_send_polls" and value is not None:
                self.can_send_polls = value
            elif index == "can_send_other_messages" and value is not None:
                self.can_send_other_messages = value
            elif index == "can_add_web_page_previews" and value is not None:
                self.can_add_web_page_previews = value
            elif index == "can_change_info" and value is not None:
                self.can_change_info = value
            elif index == "can_invite_users" and value is not None:
                self.can_invite_users = value
            elif index == "can_pin_messages" and value is not None:
                self.can_pin_messages = value
            else:
                setattr(self, index, helper.setBvar(value))


class BotCommand:
    """This object represents a bot command.[See on Telegram API](https://core.telegram.org/bots/api#botcommand)

    - - - - -
    **Fields**:

    - `command`: `string` - Text of the command, 1-32 characters. Can contain only lowercase English letters, digits and underscores.
    - `description`: `string` - Description of the command, 3-256 characters.
    """

    def __init__(self, dictionary=None):
        if dictionary is None:
            dictionary = {}
        self.dict = dictionary
        for index, value in self.dict.items():
            if index == "command" and value is not None:
                self.command = value
            elif index == "description" and value is not None:
                self.description = value
            else:
                setattr(self, index, helper.setBvar(value))


class ResponseParameters:
    """Contains information about why a request was unsuccessful.[See on Telegram API](https://core.telegram.org/bots/api#responseparameters)

    - - - - -
    **Fields**:

    - `migrate_to_chat_id`: `int` - Optional. The group has been migrated to a supergroup with the specified identifier. This number may be greater than 32 bits and some programming languages may have difficulty/silent defects in interpreting it. But it is smaller than 52 bits, so a signed 64 bit integer or double-precision float type are safe for storing this identifier.
    - `retry_after`: `int` - Optional. In case of exceeding flood control, the number of seconds left to wait before the request can be repeated
    """

    def __init__(self, dictionary=None):
        if dictionary is None:
            dictionary = {}
        self.dict = dictionary
        for index, value in self.dict.items():
            if index == "migrate_to_chat_id" and value is not None:
                self.migrate_to_chat_id = value
            elif index == "retry_after" and value is not None:
                self.retry_after = value
            else:
                setattr(self, index, helper.setBvar(value))


class InputMedia:
    """This object represents the content of a media message to be sent. It should be one of[See on Telegram API](https://core.telegram.org/bots/api#inputmedia)

    - - - - -
    **Fields**:

    """

    def __init__(self, dictionary=None):
        if dictionary is None:
            dictionary = {}
        self.dict = dictionary
        for index, value in self.dict.items():
            setattr(self, index, helper.setBvar(value))


class InputMediaPhoto:
    """Represents a photo to be sent.[See on Telegram API](https://core.telegram.org/bots/api#inputmediaphoto)

    - - - - -
    **Fields**:

    - `type`: `string` - Type of the result, must be photo
    - `media`: `string` - File to send. Pass a file_id to send a file that exists on the Telegram servers (recommended), pass an HTTP URL for Telegram to get a file from the Internet, or pass “attach://<file_attach_name>” to upload a new one using multipart/form-data under <file_attach_name> name. More info on Sending Files »
    - `caption`: `string` - Optional. Caption of the photo to be sent, 0-1024 characters after entities parsing
    - `parse_mode`: `string` - Optional. Mode for parsing entities in the photo caption. See formatting options for more details.
    """

    def __init__(self, dictionary=None):
        if dictionary is None:
            dictionary = {}
        self.dict = dictionary
        for index, value in self.dict.items():
            if index == "type" and value is not None:
                self.type = value
            elif index == "media" and value is not None:
                self.media = value
            elif index == "caption" and value is not None:
                self.caption = value
            elif index == "parse_mode" and value is not None:
                self.parse_mode = value
            else:
                setattr(self, index, helper.setBvar(value))


class InputMediaVideo:
    """Represents a video to be sent.[See on Telegram API](https://core.telegram.org/bots/api#inputmediavideo)

    - - - - -
    **Fields**:

    - `type`: `string` - Type of the result, must be video
    - `media`: `string` - File to send. Pass a file_id to send a file that exists on the Telegram servers (recommended), pass an HTTP URL for Telegram to get a file from the Internet, or pass “attach://<file_attach_name>” to upload a new one using multipart/form-data under <file_attach_name> name. More info on Sending Files »
    - `caption`: `string` - Optional. Caption of the video to be sent, 0-1024 characters after entities parsing
    - `parse_mode`: `string` - Optional. Mode for parsing entities in the video caption. See formatting options for more details.
    - `width`: `int` - Optional. Video width
    - `height`: `int` - Optional. Video height
    - `duration`: `int` - Optional. Video duration
    - `supports_streaming`: `bool` - Optional. Pass True, if the uploaded video is suitable for streaming
    """

    def __init__(self, dictionary=None):
        if dictionary is None:
            dictionary = {}
        self.dict = dictionary
        for index, value in self.dict.items():
            if index == "type" and value is not None:
                self.type = value
            elif index == "media" and value is not None:
                self.media = value
            elif index == "caption" and value is not None:
                self.caption = value
            elif index == "parse_mode" and value is not None:
                self.parse_mode = value
            elif index == "width" and value is not None:
                self.width = value
            elif index == "height" and value is not None:
                self.height = value
            elif index == "duration" and value is not None:
                self.duration = value
            elif index == "supports_streaming" and value is not None:
                self.supports_streaming = value
            else:
                setattr(self, index, helper.setBvar(value))


class InputMediaAnimation:
    """Represents an animation file (GIF or H.264/MPEG-4 AVC video without sound) to be sent.[See on Telegram API](https://core.telegram.org/bots/api#inputmediaanimation)

    - - - - -
    **Fields**:

    - `type`: `string` - Type of the result, must be animation
    - `media`: `string` - File to send. Pass a file_id to send a file that exists on the Telegram servers (recommended), pass an HTTP URL for Telegram to get a file from the Internet, or pass “attach://<file_attach_name>” to upload a new one using multipart/form-data under <file_attach_name> name. More info on Sending Files »
    - `caption`: `string` - Optional. Caption of the animation to be sent, 0-1024 characters after entities parsing
    - `parse_mode`: `string` - Optional. Mode for parsing entities in the animation caption. See formatting options for more details.
    - `width`: `int` - Optional. Animation width
    - `height`: `int` - Optional. Animation height
    - `duration`: `int` - Optional. Animation duration
    """

    def __init__(self, dictionary=None):
        if dictionary is None:
            dictionary = {}
        self.dict = dictionary
        for index, value in self.dict.items():
            if index == "type" and value is not None:
                self.type = value
            elif index == "media" and value is not None:
                self.media = value
            elif index == "caption" and value is not None:
                self.caption = value
            elif index == "parse_mode" and value is not None:
                self.parse_mode = value
            elif index == "width" and value is not None:
                self.width = value
            elif index == "height" and value is not None:
                self.height = value
            elif index == "duration" and value is not None:
                self.duration = value
            else:
                setattr(self, index, helper.setBvar(value))


class InputMediaAudio:
    """Represents an audio file to be treated as music to be sent.[See on Telegram API](https://core.telegram.org/bots/api#inputmediaaudio)

    - - - - -
    **Fields**:

    - `type`: `string` - Type of the result, must be audio
    - `media`: `string` - File to send. Pass a file_id to send a file that exists on the Telegram servers (recommended), pass an HTTP URL for Telegram to get a file from the Internet, or pass “attach://<file_attach_name>” to upload a new one using multipart/form-data under <file_attach_name> name. More info on Sending Files »
    - `caption`: `string` - Optional. Caption of the audio to be sent, 0-1024 characters after entities parsing
    - `parse_mode`: `string` - Optional. Mode for parsing entities in the audio caption. See formatting options for more details.
    - `duration`: `int` - Optional. Duration of the audio in seconds
    - `performer`: `string` - Optional. Performer of the audio
    - `title`: `string` - Optional. Title of the audio
    """

    def __init__(self, dictionary=None):
        if dictionary is None:
            dictionary = {}
        self.dict = dictionary
        for index, value in self.dict.items():
            if index == "type" and value is not None:
                self.type = value
            elif index == "media" and value is not None:
                self.media = value
            elif index == "caption" and value is not None:
                self.caption = value
            elif index == "parse_mode" and value is not None:
                self.parse_mode = value
            elif index == "duration" and value is not None:
                self.duration = value
            elif index == "performer" and value is not None:
                self.performer = value
            elif index == "title" and value is not None:
                self.title = value
            else:
                setattr(self, index, helper.setBvar(value))


class InputMediaDocument:
    """Represents a general file to be sent.[See on Telegram API](https://core.telegram.org/bots/api#inputmediadocument)

    - - - - -
    **Fields**:

    - `type`: `string` - Type of the result, must be document
    - `media`: `string` - File to send. Pass a file_id to send a file that exists on the Telegram servers (recommended), pass an HTTP URL for Telegram to get a file from the Internet, or pass “attach://<file_attach_name>” to upload a new one using multipart/form-data under <file_attach_name> name. More info on Sending Files »
    - `caption`: `string` - Optional. Caption of the document to be sent, 0-1024 characters after entities parsing
    - `parse_mode`: `string` - Optional. Mode for parsing entities in the document caption. See formatting options for more details.
    """

    def __init__(self, dictionary=None):
        if dictionary is None:
            dictionary = {}
        self.dict = dictionary
        for index, value in self.dict.items():
            if index == "type" and value is not None:
                self.type = value
            elif index == "media" and value is not None:
                self.media = value
            elif index == "caption" and value is not None:
                self.caption = value
            elif index == "parse_mode" and value is not None:
                self.parse_mode = value
            else:
                setattr(self, index, helper.setBvar(value))


class InputFile:
    """This object represents the contents of a file to be uploaded. Must be posted using multipart/form-data in the usual way that files are uploaded via the browser.[See on Telegram API](https://core.telegram.org/bots/api#inputfile)

    - - - - -
    **Fields**:

    """

    def __init__(self, dictionary=None):
        if dictionary is None:
            dictionary = {}
        self.dict = dictionary
        for index, value in self.dict.items():
            setattr(self, index, helper.setBvar(value))


class Sticker:
    """This object represents a sticker.[See on Telegram API](https://core.telegram.org/bots/api#sticker)

    - - - - -
    **Fields**:

    - `file_id`: `string` - Identifier for this file, which can be used to download or reuse the file
    - `file_unique_id`: `string` - Unique identifier for this file, which is supposed to be the same over time and for different bots. Can't be used to download or reuse the file.
    - `width`: `int` - Sticker width
    - `height`: `int` - Sticker height
    - `is_animated`: `bool` - True, if the sticker is animated
    - `thumb`: `PhotoSize` - Optional. Sticker thumbnail in the .WEBP or .JPG format
    - `emoji`: `string` - Optional. Emoji associated with the sticker
    - `set_name`: `string` - Optional. Name of the sticker set to which the sticker belongs
    - `mask_position`: `MaskPosition` - Optional. For mask stickers, the position where the mask should be placed
    - `file_size`: `int` - Optional. File size
    """

    def __init__(self, dictionary=None):
        if dictionary is None:
            dictionary = {}
        self.dict = dictionary
        for index, value in self.dict.items():
            if index == "file_id" and value is not None:
                self.file_id = value
            elif index == "file_unique_id" and value is not None:
                self.file_unique_id = value
            elif index == "width" and value is not None:
                self.width = value
            elif index == "height" and value is not None:
                self.height = value
            elif index == "is_animated" and value is not None:
                self.is_animated = value
            elif index == "thumb" and value is not None:
                self.thumb = PhotoSize(value)
            elif index == "emoji" and value is not None:
                self.emoji = value
            elif index == "set_name" and value is not None:
                self.set_name = value
            elif index == "mask_position" and value is not None:
                self.mask_position = MaskPosition(value)
            elif index == "file_size" and value is not None:
                self.file_size = value
            else:
                setattr(self, index, helper.setBvar(value))


class StickerSet:
    """This object represents a sticker set.[See on Telegram API](https://core.telegram.org/bots/api#stickerset)

    - - - - -
    **Fields**:

    - `name`: `string` - Sticker set name
    - `title`: `string` - Sticker set title
    - `is_animated`: `bool` - True, if the sticker set contains animated stickers
    - `contains_masks`: `bool` - True, if the sticker set contains masks
    - `stickers`: `Sticker[]` - List of all set stickers
    - `thumb`: `PhotoSize` - Optional. Sticker set thumbnail in the .WEBP or .TGS format
    """

    def __init__(self, dictionary=None):
        if dictionary is None:
            dictionary = {}
        self.dict = dictionary
        for index, value in self.dict.items():
            if index == "name" and value is not None:
                self.name = value
            elif index == "title" and value is not None:
                self.title = value
            elif index == "is_animated" and value is not None:
                self.is_animated = value
            elif index == "contains_masks" and value is not None:
                self.contains_masks = value
            elif index == "stickers" and value is not None:
                self.stickers = list()
                for i1 in value:
                    self.stickers.append(Sticker(i1))
            elif index == "thumb" and value is not None:
                self.thumb = PhotoSize(value)
            else:
                setattr(self, index, helper.setBvar(value))


class MaskPosition:
    """This object describes the position on faces where a mask should be placed by default.[See on Telegram API](https://core.telegram.org/bots/api#maskposition)

    - - - - -
    **Fields**:

    - `point`: `string` - The part of the face relative to which the mask should be placed. One of “forehead”, “eyes”, “mouth”, or “chin”.
    - `x_shift`: `float` - Shift by X-axis measured in widths of the mask scaled to the face size, from left to right. For example, choosing -1.0 will place mask just to the left of the default mask position.
    - `y_shift`: `float` - Shift by Y-axis measured in heights of the mask scaled to the face size, from top to bottom. For example, 1.0 will place the mask just below the default mask position.
    - `scale`: `float` - Mask scaling coefficient. For example, 2.0 means double size.
    """

    def __init__(self, dictionary=None):
        if dictionary is None:
            dictionary = {}
        self.dict = dictionary
        for index, value in self.dict.items():
            if index == "point" and value is not None:
                self.point = value
            elif index == "x_shift" and value is not None:
                self.x_shift = value
            elif index == "y_shift" and value is not None:
                self.y_shift = value
            elif index == "scale" and value is not None:
                self.scale = value
            else:
                setattr(self, index, helper.setBvar(value))


class InlineQuery:
    """This object represents an incoming inline query. When the user sends an empty query, your bot could return some default or trending results.[See on Telegram API](https://core.telegram.org/bots/api#inlinequery)

    - - - - -
    **Fields**:

    - `id`: `string` - Unique identifier for this query
    - `user`: `User` - Sender
    - `location`: `Location` - Optional. Sender location, only for bots that request user location
    - `query`: `string` - Text of the query (up to 256 characters)
    - `offset`: `string` - Offset of the results to be returned, can be controlled by the bot
    """

    def __init__(self, dictionary=None):
        if dictionary is None:
            dictionary = {}
        self.dict = dictionary
        for index, value in self.dict.items():
            if index == "id" and value is not None:
                self.id = value
            elif index == "from" and value is not None:
                self.user = User(value)
            elif index == "location" and value is not None:
                self.location = Location(value)
            elif index == "query" and value is not None:
                self.query = value
            elif index == "offset" and value is not None:
                self.offset = value
            else:
                setattr(self, index, helper.setBvar(value))


class InlineQueryResult:
    """This object represents one result of an inline query. Telegram clients currently support results of the following 20 types:[See on Telegram API](https://core.telegram.org/bots/api#inlinequeryresult)

    - - - - -
    **Fields**:

    """

    def __init__(self, dictionary=None):
        if dictionary is None:
            dictionary = {}
        self.dict = dictionary
        for index, value in self.dict.items():
            setattr(self, index, helper.setBvar(value))


class InlineQueryResultArticle:
    """Represents a link to an article or web page.[See on Telegram API](https://core.telegram.org/bots/api#inlinequeryresultarticle)

    - - - - -
    **Fields**:

    - `type`: `string` - Type of the result, must be article
    - `id`: `string` - Unique identifier for this result, 1-64 Bytes
    - `title`: `string` - Title of the result
    - `input_message_content`: `InputMessageContent` - Content of the message to be sent
    - `reply_markup`: `InlineKeyboardMarkup` - Optional. Inline keyboard attached to the message
    - `url`: `string` - Optional. URL of the result
    - `hide_url`: `bool` - Optional. Pass True, if you don't want the URL to be shown in the message
    - `description`: `string` - Optional. Short description of the result
    - `thumb_url`: `string` - Optional. Url of the thumbnail for the result
    - `thumb_width`: `int` - Optional. Thumbnail width
    - `thumb_height`: `int` - Optional. Thumbnail height
    """

    def __init__(self, dictionary=None):
        if dictionary is None:
            dictionary = {}
        self.dict = dictionary
        for index, value in self.dict.items():
            if index == "type" and value is not None:
                self.type = value
            elif index == "id" and value is not None:
                self.id = value
            elif index == "title" and value is not None:
                self.title = value
            elif index == "input_message_content" and value is not None:
                self.input_message_content = InputMessageContent(value)
            elif index == "reply_markup" and value is not None:
                self.reply_markup = InlineKeyboardMarkup(value)
            elif index == "url" and value is not None:
                self.url = value
            elif index == "hide_url" and value is not None:
                self.hide_url = value
            elif index == "description" and value is not None:
                self.description = value
            elif index == "thumb_url" and value is not None:
                self.thumb_url = value
            elif index == "thumb_width" and value is not None:
                self.thumb_width = value
            elif index == "thumb_height" and value is not None:
                self.thumb_height = value
            else:
                setattr(self, index, helper.setBvar(value))


class InlineQueryResultPhoto:
    """Represents a link to a photo. By default, this photo will be sent by the user with optional caption. Alternatively, you can use input_message_content to send a message with the specified content instead of the photo.[See on Telegram API](https://core.telegram.org/bots/api#inlinequeryresultphoto)

    - - - - -
    **Fields**:

    - `type`: `string` - Type of the result, must be photo
    - `id`: `string` - Unique identifier for this result, 1-64 bytes
    - `photo_url`: `string` - A valid URL of the photo. Photo must be in jpeg format. Photo size must not exceed 5MB
    - `thumb_url`: `string` - URL of the thumbnail for the photo
    - `photo_width`: `int` - Optional. Width of the photo
    - `photo_height`: `int` - Optional. Height of the photo
    - `title`: `string` - Optional. Title for the result
    - `description`: `string` - Optional. Short description of the result
    - `caption`: `string` - Optional. Caption of the photo to be sent, 0-1024 characters after entities parsing
    - `parse_mode`: `string` - Optional. Mode for parsing entities in the photo caption. See formatting options for more details.
    - `reply_markup`: `InlineKeyboardMarkup` - Optional. Inline keyboard attached to the message
    - `input_message_content`: `InputMessageContent` - Optional. Content of the message to be sent instead of the photo
    """

    def __init__(self, dictionary=None):
        if dictionary is None:
            dictionary = {}
        self.dict = dictionary
        for index, value in self.dict.items():
            if index == "type" and value is not None:
                self.type = value
            elif index == "id" and value is not None:
                self.id = value
            elif index == "photo_url" and value is not None:
                self.photo_url = value
            elif index == "thumb_url" and value is not None:
                self.thumb_url = value
            elif index == "photo_width" and value is not None:
                self.photo_width = value
            elif index == "photo_height" and value is not None:
                self.photo_height = value
            elif index == "title" and value is not None:
                self.title = value
            elif index == "description" and value is not None:
                self.description = value
            elif index == "caption" and value is not None:
                self.caption = value
            elif index == "parse_mode" and value is not None:
                self.parse_mode = value
            elif index == "reply_markup" and value is not None:
                self.reply_markup = InlineKeyboardMarkup(value)
            elif index == "input_message_content" and value is not None:
                self.input_message_content = InputMessageContent(value)
            else:
                setattr(self, index, helper.setBvar(value))


class InlineQueryResultGif:
    """Represents a link to an animated GIF file. By default, this animated GIF file will be sent by the user with optional caption. Alternatively, you can use input_message_content to send a message with the specified content instead of the animation.[See on Telegram API](https://core.telegram.org/bots/api#inlinequeryresultgif)

    - - - - -
    **Fields**:

    - `type`: `string` - Type of the result, must be gif
    - `id`: `string` - Unique identifier for this result, 1-64 bytes
    - `gif_url`: `string` - A valid URL for the GIF file. File size must not exceed 1MB
    - `gif_width`: `int` - Optional. Width of the GIF
    - `gif_height`: `int` - Optional. Height of the GIF
    - `gif_duration`: `int` - Optional. Duration of the GIF
    - `thumb_url`: `string` - URL of the static thumbnail for the result (jpeg or gif)
    - `title`: `string` - Optional. Title for the result
    - `caption`: `string` - Optional. Caption of the GIF file to be sent, 0-1024 characters after entities parsing
    - `parse_mode`: `string` - Optional. Mode for parsing entities in the caption. See formatting options for more details.
    - `reply_markup`: `InlineKeyboardMarkup` - Optional. Inline keyboard attached to the message
    - `input_message_content`: `InputMessageContent` - Optional. Content of the message to be sent instead of the GIF animation
    """

    def __init__(self, dictionary=None):
        if dictionary is None:
            dictionary = {}
        self.dict = dictionary
        for index, value in self.dict.items():
            if index == "type" and value is not None:
                self.type = value
            elif index == "id" and value is not None:
                self.id = value
            elif index == "gif_url" and value is not None:
                self.gif_url = value
            elif index == "gif_width" and value is not None:
                self.gif_width = value
            elif index == "gif_height" and value is not None:
                self.gif_height = value
            elif index == "gif_duration" and value is not None:
                self.gif_duration = value
            elif index == "thumb_url" and value is not None:
                self.thumb_url = value
            elif index == "title" and value is not None:
                self.title = value
            elif index == "caption" and value is not None:
                self.caption = value
            elif index == "parse_mode" and value is not None:
                self.parse_mode = value
            elif index == "reply_markup" and value is not None:
                self.reply_markup = InlineKeyboardMarkup(value)
            elif index == "input_message_content" and value is not None:
                self.input_message_content = InputMessageContent(value)
            else:
                setattr(self, index, helper.setBvar(value))


class InlineQueryResultMpeg4Gif:
    """Represents a link to a video animation (H.264/MPEG-4 AVC video without sound). By default, this animated MPEG-4 file will be sent by the user with optional caption. Alternatively, you can use input_message_content to send a message with the specified content instead of the animation.[See on Telegram API](https://core.telegram.org/bots/api#inlinequeryresultmpeg4gif)

    - - - - -
    **Fields**:

    - `type`: `string` - Type of the result, must be mpeg4_gif
    - `id`: `string` - Unique identifier for this result, 1-64 bytes
    - `mpeg4_url`: `string` - A valid URL for the MP4 file. File size must not exceed 1MB
    - `mpeg4_width`: `int` - Optional. Video width
    - `mpeg4_height`: `int` - Optional. Video height
    - `mpeg4_duration`: `int` - Optional. Video duration
    - `thumb_url`: `string` - URL of the static thumbnail (jpeg or gif) for the result
    - `title`: `string` - Optional. Title for the result
    - `caption`: `string` - Optional. Caption of the MPEG-4 file to be sent, 0-1024 characters after entities parsing
    - `parse_mode`: `string` - Optional. Mode for parsing entities in the caption. See formatting options for more details.
    - `reply_markup`: `InlineKeyboardMarkup` - Optional. Inline keyboard attached to the message
    - `input_message_content`: `InputMessageContent` - Optional. Content of the message to be sent instead of the video animation
    """

    def __init__(self, dictionary=None):
        if dictionary is None:
            dictionary = {}
        self.dict = dictionary
        for index, value in self.dict.items():
            if index == "type" and value is not None:
                self.type = value
            elif index == "id" and value is not None:
                self.id = value
            elif index == "mpeg4_url" and value is not None:
                self.mpeg4_url = value
            elif index == "mpeg4_width" and value is not None:
                self.mpeg4_width = value
            elif index == "mpeg4_height" and value is not None:
                self.mpeg4_height = value
            elif index == "mpeg4_duration" and value is not None:
                self.mpeg4_duration = value
            elif index == "thumb_url" and value is not None:
                self.thumb_url = value
            elif index == "title" and value is not None:
                self.title = value
            elif index == "caption" and value is not None:
                self.caption = value
            elif index == "parse_mode" and value is not None:
                self.parse_mode = value
            elif index == "reply_markup" and value is not None:
                self.reply_markup = InlineKeyboardMarkup(value)
            elif index == "input_message_content" and value is not None:
                self.input_message_content = InputMessageContent(value)
            else:
                setattr(self, index, helper.setBvar(value))


class InlineQueryResultVideo:
    """Represents a link to a page containing an embedded video player or a video file. By default, this video file will be sent by the user with an optional caption. Alternatively, you can use input_message_content to send a message with the specified content instead of the video.[See on Telegram API](https://core.telegram.org/bots/api#inlinequeryresultvideo)

    - - - - -
    **Fields**:

    - `type`: `string` - Type of the result, must be video
    - `id`: `string` - Unique identifier for this result, 1-64 bytes
    - `video_url`: `string` - A valid URL for the embedded video player or video file
    - `mime_type`: `string` - Mime type of the content of video url, “text/html” or “video/mp4”
    - `thumb_url`: `string` - URL of the thumbnail (jpeg only) for the video
    - `title`: `string` - Title for the result
    - `caption`: `string` - Optional. Caption of the video to be sent, 0-1024 characters after entities parsing
    - `parse_mode`: `string` - Optional. Mode for parsing entities in the video caption. See formatting options for more details.
    - `video_width`: `int` - Optional. Video width
    - `video_height`: `int` - Optional. Video height
    - `video_duration`: `int` - Optional. Video duration in seconds
    - `description`: `string` - Optional. Short description of the result
    - `reply_markup`: `InlineKeyboardMarkup` - Optional. Inline keyboard attached to the message
    - `input_message_content`: `InputMessageContent` - Optional. Content of the message to be sent instead of the video. This field is required if InlineQueryResultVideo is used to send an HTML-page as a result (e.g., a YouTube video).
    """

    def __init__(self, dictionary=None):
        if dictionary is None:
            dictionary = {}
        self.dict = dictionary
        for index, value in self.dict.items():
            if index == "type" and value is not None:
                self.type = value
            elif index == "id" and value is not None:
                self.id = value
            elif index == "video_url" and value is not None:
                self.video_url = value
            elif index == "mime_type" and value is not None:
                self.mime_type = value
            elif index == "thumb_url" and value is not None:
                self.thumb_url = value
            elif index == "title" and value is not None:
                self.title = value
            elif index == "caption" and value is not None:
                self.caption = value
            elif index == "parse_mode" and value is not None:
                self.parse_mode = value
            elif index == "video_width" and value is not None:
                self.video_width = value
            elif index == "video_height" and value is not None:
                self.video_height = value
            elif index == "video_duration" and value is not None:
                self.video_duration = value
            elif index == "description" and value is not None:
                self.description = value
            elif index == "reply_markup" and value is not None:
                self.reply_markup = InlineKeyboardMarkup(value)
            elif index == "input_message_content" and value is not None:
                self.input_message_content = InputMessageContent(value)
            else:
                setattr(self, index, helper.setBvar(value))


class InlineQueryResultAudio:
    """Represents a link to an MP3 audio file. By default, this audio file will be sent by the user. Alternatively, you can use input_message_content to send a message with the specified content instead of the audio.[See on Telegram API](https://core.telegram.org/bots/api#inlinequeryresultaudio)

    - - - - -
    **Fields**:

    - `type`: `string` - Type of the result, must be audio
    - `id`: `string` - Unique identifier for this result, 1-64 bytes
    - `audio_url`: `string` - A valid URL for the audio file
    - `title`: `string` - Title
    - `caption`: `string` - Optional. Caption, 0-1024 characters after entities parsing
    - `parse_mode`: `string` - Optional. Mode for parsing entities in the audio caption. See formatting options for more details.
    - `performer`: `string` - Optional. Performer
    - `audio_duration`: `int` - Optional. Audio duration in seconds
    - `reply_markup`: `InlineKeyboardMarkup` - Optional. Inline keyboard attached to the message
    - `input_message_content`: `InputMessageContent` - Optional. Content of the message to be sent instead of the audio
    """

    def __init__(self, dictionary=None):
        if dictionary is None:
            dictionary = {}
        self.dict = dictionary
        for index, value in self.dict.items():
            if index == "type" and value is not None:
                self.type = value
            elif index == "id" and value is not None:
                self.id = value
            elif index == "audio_url" and value is not None:
                self.audio_url = value
            elif index == "title" and value is not None:
                self.title = value
            elif index == "caption" and value is not None:
                self.caption = value
            elif index == "parse_mode" and value is not None:
                self.parse_mode = value
            elif index == "performer" and value is not None:
                self.performer = value
            elif index == "audio_duration" and value is not None:
                self.audio_duration = value
            elif index == "reply_markup" and value is not None:
                self.reply_markup = InlineKeyboardMarkup(value)
            elif index == "input_message_content" and value is not None:
                self.input_message_content = InputMessageContent(value)
            else:
                setattr(self, index, helper.setBvar(value))


class InlineQueryResultVoice:
    """Represents a link to a voice recording in an .OGG container encoded with OPUS. By default, this voice recording will be sent by the user. Alternatively, you can use input_message_content to send a message with the specified content instead of the the voice message.[See on Telegram API](https://core.telegram.org/bots/api#inlinequeryresultvoice)

    - - - - -
    **Fields**:

    - `type`: `string` - Type of the result, must be voice
    - `id`: `string` - Unique identifier for this result, 1-64 bytes
    - `voice_url`: `string` - A valid URL for the voice recording
    - `title`: `string` - Recording title
    - `caption`: `string` - Optional. Caption, 0-1024 characters after entities parsing
    - `parse_mode`: `string` - Optional. Mode for parsing entities in the voice message caption. See formatting options for more details.
    - `voice_duration`: `int` - Optional. Recording duration in seconds
    - `reply_markup`: `InlineKeyboardMarkup` - Optional. Inline keyboard attached to the message
    - `input_message_content`: `InputMessageContent` - Optional. Content of the message to be sent instead of the voice recording
    """

    def __init__(self, dictionary=None):
        if dictionary is None:
            dictionary = {}
        self.dict = dictionary
        for index, value in self.dict.items():
            if index == "type" and value is not None:
                self.type = value
            elif index == "id" and value is not None:
                self.id = value
            elif index == "voice_url" and value is not None:
                self.voice_url = value
            elif index == "title" and value is not None:
                self.title = value
            elif index == "caption" and value is not None:
                self.caption = value
            elif index == "parse_mode" and value is not None:
                self.parse_mode = value
            elif index == "voice_duration" and value is not None:
                self.voice_duration = value
            elif index == "reply_markup" and value is not None:
                self.reply_markup = InlineKeyboardMarkup(value)
            elif index == "input_message_content" and value is not None:
                self.input_message_content = InputMessageContent(value)
            else:
                setattr(self, index, helper.setBvar(value))


class InlineQueryResultDocument:
    """Represents a link to a file. By default, this file will be sent by the user with an optional caption. Alternatively, you can use input_message_content to send a message with the specified content instead of the file. Currently, only .PDF and .ZIP files can be sent using this method.[See on Telegram API](https://core.telegram.org/bots/api#inlinequeryresultdocument)

    - - - - -
    **Fields**:

    - `type`: `string` - Type of the result, must be document
    - `id`: `string` - Unique identifier for this result, 1-64 bytes
    - `title`: `string` - Title for the result
    - `caption`: `string` - Optional. Caption of the document to be sent, 0-1024 characters after entities parsing
    - `parse_mode`: `string` - Optional. Mode for parsing entities in the document caption. See formatting options for more details.
    - `document_url`: `string` - A valid URL for the file
    - `mime_type`: `string` - Mime type of the content of the file, either “application/pdf” or “application/zip”
    - `description`: `string` - Optional. Short description of the result
    - `reply_markup`: `InlineKeyboardMarkup` - Optional. Inline keyboard attached to the message
    - `input_message_content`: `InputMessageContent` - Optional. Content of the message to be sent instead of the file
    - `thumb_url`: `string` - Optional. URL of the thumbnail (jpeg only) for the file
    - `thumb_width`: `int` - Optional. Thumbnail width
    - `thumb_height`: `int` - Optional. Thumbnail height
    """

    def __init__(self, dictionary=None):
        if dictionary is None:
            dictionary = {}
        self.dict = dictionary
        for index, value in self.dict.items():
            if index == "type" and value is not None:
                self.type = value
            elif index == "id" and value is not None:
                self.id = value
            elif index == "title" and value is not None:
                self.title = value
            elif index == "caption" and value is not None:
                self.caption = value
            elif index == "parse_mode" and value is not None:
                self.parse_mode = value
            elif index == "document_url" and value is not None:
                self.document_url = value
            elif index == "mime_type" and value is not None:
                self.mime_type = value
            elif index == "description" and value is not None:
                self.description = value
            elif index == "reply_markup" and value is not None:
                self.reply_markup = InlineKeyboardMarkup(value)
            elif index == "input_message_content" and value is not None:
                self.input_message_content = InputMessageContent(value)
            elif index == "thumb_url" and value is not None:
                self.thumb_url = value
            elif index == "thumb_width" and value is not None:
                self.thumb_width = value
            elif index == "thumb_height" and value is not None:
                self.thumb_height = value
            else:
                setattr(self, index, helper.setBvar(value))


class InlineQueryResultLocation:
    """Represents a location on a map. By default, the location will be sent by the user. Alternatively, you can use input_message_content to send a message with the specified content instead of the location.[See on Telegram API](https://core.telegram.org/bots/api#inlinequeryresultlocation)

    - - - - -
    **Fields**:

    - `type`: `string` - Type of the result, must be location
    - `id`: `string` - Unique identifier for this result, 1-64 Bytes
    - `latitude`: `float` - Location latitude in degrees
    - `longitude`: `float` - Location longitude in degrees
    - `title`: `string` - Location title
    - `live_period`: `int` - Optional. Period in seconds for which the location can be updated, should be between 60 and 86400.
    - `reply_markup`: `InlineKeyboardMarkup` - Optional. Inline keyboard attached to the message
    - `input_message_content`: `InputMessageContent` - Optional. Content of the message to be sent instead of the location
    - `thumb_url`: `string` - Optional. Url of the thumbnail for the result
    - `thumb_width`: `int` - Optional. Thumbnail width
    - `thumb_height`: `int` - Optional. Thumbnail height
    """

    def __init__(self, dictionary=None):
        if dictionary is None:
            dictionary = {}
        self.dict = dictionary
        for index, value in self.dict.items():
            if index == "type" and value is not None:
                self.type = value
            elif index == "id" and value is not None:
                self.id = value
            elif index == "latitude" and value is not None:
                self.latitude = value
            elif index == "longitude" and value is not None:
                self.longitude = value
            elif index == "title" and value is not None:
                self.title = value
            elif index == "live_period" and value is not None:
                self.live_period = value
            elif index == "reply_markup" and value is not None:
                self.reply_markup = InlineKeyboardMarkup(value)
            elif index == "input_message_content" and value is not None:
                self.input_message_content = InputMessageContent(value)
            elif index == "thumb_url" and value is not None:
                self.thumb_url = value
            elif index == "thumb_width" and value is not None:
                self.thumb_width = value
            elif index == "thumb_height" and value is not None:
                self.thumb_height = value
            else:
                setattr(self, index, helper.setBvar(value))


class InlineQueryResultVenue:
    """Represents a venue. By default, the venue will be sent by the user. Alternatively, you can use input_message_content to send a message with the specified content instead of the venue.[See on Telegram API](https://core.telegram.org/bots/api#inlinequeryresultvenue)

    - - - - -
    **Fields**:

    - `type`: `string` - Type of the result, must be venue
    - `id`: `string` - Unique identifier for this result, 1-64 Bytes
    - `latitude`: `float` - Latitude of the venue location in degrees
    - `longitude`: `float` - Longitude of the venue location in degrees
    - `title`: `string` - Title of the venue
    - `address`: `string` - Address of the venue
    - `foursquare_id`: `string` - Optional. Foursquare identifier of the venue if known
    - `foursquare_type`: `string` - Optional. Foursquare type of the venue, if known. (For example, “arts_entertainment/default”, “arts_entertainment/aquarium” or “food/icecream”.)
    - `reply_markup`: `InlineKeyboardMarkup` - Optional. Inline keyboard attached to the message
    - `input_message_content`: `InputMessageContent` - Optional. Content of the message to be sent instead of the venue
    - `thumb_url`: `string` - Optional. Url of the thumbnail for the result
    - `thumb_width`: `int` - Optional. Thumbnail width
    - `thumb_height`: `int` - Optional. Thumbnail height
    """

    def __init__(self, dictionary=None):
        if dictionary is None:
            dictionary = {}
        self.dict = dictionary
        for index, value in self.dict.items():
            if index == "type" and value is not None:
                self.type = value
            elif index == "id" and value is not None:
                self.id = value
            elif index == "latitude" and value is not None:
                self.latitude = value
            elif index == "longitude" and value is not None:
                self.longitude = value
            elif index == "title" and value is not None:
                self.title = value
            elif index == "address" and value is not None:
                self.address = value
            elif index == "foursquare_id" and value is not None:
                self.foursquare_id = value
            elif index == "foursquare_type" and value is not None:
                self.foursquare_type = value
            elif index == "reply_markup" and value is not None:
                self.reply_markup = InlineKeyboardMarkup(value)
            elif index == "input_message_content" and value is not None:
                self.input_message_content = InputMessageContent(value)
            elif index == "thumb_url" and value is not None:
                self.thumb_url = value
            elif index == "thumb_width" and value is not None:
                self.thumb_width = value
            elif index == "thumb_height" and value is not None:
                self.thumb_height = value
            else:
                setattr(self, index, helper.setBvar(value))


class InlineQueryResultContact:
    """Represents a contact with a phone number. By default, this contact will be sent by the user. Alternatively, you can use input_message_content to send a message with the specified content instead of the contact.[See on Telegram API](https://core.telegram.org/bots/api#inlinequeryresultcontact)

    - - - - -
    **Fields**:

    - `type`: `string` - Type of the result, must be contact
    - `id`: `string` - Unique identifier for this result, 1-64 Bytes
    - `phone_number`: `string` - Contact's phone number
    - `first_name`: `string` - Contact's first name
    - `last_name`: `string` - Optional. Contact's last name
    - `vcard`: `string` - Optional. Additional data about the contact in the form of a vCard, 0-2048 bytes
    - `reply_markup`: `InlineKeyboardMarkup` - Optional. Inline keyboard attached to the message
    - `input_message_content`: `InputMessageContent` - Optional. Content of the message to be sent instead of the contact
    - `thumb_url`: `string` - Optional. Url of the thumbnail for the result
    - `thumb_width`: `int` - Optional. Thumbnail width
    - `thumb_height`: `int` - Optional. Thumbnail height
    """

    def __init__(self, dictionary=None):
        if dictionary is None:
            dictionary = {}
        self.dict = dictionary
        for index, value in self.dict.items():
            if index == "type" and value is not None:
                self.type = value
            elif index == "id" and value is not None:
                self.id = value
            elif index == "phone_number" and value is not None:
                self.phone_number = value
            elif index == "first_name" and value is not None:
                self.first_name = value
            elif index == "last_name" and value is not None:
                self.last_name = value
            elif index == "vcard" and value is not None:
                self.vcard = value
            elif index == "reply_markup" and value is not None:
                self.reply_markup = InlineKeyboardMarkup(value)
            elif index == "input_message_content" and value is not None:
                self.input_message_content = InputMessageContent(value)
            elif index == "thumb_url" and value is not None:
                self.thumb_url = value
            elif index == "thumb_width" and value is not None:
                self.thumb_width = value
            elif index == "thumb_height" and value is not None:
                self.thumb_height = value
            else:
                setattr(self, index, helper.setBvar(value))


class InlineQueryResultGame:
    """Represents a Game.[See on Telegram API](https://core.telegram.org/bots/api#inlinequeryresultgame)

    - - - - -
    **Fields**:

    - `type`: `string` - Type of the result, must be game
    - `id`: `string` - Unique identifier for this result, 1-64 bytes
    - `game_short_name`: `string` - Short name of the game
    - `reply_markup`: `InlineKeyboardMarkup` - Optional. Inline keyboard attached to the message
    """

    def __init__(self, dictionary=None):
        if dictionary is None:
            dictionary = {}
        self.dict = dictionary
        for index, value in self.dict.items():
            if index == "type" and value is not None:
                self.type = value
            elif index == "id" and value is not None:
                self.id = value
            elif index == "game_short_name" and value is not None:
                self.game_short_name = value
            elif index == "reply_markup" and value is not None:
                self.reply_markup = InlineKeyboardMarkup(value)
            else:
                setattr(self, index, helper.setBvar(value))


class InlineQueryResultCachedPhoto:
    """Represents a link to a photo stored on the Telegram servers. By default, this photo will be sent by the user with an optional caption. Alternatively, you can use input_message_content to send a message with the specified content instead of the photo.[See on Telegram API](https://core.telegram.org/bots/api#inlinequeryresultcachedphoto)

    - - - - -
    **Fields**:

    - `type`: `string` - Type of the result, must be photo
    - `id`: `string` - Unique identifier for this result, 1-64 bytes
    - `photo_file_id`: `string` - A valid file identifier of the photo
    - `title`: `string` - Optional. Title for the result
    - `description`: `string` - Optional. Short description of the result
    - `caption`: `string` - Optional. Caption of the photo to be sent, 0-1024 characters after entities parsing
    - `parse_mode`: `string` - Optional. Mode for parsing entities in the photo caption. See formatting options for more details.
    - `reply_markup`: `InlineKeyboardMarkup` - Optional. Inline keyboard attached to the message
    - `input_message_content`: `InputMessageContent` - Optional. Content of the message to be sent instead of the photo
    """

    def __init__(self, dictionary=None):
        if dictionary is None:
            dictionary = {}
        self.dict = dictionary
        for index, value in self.dict.items():
            if index == "type" and value is not None:
                self.type = value
            elif index == "id" and value is not None:
                self.id = value
            elif index == "photo_file_id" and value is not None:
                self.photo_file_id = value
            elif index == "title" and value is not None:
                self.title = value
            elif index == "description" and value is not None:
                self.description = value
            elif index == "caption" and value is not None:
                self.caption = value
            elif index == "parse_mode" and value is not None:
                self.parse_mode = value
            elif index == "reply_markup" and value is not None:
                self.reply_markup = InlineKeyboardMarkup(value)
            elif index == "input_message_content" and value is not None:
                self.input_message_content = InputMessageContent(value)
            else:
                setattr(self, index, helper.setBvar(value))


class InlineQueryResultCachedGif:
    """Represents a link to an animated GIF file stored on the Telegram servers. By default, this animated GIF file will be sent by the user with an optional caption. Alternatively, you can use input_message_content to send a message with specified content instead of the animation.[See on Telegram API](https://core.telegram.org/bots/api#inlinequeryresultcachedgif)

    - - - - -
    **Fields**:

    - `type`: `string` - Type of the result, must be gif
    - `id`: `string` - Unique identifier for this result, 1-64 bytes
    - `gif_file_id`: `string` - A valid file identifier for the GIF file
    - `title`: `string` - Optional. Title for the result
    - `caption`: `string` - Optional. Caption of the GIF file to be sent, 0-1024 characters after entities parsing
    - `parse_mode`: `string` - Optional. Mode for parsing entities in the caption. See formatting options for more details.
    - `reply_markup`: `InlineKeyboardMarkup` - Optional. Inline keyboard attached to the message
    - `input_message_content`: `InputMessageContent` - Optional. Content of the message to be sent instead of the GIF animation
    """

    def __init__(self, dictionary=None):
        if dictionary is None:
            dictionary = {}
        self.dict = dictionary
        for index, value in self.dict.items():
            if index == "type" and value is not None:
                self.type = value
            elif index == "id" and value is not None:
                self.id = value
            elif index == "gif_file_id" and value is not None:
                self.gif_file_id = value
            elif index == "title" and value is not None:
                self.title = value
            elif index == "caption" and value is not None:
                self.caption = value
            elif index == "parse_mode" and value is not None:
                self.parse_mode = value
            elif index == "reply_markup" and value is not None:
                self.reply_markup = InlineKeyboardMarkup(value)
            elif index == "input_message_content" and value is not None:
                self.input_message_content = InputMessageContent(value)
            else:
                setattr(self, index, helper.setBvar(value))


class InlineQueryResultCachedMpeg4Gif:
    """Represents a link to a video animation (H.264/MPEG-4 AVC video without sound) stored on the Telegram servers. By default, this animated MPEG-4 file will be sent by the user with an optional caption. Alternatively, you can use input_message_content to send a message with the specified content instead of the animation.[See on Telegram API](https://core.telegram.org/bots/api#inlinequeryresultcachedmpeg4gif)

    - - - - -
    **Fields**:

    - `type`: `string` - Type of the result, must be mpeg4_gif
    - `id`: `string` - Unique identifier for this result, 1-64 bytes
    - `mpeg4_file_id`: `string` - A valid file identifier for the MP4 file
    - `title`: `string` - Optional. Title for the result
    - `caption`: `string` - Optional. Caption of the MPEG-4 file to be sent, 0-1024 characters after entities parsing
    - `parse_mode`: `string` - Optional. Mode for parsing entities in the caption. See formatting options for more details.
    - `reply_markup`: `InlineKeyboardMarkup` - Optional. Inline keyboard attached to the message
    - `input_message_content`: `InputMessageContent` - Optional. Content of the message to be sent instead of the video animation
    """

    def __init__(self, dictionary=None):
        if dictionary is None:
            dictionary = {}
        self.dict = dictionary
        for index, value in self.dict.items():
            if index == "type" and value is not None:
                self.type = value
            elif index == "id" and value is not None:
                self.id = value
            elif index == "mpeg4_file_id" and value is not None:
                self.mpeg4_file_id = value
            elif index == "title" and value is not None:
                self.title = value
            elif index == "caption" and value is not None:
                self.caption = value
            elif index == "parse_mode" and value is not None:
                self.parse_mode = value
            elif index == "reply_markup" and value is not None:
                self.reply_markup = InlineKeyboardMarkup(value)
            elif index == "input_message_content" and value is not None:
                self.input_message_content = InputMessageContent(value)
            else:
                setattr(self, index, helper.setBvar(value))


class InlineQueryResultCachedSticker:
    """Represents a link to a sticker stored on the Telegram servers. By default, this sticker will be sent by the user. Alternatively, you can use input_message_content to send a message with the specified content instead of the sticker.[See on Telegram API](https://core.telegram.org/bots/api#inlinequeryresultcachedsticker)

    - - - - -
    **Fields**:

    - `type`: `string` - Type of the result, must be sticker
    - `id`: `string` - Unique identifier for this result, 1-64 bytes
    - `sticker_file_id`: `string` - A valid file identifier of the sticker
    - `reply_markup`: `InlineKeyboardMarkup` - Optional. Inline keyboard attached to the message
    - `input_message_content`: `InputMessageContent` - Optional. Content of the message to be sent instead of the sticker
    """

    def __init__(self, dictionary=None):
        if dictionary is None:
            dictionary = {}
        self.dict = dictionary
        for index, value in self.dict.items():
            if index == "type" and value is not None:
                self.type = value
            elif index == "id" and value is not None:
                self.id = value
            elif index == "sticker_file_id" and value is not None:
                self.sticker_file_id = value
            elif index == "reply_markup" and value is not None:
                self.reply_markup = InlineKeyboardMarkup(value)
            elif index == "input_message_content" and value is not None:
                self.input_message_content = InputMessageContent(value)
            else:
                setattr(self, index, helper.setBvar(value))


class InlineQueryResultCachedDocument:
    """Represents a link to a file stored on the Telegram servers. By default, this file will be sent by the user with an optional caption. Alternatively, you can use input_message_content to send a message with the specified content instead of the file.[See on Telegram API](https://core.telegram.org/bots/api#inlinequeryresultcacheddocument)

    - - - - -
    **Fields**:

    - `type`: `string` - Type of the result, must be document
    - `id`: `string` - Unique identifier for this result, 1-64 bytes
    - `title`: `string` - Title for the result
    - `document_file_id`: `string` - A valid file identifier for the file
    - `description`: `string` - Optional. Short description of the result
    - `caption`: `string` - Optional. Caption of the document to be sent, 0-1024 characters after entities parsing
    - `parse_mode`: `string` - Optional. Mode for parsing entities in the document caption. See formatting options for more details.
    - `reply_markup`: `InlineKeyboardMarkup` - Optional. Inline keyboard attached to the message
    - `input_message_content`: `InputMessageContent` - Optional. Content of the message to be sent instead of the file
    """

    def __init__(self, dictionary=None):
        if dictionary is None:
            dictionary = {}
        self.dict = dictionary
        for index, value in self.dict.items():
            if index == "type" and value is not None:
                self.type = value
            elif index == "id" and value is not None:
                self.id = value
            elif index == "title" and value is not None:
                self.title = value
            elif index == "document_file_id" and value is not None:
                self.document_file_id = value
            elif index == "description" and value is not None:
                self.description = value
            elif index == "caption" and value is not None:
                self.caption = value
            elif index == "parse_mode" and value is not None:
                self.parse_mode = value
            elif index == "reply_markup" and value is not None:
                self.reply_markup = InlineKeyboardMarkup(value)
            elif index == "input_message_content" and value is not None:
                self.input_message_content = InputMessageContent(value)
            else:
                setattr(self, index, helper.setBvar(value))


class InlineQueryResultCachedVideo:
    """Represents a link to a video file stored on the Telegram servers. By default, this video file will be sent by the user with an optional caption. Alternatively, you can use input_message_content to send a message with the specified content instead of the video.[See on Telegram API](https://core.telegram.org/bots/api#inlinequeryresultcachedvideo)

    - - - - -
    **Fields**:

    - `type`: `string` - Type of the result, must be video
    - `id`: `string` - Unique identifier for this result, 1-64 bytes
    - `video_file_id`: `string` - A valid file identifier for the video file
    - `title`: `string` - Title for the result
    - `description`: `string` - Optional. Short description of the result
    - `caption`: `string` - Optional. Caption of the video to be sent, 0-1024 characters after entities parsing
    - `parse_mode`: `string` - Optional. Mode for parsing entities in the video caption. See formatting options for more details.
    - `reply_markup`: `InlineKeyboardMarkup` - Optional. Inline keyboard attached to the message
    - `input_message_content`: `InputMessageContent` - Optional. Content of the message to be sent instead of the video
    """

    def __init__(self, dictionary=None):
        if dictionary is None:
            dictionary = {}
        self.dict = dictionary
        for index, value in self.dict.items():
            if index == "type" and value is not None:
                self.type = value
            elif index == "id" and value is not None:
                self.id = value
            elif index == "video_file_id" and value is not None:
                self.video_file_id = value
            elif index == "title" and value is not None:
                self.title = value
            elif index == "description" and value is not None:
                self.description = value
            elif index == "caption" and value is not None:
                self.caption = value
            elif index == "parse_mode" and value is not None:
                self.parse_mode = value
            elif index == "reply_markup" and value is not None:
                self.reply_markup = InlineKeyboardMarkup(value)
            elif index == "input_message_content" and value is not None:
                self.input_message_content = InputMessageContent(value)
            else:
                setattr(self, index, helper.setBvar(value))


class InlineQueryResultCachedVoice:
    """Represents a link to a voice message stored on the Telegram servers. By default, this voice message will be sent by the user. Alternatively, you can use input_message_content to send a message with the specified content instead of the voice message.[See on Telegram API](https://core.telegram.org/bots/api#inlinequeryresultcachedvoice)

    - - - - -
    **Fields**:

    - `type`: `string` - Type of the result, must be voice
    - `id`: `string` - Unique identifier for this result, 1-64 bytes
    - `voice_file_id`: `string` - A valid file identifier for the voice message
    - `title`: `string` - Voice message title
    - `caption`: `string` - Optional. Caption, 0-1024 characters after entities parsing
    - `parse_mode`: `string` - Optional. Mode for parsing entities in the voice message caption. See formatting options for more details.
    - `reply_markup`: `InlineKeyboardMarkup` - Optional. Inline keyboard attached to the message
    - `input_message_content`: `InputMessageContent` - Optional. Content of the message to be sent instead of the voice message
    """

    def __init__(self, dictionary=None):
        if dictionary is None:
            dictionary = {}
        self.dict = dictionary
        for index, value in self.dict.items():
            if index == "type" and value is not None:
                self.type = value
            elif index == "id" and value is not None:
                self.id = value
            elif index == "voice_file_id" and value is not None:
                self.voice_file_id = value
            elif index == "title" and value is not None:
                self.title = value
            elif index == "caption" and value is not None:
                self.caption = value
            elif index == "parse_mode" and value is not None:
                self.parse_mode = value
            elif index == "reply_markup" and value is not None:
                self.reply_markup = InlineKeyboardMarkup(value)
            elif index == "input_message_content" and value is not None:
                self.input_message_content = InputMessageContent(value)
            else:
                setattr(self, index, helper.setBvar(value))


class InlineQueryResultCachedAudio:
    """Represents a link to an MP3 audio file stored on the Telegram servers. By default, this audio file will be sent by the user. Alternatively, you can use input_message_content to send a message with the specified content instead of the audio.[See on Telegram API](https://core.telegram.org/bots/api#inlinequeryresultcachedaudio)

    - - - - -
    **Fields**:

    - `type`: `string` - Type of the result, must be audio
    - `id`: `string` - Unique identifier for this result, 1-64 bytes
    - `audio_file_id`: `string` - A valid file identifier for the audio file
    - `caption`: `string` - Optional. Caption, 0-1024 characters after entities parsing
    - `parse_mode`: `string` - Optional. Mode for parsing entities in the audio caption. See formatting options for more details.
    - `reply_markup`: `InlineKeyboardMarkup` - Optional. Inline keyboard attached to the message
    - `input_message_content`: `InputMessageContent` - Optional. Content of the message to be sent instead of the audio
    """

    def __init__(self, dictionary=None):
        if dictionary is None:
            dictionary = {}
        self.dict = dictionary
        for index, value in self.dict.items():
            if index == "type" and value is not None:
                self.type = value
            elif index == "id" and value is not None:
                self.id = value
            elif index == "audio_file_id" and value is not None:
                self.audio_file_id = value
            elif index == "caption" and value is not None:
                self.caption = value
            elif index == "parse_mode" and value is not None:
                self.parse_mode = value
            elif index == "reply_markup" and value is not None:
                self.reply_markup = InlineKeyboardMarkup(value)
            elif index == "input_message_content" and value is not None:
                self.input_message_content = InputMessageContent(value)
            else:
                setattr(self, index, helper.setBvar(value))


class InputMessageContent:
    """This object represents the content of a message to be sent as a result of an inline query. Telegram clients currently support the following 4 types:[See on Telegram API](https://core.telegram.org/bots/api#inputmessagecontent)

    - - - - -
    **Fields**:

    """

    def __init__(self, dictionary=None):
        if dictionary is None:
            dictionary = {}
        self.dict = dictionary
        for index, value in self.dict.items():
            setattr(self, index, helper.setBvar(value))


class InputTextMessageContent:
    """Represents the content of a text message to be sent as the result of an inline query.[See on Telegram API](https://core.telegram.org/bots/api#inputtextmessagecontent)

    - - - - -
    **Fields**:

    - `message_text`: `string` - Text of the message to be sent, 1-4096 characters
    - `parse_mode`: `string` - Optional. Mode for parsing entities in the message text. See formatting options for more details.
    - `disable_web_page_preview`: `bool` - Optional. Disables link previews for links in the sent message
    """

    def __init__(self, dictionary=None):
        if dictionary is None:
            dictionary = {}
        self.dict = dictionary
        for index, value in self.dict.items():
            if index == "message_text" and value is not None:
                self.message_text = value
            elif index == "parse_mode" and value is not None:
                self.parse_mode = value
            elif index == "disable_web_page_preview" and value is not None:
                self.disable_web_page_preview = value
            else:
                setattr(self, index, helper.setBvar(value))


class InputLocationMessageContent:
    """Represents the content of a location message to be sent as the result of an inline query.[See on Telegram API](https://core.telegram.org/bots/api#inputlocationmessagecontent)

    - - - - -
    **Fields**:

    - `latitude`: `float` - Latitude of the location in degrees
    - `longitude`: `float` - Longitude of the location in degrees
    - `live_period`: `int` - Optional. Period in seconds for which the location can be updated, should be between 60 and 86400.
    """

    def __init__(self, dictionary=None):
        if dictionary is None:
            dictionary = {}
        self.dict = dictionary
        for index, value in self.dict.items():
            if index == "latitude" and value is not None:
                self.latitude = value
            elif index == "longitude" and value is not None:
                self.longitude = value
            elif index == "live_period" and value is not None:
                self.live_period = value
            else:
                setattr(self, index, helper.setBvar(value))


class InputVenueMessageContent:
    """Represents the content of a venue message to be sent as the result of an inline query.[See on Telegram API](https://core.telegram.org/bots/api#inputvenuemessagecontent)

    - - - - -
    **Fields**:

    - `latitude`: `float` - Latitude of the venue in degrees
    - `longitude`: `float` - Longitude of the venue in degrees
    - `title`: `string` - Name of the venue
    - `address`: `string` - Address of the venue
    - `foursquare_id`: `string` - Optional. Foursquare identifier of the venue, if known
    - `foursquare_type`: `string` - Optional. Foursquare type of the venue, if known. (For example, “arts_entertainment/default”, “arts_entertainment/aquarium” or “food/icecream”.)
    """

    def __init__(self, dictionary=None):
        if dictionary is None:
            dictionary = {}
        self.dict = dictionary
        for index, value in self.dict.items():
            if index == "latitude" and value is not None:
                self.latitude = value
            elif index == "longitude" and value is not None:
                self.longitude = value
            elif index == "title" and value is not None:
                self.title = value
            elif index == "address" and value is not None:
                self.address = value
            elif index == "foursquare_id" and value is not None:
                self.foursquare_id = value
            elif index == "foursquare_type" and value is not None:
                self.foursquare_type = value
            else:
                setattr(self, index, helper.setBvar(value))


class InputContactMessageContent:
    """Represents the content of a contact message to be sent as the result of an inline query.[See on Telegram API](https://core.telegram.org/bots/api#inputcontactmessagecontent)

    - - - - -
    **Fields**:

    - `phone_number`: `string` - Contact's phone number
    - `first_name`: `string` - Contact's first name
    - `last_name`: `string` - Optional. Contact's last name
    - `vcard`: `string` - Optional. Additional data about the contact in the form of a vCard, 0-2048 bytes
    """

    def __init__(self, dictionary=None):
        if dictionary is None:
            dictionary = {}
        self.dict = dictionary
        for index, value in self.dict.items():
            if index == "phone_number" and value is not None:
                self.phone_number = value
            elif index == "first_name" and value is not None:
                self.first_name = value
            elif index == "last_name" and value is not None:
                self.last_name = value
            elif index == "vcard" and value is not None:
                self.vcard = value
            else:
                setattr(self, index, helper.setBvar(value))


class ChosenInlineResult:
    """Represents a result of an inline query that was chosen by the user and sent to their chat partner.[See on Telegram API](https://core.telegram.org/bots/api#choseninlineresult)

    - - - - -
    **Fields**:

    - `result_id`: `string` - The unique identifier for the result that was chosen
    - `user`: `User` - The user that chose the result
    - `location`: `Location` - Optional. Sender location, only for bots that require user location
    - `inline_message_id`: `string` - Optional. Identifier of the sent inline message. Available only if there is an inline keyboard attached to the message. Will be also received in callback queries and can be used to edit the message.
    - `query`: `string` - The query that was used to obtain the result
    """

    def __init__(self, dictionary=None):
        if dictionary is None:
            dictionary = {}
        self.dict = dictionary
        for index, value in self.dict.items():
            if index == "result_id" and value is not None:
                self.result_id = value
            elif index == "from" and value is not None:
                self.user = User(value)
            elif index == "location" and value is not None:
                self.location = Location(value)
            elif index == "inline_message_id" and value is not None:
                self.inline_message_id = value
            elif index == "query" and value is not None:
                self.query = value
            else:
                setattr(self, index, helper.setBvar(value))


class LabeledPrice:
    """This object represents a portion of the price for goods or services.[See on Telegram API](https://core.telegram.org/bots/api#labeledprice)

    - - - - -
    **Fields**:

    - `label`: `string` - Portion label
    - `amount`: `int` - Price of the product in the smallest units of the currency (integer, not float/double). For example, for a price of US$ 1.45 pass amount = 145. See the exp parameter in currencies.json, it shows the number of digits past the decimal point for each currency (2 for the majority of currencies).
    """

    def __init__(self, dictionary=None):
        if dictionary is None:
            dictionary = {}
        self.dict = dictionary
        for index, value in self.dict.items():
            if index == "label" and value is not None:
                self.label = value
            elif index == "amount" and value is not None:
                self.amount = value
            else:
                setattr(self, index, helper.setBvar(value))


class Invoice:
    """This object contains basic information about an invoice.[See on Telegram API](https://core.telegram.org/bots/api#invoice)

    - - - - -
    **Fields**:

    - `title`: `string` - Product name
    - `description`: `string` - Product description
    - `start_parameter`: `string` - Unique bot deep-linking parameter that can be used to generate this invoice
    - `currency`: `string` - Three-letter ISO 4217 currency code
    - `total_amount`: `int` - Total price in the smallest units of the currency (integer, not float/double). For example, for a price of US$ 1.45 pass amount = 145. See the exp parameter in currencies.json, it shows the number of digits past the decimal point for each currency (2 for the majority of currencies).
    """

    def __init__(self, dictionary=None):
        if dictionary is None:
            dictionary = {}
        self.dict = dictionary
        for index, value in self.dict.items():
            if index == "title" and value is not None:
                self.title = value
            elif index == "description" and value is not None:
                self.description = value
            elif index == "start_parameter" and value is not None:
                self.start_parameter = value
            elif index == "currency" and value is not None:
                self.currency = value
            elif index == "total_amount" and value is not None:
                self.total_amount = value
            else:
                setattr(self, index, helper.setBvar(value))


class ShippingAddress:
    """This object represents a shipping address.[See on Telegram API](https://core.telegram.org/bots/api#shippingaddress)

    - - - - -
    **Fields**:

    - `country_code`: `string` - ISO 3166-1 alpha-2 country code
    - `state`: `string` - State, if applicable
    - `city`: `string` - City
    - `street_line1`: `string` - First line for the address
    - `street_line2`: `string` - Second line for the address
    - `post_code`: `string` - Address post code
    """

    def __init__(self, dictionary=None):
        if dictionary is None:
            dictionary = {}
        self.dict = dictionary
        for index, value in self.dict.items():
            if index == "country_code" and value is not None:
                self.country_code = value
            elif index == "state" and value is not None:
                self.state = value
            elif index == "city" and value is not None:
                self.city = value
            elif index == "street_line1" and value is not None:
                self.street_line1 = value
            elif index == "street_line2" and value is not None:
                self.street_line2 = value
            elif index == "post_code" and value is not None:
                self.post_code = value
            else:
                setattr(self, index, helper.setBvar(value))


class OrderInfo:
    """This object represents information about an order.[See on Telegram API](https://core.telegram.org/bots/api#orderinfo)

    - - - - -
    **Fields**:

    - `name`: `string` - Optional. User name
    - `phone_number`: `string` - Optional. User's phone number
    - `email`: `string` - Optional. User email
    - `shipping_address`: `ShippingAddress` - Optional. User shipping address
    """

    def __init__(self, dictionary=None):
        if dictionary is None:
            dictionary = {}
        self.dict = dictionary
        for index, value in self.dict.items():
            if index == "name" and value is not None:
                self.name = value
            elif index == "phone_number" and value is not None:
                self.phone_number = value
            elif index == "email" and value is not None:
                self.email = value
            elif index == "shipping_address" and value is not None:
                self.shipping_address = ShippingAddress(value)
            else:
                setattr(self, index, helper.setBvar(value))


class ShippingOption:
    """This object represents one shipping option.[See on Telegram API](https://core.telegram.org/bots/api#shippingoption)

    - - - - -
    **Fields**:

    - `id`: `string` - Shipping option identifier
    - `title`: `string` - Option title
    - `prices`: `LabeledPrice[]` - List of price portions
    """

    def __init__(self, dictionary=None):
        if dictionary is None:
            dictionary = {}
        self.dict = dictionary
        for index, value in self.dict.items():
            if index == "id" and value is not None:
                self.id = value
            elif index == "title" and value is not None:
                self.title = value
            elif index == "prices" and value is not None:
                self.prices = list()
                for i1 in value:
                    self.prices.append(LabeledPrice(i1))
            else:
                setattr(self, index, helper.setBvar(value))


class SuccessfulPayment:
    """This object contains basic information about a successful payment.[See on Telegram API](https://core.telegram.org/bots/api#successfulpayment)

    - - - - -
    **Fields**:

    - `currency`: `string` - Three-letter ISO 4217 currency code
    - `total_amount`: `int` - Total price in the smallest units of the currency (integer, not float/double). For example, for a price of US$ 1.45 pass amount = 145. See the exp parameter in currencies.json, it shows the number of digits past the decimal point for each currency (2 for the majority of currencies).
    - `invoice_payload`: `string` - Bot specified invoice payload
    - `shipping_option_id`: `string` - Optional. Identifier of the shipping option chosen by the user
    - `order_info`: `OrderInfo` - Optional. Order info provided by the user
    - `telegram_payment_charge_id`: `string` - Telegram payment identifier
    - `provider_payment_charge_id`: `string` - Provider payment identifier
    """

    def __init__(self, dictionary=None):
        if dictionary is None:
            dictionary = {}
        self.dict = dictionary
        for index, value in self.dict.items():
            if index == "currency" and value is not None:
                self.currency = value
            elif index == "total_amount" and value is not None:
                self.total_amount = value
            elif index == "invoice_payload" and value is not None:
                self.invoice_payload = value
            elif index == "shipping_option_id" and value is not None:
                self.shipping_option_id = value
            elif index == "order_info" and value is not None:
                self.order_info = OrderInfo(value)
            elif index == "telegram_payment_charge_id" and value is not None:
                self.telegram_payment_charge_id = value
            elif index == "provider_payment_charge_id" and value is not None:
                self.provider_payment_charge_id = value
            else:
                setattr(self, index, helper.setBvar(value))


class ShippingQuery:
    """This object contains information about an incoming shipping query.[See on Telegram API](https://core.telegram.org/bots/api#shippingquery)

    - - - - -
    **Fields**:

    - `id`: `string` - Unique query identifier
    - `user`: `User` - User who sent the query
    - `invoice_payload`: `string` - Bot specified invoice payload
    - `shipping_address`: `ShippingAddress` - User specified shipping address
    """

    def __init__(self, dictionary=None):
        if dictionary is None:
            dictionary = {}
        self.dict = dictionary
        for index, value in self.dict.items():
            if index == "id" and value is not None:
                self.id = value
            elif index == "from" and value is not None:
                self.user = User(value)
            elif index == "invoice_payload" and value is not None:
                self.invoice_payload = value
            elif index == "shipping_address" and value is not None:
                self.shipping_address = ShippingAddress(value)
            else:
                setattr(self, index, helper.setBvar(value))


class PreCheckoutQuery:
    """This object contains information about an incoming pre-checkout query.[See on Telegram API](https://core.telegram.org/bots/api#precheckoutquery)

    - - - - -
    **Fields**:

    - `id`: `string` - Unique query identifier
    - `user`: `User` - User who sent the query
    - `currency`: `string` - Three-letter ISO 4217 currency code
    - `total_amount`: `int` - Total price in the smallest units of the currency (integer, not float/double). For example, for a price of US$ 1.45 pass amount = 145. See the exp parameter in currencies.json, it shows the number of digits past the decimal point for each currency (2 for the majority of currencies).
    - `invoice_payload`: `string` - Bot specified invoice payload
    - `shipping_option_id`: `string` - Optional. Identifier of the shipping option chosen by the user
    - `order_info`: `OrderInfo` - Optional. Order info provided by the user
    """

    def __init__(self, dictionary=None):
        if dictionary is None:
            dictionary = {}
        self.dict = dictionary
        for index, value in self.dict.items():
            if index == "id" and value is not None:
                self.id = value
            elif index == "from" and value is not None:
                self.user = User(value)
            elif index == "currency" and value is not None:
                self.currency = value
            elif index == "total_amount" and value is not None:
                self.total_amount = value
            elif index == "invoice_payload" and value is not None:
                self.invoice_payload = value
            elif index == "shipping_option_id" and value is not None:
                self.shipping_option_id = value
            elif index == "order_info" and value is not None:
                self.order_info = OrderInfo(value)
            else:
                setattr(self, index, helper.setBvar(value))


class PassportData:
    """Contains information about Telegram Passport data shared with the bot by the user.[See on Telegram API](https://core.telegram.org/bots/api#passportdata)

    - - - - -
    **Fields**:

    - `data`: `EncryptedPassportElement[]` - Array with information about documents and other Telegram Passport elements that was shared with the bot
    - `credentials`: `EncryptedCredentials` - Encrypted credentials required to decrypt the data
    """

    def __init__(self, dictionary=None):
        if dictionary is None:
            dictionary = {}
        self.dict = dictionary
        for index, value in self.dict.items():
            if index == "data" and value is not None:
                self.data = list()
                for i1 in value:
                    self.data.append(EncryptedPassportElement(i1))
            elif index == "credentials" and value is not None:
                self.credentials = EncryptedCredentials(value)
            else:
                setattr(self, index, helper.setBvar(value))


class PassportFile:
    """This object represents a file uploaded to Telegram Passport. Currently all Telegram Passport files are in JPEG format when decrypted and don't exceed 10MB.[See on Telegram API](https://core.telegram.org/bots/api#passportfile)

    - - - - -
    **Fields**:

    - `file_id`: `string` - Identifier for this file, which can be used to download or reuse the file
    - `file_unique_id`: `string` - Unique identifier for this file, which is supposed to be the same over time and for different bots. Can't be used to download or reuse the file.
    - `file_size`: `int` - File size
    - `file_date`: `int` - Unix time when the file was uploaded
    """

    def __init__(self, dictionary=None):
        if dictionary is None:
            dictionary = {}
        self.dict = dictionary
        for index, value in self.dict.items():
            if index == "file_id" and value is not None:
                self.file_id = value
            elif index == "file_unique_id" and value is not None:
                self.file_unique_id = value
            elif index == "file_size" and value is not None:
                self.file_size = value
            elif index == "file_date" and value is not None:
                self.file_date = value
            else:
                setattr(self, index, helper.setBvar(value))


class EncryptedPassportElement:
    """Contains information about documents or other Telegram Passport elements shared with the bot by the user.[See on Telegram API](https://core.telegram.org/bots/api#encryptedpassportelement)

    - - - - -
    **Fields**:

    - `type`: `string` - Element type. One of “personal_details”, “passport”, “driver_license”, “identity_card”, “internal_passport”, “address”, “utility_bill”, “bank_statement”, “rental_agreement”, “passport_registration”, “temporary_registration”, “phone_number”, “email”.
    - `data`: `string` - Optional. Base64-encoded encrypted Telegram Passport element data provided by the user, available for “personal_details”, “passport”, “driver_license”, “identity_card”, “internal_passport” and “address” types. Can be decrypted and verified using the accompanying EncryptedCredentials.
    - `phone_number`: `string` - Optional. User's verified phone number, available only for “phone_number” type
    - `email`: `string` - Optional. User's verified email address, available only for “email” type
    - `files`: `PassportFile[]` - Optional. Array of encrypted files with documents provided by the user, available for “utility_bill”, “bank_statement”, “rental_agreement”, “passport_registration” and “temporary_registration” types. Files can be decrypted and verified using the accompanying EncryptedCredentials.
    - `front_side`: `PassportFile` - Optional. Encrypted file with the front side of the document, provided by the user. Available for “passport”, “driver_license”, “identity_card” and “internal_passport”. The file can be decrypted and verified using the accompanying EncryptedCredentials.
    - `reverse_side`: `PassportFile` - Optional. Encrypted file with the reverse side of the document, provided by the user. Available for “driver_license” and “identity_card”. The file can be decrypted and verified using the accompanying EncryptedCredentials.
    - `selfie`: `PassportFile` - Optional. Encrypted file with the selfie of the user holding a document, provided by the user; available for “passport”, “driver_license”, “identity_card” and “internal_passport”. The file can be decrypted and verified using the accompanying EncryptedCredentials.
    - `translation`: `PassportFile[]` - Optional. Array of encrypted files with translated versions of documents provided by the user. Available if requested for “passport”, “driver_license”, “identity_card”, “internal_passport”, “utility_bill”, “bank_statement”, “rental_agreement”, “passport_registration” and “temporary_registration” types. Files can be decrypted and verified using the accompanying EncryptedCredentials.
    - `hash`: `string` - Base64-encoded element hash for using in PassportElementErrorUnspecified
    """

    def __init__(self, dictionary=None):
        if dictionary is None:
            dictionary = {}
        self.dict = dictionary
        for index, value in self.dict.items():
            if index == "type" and value is not None:
                self.type = value
            elif index == "data" and value is not None:
                self.data = value
            elif index == "phone_number" and value is not None:
                self.phone_number = value
            elif index == "email" and value is not None:
                self.email = value
            elif index == "files" and value is not None:
                self.files = list()
                for i1 in value:
                    self.files.append(PassportFile(i1))
            elif index == "front_side" and value is not None:
                self.front_side = PassportFile(value)
            elif index == "reverse_side" and value is not None:
                self.reverse_side = PassportFile(value)
            elif index == "selfie" and value is not None:
                self.selfie = PassportFile(value)
            elif index == "translation" and value is not None:
                self.translation = list()
                for i1 in value:
                    self.translation.append(PassportFile(i1))
            elif index == "hash" and value is not None:
                self.hash = value
            else:
                setattr(self, index, helper.setBvar(value))


class EncryptedCredentials:
    """Contains data required for decrypting and authenticating EncryptedPassportElement. See the Telegram Passport Documentation for a complete description of the data decryption and authentication processes.[See on Telegram API](https://core.telegram.org/bots/api#encryptedcredentials)

    - - - - -
    **Fields**:

    - `data`: `string` - Base64-encoded encrypted JSON-serialized data with unique user's payload, data hashes and secrets required for EncryptedPassportElement decryption and authentication
    - `hash`: `string` - Base64-encoded data hash for data authentication
    - `secret`: `string` - Base64-encoded secret, encrypted with the bot's public RSA key, required for data decryption
    """

    def __init__(self, dictionary=None):
        if dictionary is None:
            dictionary = {}
        self.dict = dictionary
        for index, value in self.dict.items():
            if index == "data" and value is not None:
                self.data = value
            elif index == "hash" and value is not None:
                self.hash = value
            elif index == "secret" and value is not None:
                self.secret = value
            else:
                setattr(self, index, helper.setBvar(value))


class PassportElementError:
    """This object represents an error in the Telegram Passport element which was submitted that should be resolved by the user. It should be one of:[See on Telegram API](https://core.telegram.org/bots/api#passportelementerror)

    - - - - -
    **Fields**:

    """

    def __init__(self, dictionary=None):
        if dictionary is None:
            dictionary = {}
        self.dict = dictionary
        for index, value in self.dict.items():
            setattr(self, index, helper.setBvar(value))


class PassportElementErrorDataField:
    """Represents an issue in one of the data fields that was provided by the user. The error is considered resolved when the field's value changes.[See on Telegram API](https://core.telegram.org/bots/api#passportelementerrordatafield)

    - - - - -
    **Fields**:

    - `source`: `string` - Error source, must be data
    - `type`: `string` - The section of the user's Telegram Passport which has the error, one of “personal_details”, “passport”, “driver_license”, “identity_card”, “internal_passport”, “address”
    - `field_name`: `string` - Name of the data field which has the error
    - `data_hash`: `string` - Base64-encoded data hash
    - `message`: `string` - Error message
    """

    def __init__(self, dictionary=None):
        if dictionary is None:
            dictionary = {}
        self.dict = dictionary
        for index, value in self.dict.items():
            if index == "source" and value is not None:
                self.source = value
            elif index == "type" and value is not None:
                self.type = value
            elif index == "field_name" and value is not None:
                self.field_name = value
            elif index == "data_hash" and value is not None:
                self.data_hash = value
            elif index == "message" and value is not None:
                self.message = value
            else:
                setattr(self, index, helper.setBvar(value))


class PassportElementErrorFrontSide:
    """Represents an issue with the front side of a document. The error is considered resolved when the file with the front side of the document changes.[See on Telegram API](https://core.telegram.org/bots/api#passportelementerrorfrontside)

    - - - - -
    **Fields**:

    - `source`: `string` - Error source, must be front_side
    - `type`: `string` - The section of the user's Telegram Passport which has the issue, one of “passport”, “driver_license”, “identity_card”, “internal_passport”
    - `file_hash`: `string` - Base64-encoded hash of the file with the front side of the document
    - `message`: `string` - Error message
    """

    def __init__(self, dictionary=None):
        if dictionary is None:
            dictionary = {}
        self.dict = dictionary
        for index, value in self.dict.items():
            if index == "source" and value is not None:
                self.source = value
            elif index == "type" and value is not None:
                self.type = value
            elif index == "file_hash" and value is not None:
                self.file_hash = value
            elif index == "message" and value is not None:
                self.message = value
            else:
                setattr(self, index, helper.setBvar(value))


class PassportElementErrorReverseSide:
    """Represents an issue with the reverse side of a document. The error is considered resolved when the file with reverse side of the document changes.[See on Telegram API](https://core.telegram.org/bots/api#passportelementerrorreverseside)

    - - - - -
    **Fields**:

    - `source`: `string` - Error source, must be reverse_side
    - `type`: `string` - The section of the user's Telegram Passport which has the issue, one of “driver_license”, “identity_card”
    - `file_hash`: `string` - Base64-encoded hash of the file with the reverse side of the document
    - `message`: `string` - Error message
    """

    def __init__(self, dictionary=None):
        if dictionary is None:
            dictionary = {}
        self.dict = dictionary
        for index, value in self.dict.items():
            if index == "source" and value is not None:
                self.source = value
            elif index == "type" and value is not None:
                self.type = value
            elif index == "file_hash" and value is not None:
                self.file_hash = value
            elif index == "message" and value is not None:
                self.message = value
            else:
                setattr(self, index, helper.setBvar(value))


class PassportElementErrorSelfie:
    """Represents an issue with the selfie with a document. The error is considered resolved when the file with the selfie changes.[See on Telegram API](https://core.telegram.org/bots/api#passportelementerrorselfie)

    - - - - -
    **Fields**:

    - `source`: `string` - Error source, must be selfie
    - `type`: `string` - The section of the user's Telegram Passport which has the issue, one of “passport”, “driver_license”, “identity_card”, “internal_passport”
    - `file_hash`: `string` - Base64-encoded hash of the file with the selfie
    - `message`: `string` - Error message
    """

    def __init__(self, dictionary=None):
        if dictionary is None:
            dictionary = {}
        self.dict = dictionary
        for index, value in self.dict.items():
            if index == "source" and value is not None:
                self.source = value
            elif index == "type" and value is not None:
                self.type = value
            elif index == "file_hash" and value is not None:
                self.file_hash = value
            elif index == "message" and value is not None:
                self.message = value
            else:
                setattr(self, index, helper.setBvar(value))


class PassportElementErrorFile:
    """Represents an issue with a document scan. The error is considered resolved when the file with the document scan changes.[See on Telegram API](https://core.telegram.org/bots/api#passportelementerrorfile)

    - - - - -
    **Fields**:

    - `source`: `string` - Error source, must be file
    - `type`: `string` - The section of the user's Telegram Passport which has the issue, one of “utility_bill”, “bank_statement”, “rental_agreement”, “passport_registration”, “temporary_registration”
    - `file_hash`: `string` - Base64-encoded file hash
    - `message`: `string` - Error message
    """

    def __init__(self, dictionary=None):
        if dictionary is None:
            dictionary = {}
        self.dict = dictionary
        for index, value in self.dict.items():
            if index == "source" and value is not None:
                self.source = value
            elif index == "type" and value is not None:
                self.type = value
            elif index == "file_hash" and value is not None:
                self.file_hash = value
            elif index == "message" and value is not None:
                self.message = value
            else:
                setattr(self, index, helper.setBvar(value))


class PassportElementErrorFiles:
    """Represents an issue with a list of scans. The error is considered resolved when the list of files containing the scans changes.[See on Telegram API](https://core.telegram.org/bots/api#passportelementerrorfiles)

    - - - - -
    **Fields**:

    - `source`: `string` - Error source, must be files
    - `type`: `string` - The section of the user's Telegram Passport which has the issue, one of “utility_bill”, “bank_statement”, “rental_agreement”, “passport_registration”, “temporary_registration”
    - `file_hashes`: `string[]` - List of base64-encoded file hashes
    - `message`: `string` - Error message
    """

    def __init__(self, dictionary=None):
        if dictionary is None:
            dictionary = {}
        self.dict = dictionary
        for index, value in self.dict.items():
            if index == "source" and value is not None:
                self.source = value
            elif index == "type" and value is not None:
                self.type = value
            elif index == "file_hashes" and value is not None:
                self.file_hashes = list()
                for i1 in value:
                    self.file_hashes.append(i1)
            elif index == "message" and value is not None:
                self.message = value
            else:
                setattr(self, index, helper.setBvar(value))


class PassportElementErrorTranslationFile:
    """Represents an issue with one of the files that constitute the translation of a document. The error is considered resolved when the file changes.[See on Telegram API](https://core.telegram.org/bots/api#passportelementerrortranslationfile)

    - - - - -
    **Fields**:

    - `source`: `string` - Error source, must be translation_file
    - `type`: `string` - Type of element of the user's Telegram Passport which has the issue, one of “passport”, “driver_license”, “identity_card”, “internal_passport”, “utility_bill”, “bank_statement”, “rental_agreement”, “passport_registration”, “temporary_registration”
    - `file_hash`: `string` - Base64-encoded file hash
    - `message`: `string` - Error message
    """

    def __init__(self, dictionary=None):
        if dictionary is None:
            dictionary = {}
        self.dict = dictionary
        for index, value in self.dict.items():
            if index == "source" and value is not None:
                self.source = value
            elif index == "type" and value is not None:
                self.type = value
            elif index == "file_hash" and value is not None:
                self.file_hash = value
            elif index == "message" and value is not None:
                self.message = value
            else:
                setattr(self, index, helper.setBvar(value))


class PassportElementErrorTranslationFiles:
    """Represents an issue with the translated version of a document. The error is considered resolved when a file with the document translation change.[See on Telegram API](https://core.telegram.org/bots/api#passportelementerrortranslationfiles)

    - - - - -
    **Fields**:

    - `source`: `string` - Error source, must be translation_files
    - `type`: `string` - Type of element of the user's Telegram Passport which has the issue, one of “passport”, “driver_license”, “identity_card”, “internal_passport”, “utility_bill”, “bank_statement”, “rental_agreement”, “passport_registration”, “temporary_registration”
    - `file_hashes`: `string[]` - List of base64-encoded file hashes
    - `message`: `string` - Error message
    """

    def __init__(self, dictionary=None):
        if dictionary is None:
            dictionary = {}
        self.dict = dictionary
        for index, value in self.dict.items():
            if index == "source" and value is not None:
                self.source = value
            elif index == "type" and value is not None:
                self.type = value
            elif index == "file_hashes" and value is not None:
                self.file_hashes = list()
                for i1 in value:
                    self.file_hashes.append(i1)
            elif index == "message" and value is not None:
                self.message = value
            else:
                setattr(self, index, helper.setBvar(value))


class PassportElementErrorUnspecified:
    """Represents an issue in an unspecified place. The error is considered resolved when new data is added.[See on Telegram API](https://core.telegram.org/bots/api#passportelementerrorunspecified)

    - - - - -
    **Fields**:

    - `source`: `string` - Error source, must be unspecified
    - `type`: `string` - Type of element of the user's Telegram Passport which has the issue
    - `element_hash`: `string` - Base64-encoded element hash
    - `message`: `string` - Error message
    """

    def __init__(self, dictionary=None):
        if dictionary is None:
            dictionary = {}
        self.dict = dictionary
        for index, value in self.dict.items():
            if index == "source" and value is not None:
                self.source = value
            elif index == "type" and value is not None:
                self.type = value
            elif index == "element_hash" and value is not None:
                self.element_hash = value
            elif index == "message" and value is not None:
                self.message = value
            else:
                setattr(self, index, helper.setBvar(value))


class Game:
    """This object represents a game. Use BotFather to create and edit games, their short names will act as unique identifiers.[See on Telegram API](https://core.telegram.org/bots/api#game)

    - - - - -
    **Fields**:

    - `title`: `string` - Title of the game
    - `description`: `string` - Description of the game
    - `photo`: `PhotoSize[]` - Photo that will be displayed in the game message in chats.
    - `text`: `string` - Optional. Brief description of the game or high scores included in the game message. Can be automatically edited to include current high scores for the game when the bot calls setGameScore, or manually edited using editMessageText. 0-4096 characters.
    - `text_entities`: `MessageEntity[]` - Optional. Special entities that appear in text, such as usernames, URLs, bot commands, etc.
    - `animation`: `Animation` - Optional. Animation that will be displayed in the game message in chats. Upload via BotFather
    """

    def __init__(self, dictionary=None):
        if dictionary is None:
            dictionary = {}
        self.dict = dictionary
        for index, value in self.dict.items():
            if index == "title" and value is not None:
                self.title = value
            elif index == "description" and value is not None:
                self.description = value
            elif index == "photo" and value is not None:
                self.photo = list()
                for i1 in value:
                    self.photo.append(PhotoSize(i1))
            elif index == "text" and value is not None:
                self.text = value
            elif index == "text_entities" and value is not None:
                self.text_entities = list()
                for i1 in value:
                    self.text_entities.append(MessageEntity(i1))
            elif index == "animation" and value is not None:
                self.animation = Animation(value)
            else:
                setattr(self, index, helper.setBvar(value))


class CallbackGame:
    """A placeholder, currently holds no information. Use BotFather to set up your game.[See on Telegram API](https://core.telegram.org/bots/api#callbackgame)

    - - - - -
    **Fields**:

    """

    def __init__(self, dictionary=None):
        if dictionary is None:
            dictionary = {}
        self.dict = dictionary
        for index, value in self.dict.items():
            setattr(self, index, helper.setBvar(value))


class GameHighScore:
    """This object represents one row of the high scores table for a game.[See on Telegram API](https://core.telegram.org/bots/api#gamehighscore)

    - - - - -
    **Fields**:

    - `position`: `int` - Position in high score table for the game
    - `user`: `User` - User
    - `score`: `int` - Score
    """

    def __init__(self, dictionary=None):
        if dictionary is None:
            dictionary = {}
        self.dict = dictionary
        for index, value in self.dict.items():
            if index == "position" and value is not None:
                self.position = value
            elif index == "user" and value is not None:
                self.user = User(value)
            elif index == "score" and value is not None:
                self.score = value
            else:
                setattr(self, index, helper.setBvar(value))
