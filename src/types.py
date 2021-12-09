from silbot import helper, objects


class Update:
    """This object represents an incoming update.At most one of the optional parameters can be present in any given update.[See on Telegram API](https://core.telegram.org/bots/api#update)

    - - - - -
    **Fields**:

    - `update_id`: `int` - The update's unique identifier. Update identifiers start from a certain positive number and increase sequentially. This ID becomes especially handy if you're using Webhooks, since it allows you to ignore repeated updates or to restore the correct update sequence, should they get out of order. If there are no new updates for at least a week, then identifier of the next update will be chosen randomly instead of sequentially.
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
    - `my_chat_member`: `ChatMemberUpdated` - Optional. The bot's chat member status was updated in a chat. For private chats, this update is received only when the bot is blocked or unblocked by the user.
    - `chat_member`: `ChatMemberUpdated` - Optional. A chat member's status was updated in a chat. The bot must be an administrator in the chat and must explicitly specify “chat_member” in the list of allowed_updates to receive these updates.
    - `chat_join_request`: `ChatJoinRequest` - Optional. A request to join the chat has been sent. The bot must have the can_invite_users administrator right in the chat to receive these updates.
    """

    def __init__(self, dictionary=None):
        if dictionary is None:
            dictionary = {}
        self.dict = dictionary
        self.update_id = dictionary["update_id"] if "update_id" in dictionary else None
        self.message = Message(dictionary["message"]) if "message" in dictionary else None
        self.edited_message = Message(dictionary["edited_message"]) if "edited_message" in dictionary else None
        self.channel_post = Message(dictionary["channel_post"]) if "channel_post" in dictionary else None
        self.edited_channel_post = Message(dictionary["edited_channel_post"]) if "edited_channel_post" in dictionary else None
        self.inline_query = InlineQuery(dictionary["inline_query"]) if "inline_query" in dictionary else None
        self.chosen_inline_result = ChosenInlineResult(dictionary["chosen_inline_result"]) if "chosen_inline_result" in dictionary else None
        self.callback_query = CallbackQuery(dictionary["callback_query"]) if "callback_query" in dictionary else None
        self.shipping_query = ShippingQuery(dictionary["shipping_query"]) if "shipping_query" in dictionary else None
        self.pre_checkout_query = PreCheckoutQuery(dictionary["pre_checkout_query"]) if "pre_checkout_query" in dictionary else None
        self.poll = Poll(dictionary["poll"]) if "poll" in dictionary else None
        self.poll_answer = PollAnswer(dictionary["poll_answer"]) if "poll_answer" in dictionary else None
        self.my_chat_member = ChatMemberUpdated(dictionary["my_chat_member"]) if "my_chat_member" in dictionary else None
        self.chat_member = ChatMemberUpdated(dictionary["chat_member"]) if "chat_member" in dictionary else None
        self.chat_join_request = ChatJoinRequest(dictionary["chat_join_request"]) if "chat_join_request" in dictionary else None

        for index, value in self.dict.items():
            if not hasattr(self, index):
                setattr(self, index, helper.setBvar(value))


class WebhookInfo:
    """Contains information about the current status of a webhook.[See on Telegram API](https://core.telegram.org/bots/api#webhookinfo)

    - - - - -
    **Fields**:

    - `url`: `string` - Webhook URL, may be empty if webhook is not set up
    - `has_custom_certificate`: `bool` - True, if a custom certificate was provided for webhook certificate checks
    - `pending_update_count`: `int` - Number of updates awaiting delivery
    - `ip_address`: `string` - Optional. Currently used webhook IP address
    - `last_error_date`: `int` - Optional. Unix time for the most recent error that happened when trying to deliver an update via webhook
    - `last_error_message`: `string` - Optional. Error message in human-readable format for the most recent error that happened when trying to deliver an update via webhook
    - `max_connections`: `int` - Optional. Maximum allowed number of simultaneous HTTPS connections to the webhook for update delivery
    - `allowed_updates`: `list` - Optional. A list of update types the bot is subscribed to. Defaults to all update types except chat_member
    """

    def __init__(self, dictionary=None):
        if dictionary is None:
            dictionary = {}
        self.dict = dictionary
        self.url = dictionary["url"] if "url" in dictionary else None
        self.has_custom_certificate = dictionary["has_custom_certificate"] if "has_custom_certificate" in dictionary else None
        self.pending_update_count = dictionary["pending_update_count"] if "pending_update_count" in dictionary else None
        self.ip_address = dictionary["ip_address"] if "ip_address" in dictionary else None
        self.last_error_date = dictionary["last_error_date"] if "last_error_date" in dictionary else None
        self.last_error_message = dictionary["last_error_message"] if "last_error_message" in dictionary else None
        self.max_connections = dictionary["max_connections"] if "max_connections" in dictionary else None
        self.allowed_updates = list(dictionary["allowed_updates"]) if "allowed_updates" in dictionary else None

        for index, value in self.dict.items():
            if not hasattr(self, index):
                setattr(self, index, helper.setBvar(value))


class User(objects.User):
    """This object represents a Telegram user or bot.[See on Telegram API](https://core.telegram.org/bots/api#user)

    - - - - -
    **Fields**:

    - `id`: `int` - Unique identifier for this user or bot. This number may have more than 32 significant bits and some programming languages may have difficulty/silent defects in interpreting it. But it has at most 52 significant bits, so a 64-bit integer or double-precision float type are safe for storing this identifier.
    - `is_bot`: `bool` - True, if this user is a bot
    - `first_name`: `string` - User's or bot's first name
    - `last_name`: `string` - Optional. User's or bot's last name
    - `username`: `string` - Optional. User's or bot's username
    - `language_code`: `string` - Optional. IETF language tag of the user's language
    - `can_join_groups`: `bool` - Optional. True, if the bot can be invited to groups. Returned only in getMe.
    - `can_read_all_group_messages`: `bool` - Optional. True, if privacy mode is disabled for the bot. Returned only in getMe.
    - `supports_inline_queries`: `bool` - Optional. True, if the bot supports inline queries. Returned only in getMe.
    """

    def __init__(self, dictionary=None):
        if dictionary is None:
            dictionary = {}
        self.dict = dictionary
        self.id = dictionary["id"] if "id" in dictionary else None
        self.is_bot = dictionary["is_bot"] if "is_bot" in dictionary else None
        self.first_name = dictionary["first_name"] if "first_name" in dictionary else None
        self.last_name = dictionary["last_name"] if "last_name" in dictionary else None
        self.username = dictionary["username"] if "username" in dictionary else None
        self.language_code = dictionary["language_code"] if "language_code" in dictionary else None
        self.can_join_groups = dictionary["can_join_groups"] if "can_join_groups" in dictionary else None
        self.can_read_all_group_messages = dictionary["can_read_all_group_messages"] if "can_read_all_group_messages" in dictionary else None
        self.supports_inline_queries = dictionary["supports_inline_queries"] if "supports_inline_queries" in dictionary else None

        for index, value in self.dict.items():
            if not hasattr(self, index):
                setattr(self, index, helper.setBvar(value))


class Chat(objects.Chat):
    """This object represents a chat.[See on Telegram API](https://core.telegram.org/bots/api#chat)

    - - - - -
    **Fields**:

    - `id`: `int` - Unique identifier for this chat. This number may have more than 32 significant bits and some programming languages may have difficulty/silent defects in interpreting it. But it has at most 52 significant bits, so a signed 64-bit integer or double-precision float type are safe for storing this identifier.
    - `type`: `string` - Type of chat, can be either “private”, “group”, “supergroup” or “channel”
    - `title`: `string` - Optional. Title, for supergroups, channels and group chats
    - `username`: `string` - Optional. Username, for private chats, supergroups and channels if available
    - `first_name`: `string` - Optional. First name of the other party in a private chat
    - `last_name`: `string` - Optional. Last name of the other party in a private chat
    - `photo`: `ChatPhoto` - Optional. Chat photo. Returned only in getChat.
    - `bio`: `string` - Optional. Bio of the other party in a private chat. Returned only in getChat.
    - `has_private_forwards`: `bool` - Optional. True, if privacy settings of the other party in the private chat allows to use tg://user?id=<user_id> links only in chats with the user. Returned only in getChat.
    - `description`: `string` - Optional. Description, for groups, supergroups and channel chats. Returned only in getChat.
    - `invite_link`: `string` - Optional. Primary invite link, for groups, supergroups and channel chats. Returned only in getChat.
    - `pinned_message`: `Message` - Optional. The most recent pinned message (by sending date). Returned only in getChat.
    - `permissions`: `ChatPermissions` - Optional. Default chat member permissions, for groups and supergroups. Returned only in getChat.
    - `slow_mode_delay`: `int` - Optional. For supergroups, the minimum allowed delay between consecutive messages sent by each unpriviledged user; in seconds. Returned only in getChat.
    - `message_auto_delete_time`: `int` - Optional. The time after which all messages sent to the chat will be automatically deleted; in seconds. Returned only in getChat.
    - `has_protected_content`: `bool` - Optional. True, if messages from the chat can't be forwarded to other chats. Returned only in getChat.
    - `sticker_set_name`: `string` - Optional. For supergroups, name of group sticker set. Returned only in getChat.
    - `can_set_sticker_set`: `bool` - Optional. True, if the bot can change the group sticker set. Returned only in getChat.
    - `linked_chat_id`: `int` - Optional. Unique identifier for the linked chat, i.e. the discussion group identifier for a channel and vice versa; for supergroups and channel chats. This identifier may be greater than 32 bits and some programming languages may have difficulty/silent defects in interpreting it. But it is smaller than 52 bits, so a signed 64 bit integer or double-precision float type are safe for storing this identifier. Returned only in getChat.
    - `location`: `ChatLocation` - Optional. For supergroups, the location to which the supergroup is connected. Returned only in getChat.
    """

    def __init__(self, dictionary=None):
        if dictionary is None:
            dictionary = {}
        self.dict = dictionary
        self.id = dictionary["id"] if "id" in dictionary else None
        self.type = dictionary["type"] if "type" in dictionary else None
        self.title = dictionary["title"] if "title" in dictionary else None
        self.username = dictionary["username"] if "username" in dictionary else None
        self.first_name = dictionary["first_name"] if "first_name" in dictionary else None
        self.last_name = dictionary["last_name"] if "last_name" in dictionary else None
        self.photo = ChatPhoto(dictionary["photo"]) if "photo" in dictionary else None
        self.bio = dictionary["bio"] if "bio" in dictionary else None
        self.has_private_forwards = dictionary["has_private_forwards"] if "has_private_forwards" in dictionary else None
        self.description = dictionary["description"] if "description" in dictionary else None
        self.invite_link = dictionary["invite_link"] if "invite_link" in dictionary else None
        self.pinned_message = Message(dictionary["pinned_message"]) if "pinned_message" in dictionary else None
        self.permissions = ChatPermissions(dictionary["permissions"]) if "permissions" in dictionary else None
        self.slow_mode_delay = dictionary["slow_mode_delay"] if "slow_mode_delay" in dictionary else None
        self.message_auto_delete_time = dictionary["message_auto_delete_time"] if "message_auto_delete_time" in dictionary else None
        self.has_protected_content = dictionary["has_protected_content"] if "has_protected_content" in dictionary else None
        self.sticker_set_name = dictionary["sticker_set_name"] if "sticker_set_name" in dictionary else None
        self.can_set_sticker_set = dictionary["can_set_sticker_set"] if "can_set_sticker_set" in dictionary else None
        self.linked_chat_id = dictionary["linked_chat_id"] if "linked_chat_id" in dictionary else None
        self.location = ChatLocation(dictionary["location"]) if "location" in dictionary else None

        for index, value in self.dict.items():
            if not hasattr(self, index):
                setattr(self, index, helper.setBvar(value))


class Message:
    """This object represents a message.[See on Telegram API](https://core.telegram.org/bots/api#message)

    - - - - -
    **Fields**:

    - `message_id`: `int` - Unique message identifier inside this chat
    - `user`: `User` - Optional. Sender, empty for messages sent to channels
    - `sender_chat`: `Chat` - Optional. Sender of the message, sent on behalf of a chat. The channel itself for channel messages. The supergroup itself for messages from anonymous group administrators. The linked channel for messages automatically forwarded to the discussion group
    - `date`: `int` - Date the message was sent in Unix time
    - `chat`: `Chat` - Conversation the message belongs to
    - `forward_from`: `User` - Optional. For forwarded messages, sender of the original message
    - `forward_from_chat`: `Chat` - Optional. For messages forwarded from channels or from anonymous administrators, information about the original sender chat
    - `forward_from_message_id`: `int` - Optional. For messages forwarded from channels, identifier of the original message in the channel
    - `forward_signature`: `string` - Optional. For messages forwarded from channels, signature of the post author if present
    - `forward_sender_name`: `string` - Optional. Sender's name for messages forwarded from users who disallow adding a link to their account in forwarded messages
    - `forward_date`: `int` - Optional. For forwarded messages, date the original message was sent in Unix time
    - `is_automatic_forward`: `bool` - Optional. True, if the message is a channel post that was automatically forwarded to the connected discussion group
    - `reply_to_message`: `Message` - Optional. For replies, the original message. Note that the Message object in this field will not contain further reply_to_message fields even if it itself is a reply.
    - `via_bot`: `User` - Optional. Bot through which the message was sent
    - `edit_date`: `int` - Optional. Date the message was last edited in Unix time
    - `has_protected_content`: `bool` - Optional. True, if the message can't be forwarded
    - `media_group_id`: `string` - Optional. The unique identifier of a media message group this message belongs to
    - `author_signature`: `string` - Optional. Signature of the post author for messages in channels, or the custom title of an anonymous group administrator
    - `text`: `string` - Optional. For text messages, the actual UTF-8 text of the message, 0-4096 characters
    - `entities`: `list` - Optional. For text messages, special entities like usernames, URLs, bot commands, etc. that appear in the text
    - `animation`: `Animation` - Optional. Message is an animation, information about the animation. For backward compatibility, when this field is set, the document field will also be set
    - `audio`: `Audio` - Optional. Message is an audio file, information about the file
    - `document`: `Document` - Optional. Message is a general file, information about the file
    - `photo`: `list` - Optional. Message is a photo, available sizes of the photo
    - `sticker`: `Sticker` - Optional. Message is a sticker, information about the sticker
    - `video`: `Video` - Optional. Message is a video, information about the video
    - `video_note`: `VideoNote` - Optional. Message is a video note, information about the video message
    - `voice`: `Voice` - Optional. Message is a voice message, information about the file
    - `caption`: `string` - Optional. Caption for the animation, audio, document, photo, video or voice, 0-1024 characters
    - `caption_entities`: `list` - Optional. For messages with a caption, special entities like usernames, URLs, bot commands, etc. that appear in the caption
    - `contact`: `Contact` - Optional. Message is a shared contact, information about the contact
    - `dice`: `Dice` - Optional. Message is a dice with random value
    - `game`: `Game` - Optional. Message is a game, information about the game. More about games »
    - `poll`: `Poll` - Optional. Message is a native poll, information about the poll
    - `venue`: `Venue` - Optional. Message is a venue, information about the venue. For backward compatibility, when this field is set, the location field will also be set
    - `location`: `Location` - Optional. Message is a shared location, information about the location
    - `new_chat_members`: `list` - Optional. New members that were added to the group or supergroup and information about them (the bot itself may be one of these members)
    - `left_chat_member`: `User` - Optional. A member was removed from the group, information about them (this member may be the bot itself)
    - `new_chat_title`: `string` - Optional. A chat title was changed to this value
    - `new_chat_photo`: `list` - Optional. A chat photo was change to this value
    - `delete_chat_photo`: `bool` - Optional. Service message: the chat photo was deleted
    - `group_chat_created`: `bool` - Optional. Service message: the group has been created
    - `supergroup_chat_created`: `bool` - Optional. Service message: the supergroup has been created. This field can't be received in a message coming through updates, because bot can't be a member of a supergroup when it is created. It can only be found in reply_to_message if someone replies to a very first message in a directly created supergroup.
    - `channel_chat_created`: `bool` - Optional. Service message: the channel has been created. This field can't be received in a message coming through updates, because bot can't be a member of a channel when it is created. It can only be found in reply_to_message if someone replies to a very first message in a channel.
    - `message_auto_delete_timer_changed`: `MessageAutoDeleteTimerChanged` - Optional. Service message: auto-delete timer settings changed in the chat
    - `migrate_to_chat_id`: `int` - Optional. The group has been migrated to a supergroup with the specified identifier. This number may have more than 32 significant bits and some programming languages may have difficulty/silent defects in interpreting it. But it has at most 52 significant bits, so a signed 64-bit integer or double-precision float type are safe for storing this identifier.
    - `migrate_from_chat_id`: `int` - Optional. The supergroup has been migrated from a group with the specified identifier. This number may have more than 32 significant bits and some programming languages may have difficulty/silent defects in interpreting it. But it has at most 52 significant bits, so a signed 64-bit integer or double-precision float type are safe for storing this identifier.
    - `pinned_message`: `Message` - Optional. Specified message was pinned. Note that the Message object in this field will not contain further reply_to_message fields even if it is itself a reply.
    - `invoice`: `Invoice` - Optional. Message is an invoice for a payment, information about the invoice. More about payments »
    - `successful_payment`: `SuccessfulPayment` - Optional. Message is a service message about a successful payment, information about the payment. More about payments »
    - `connected_website`: `string` - Optional. The domain name of the website on which the user has logged in. More about Telegram Login »
    - `passport_data`: `PassportData` - Optional. Telegram Passport data
    - `proximity_alert_triggered`: `ProximityAlertTriggered` - Optional. Service message. A user in the chat triggered another user's proximity alert while sharing Live Location.
    - `voice_chat_scheduled`: `VoiceChatScheduled` - Optional. Service message: voice chat scheduled
    - `voice_chat_started`: `VoiceChatStarted` - Optional. Service message: voice chat started
    - `voice_chat_ended`: `VoiceChatEnded` - Optional. Service message: voice chat ended
    - `voice_chat_participants_invited`: `VoiceChatParticipantsInvited` - Optional. Service message: new participants invited to a voice chat
    - `reply_markup`: `InlineKeyboardMarkup` - Optional. Inline keyboard attached to the message. login_url buttons are represented as ordinary url buttons.
    """

    def __init__(self, dictionary=None):
        if dictionary is None:
            dictionary = {}
        self.dict = dictionary
        self.message_id = dictionary["message_id"] if "message_id" in dictionary else None
        self.user = User(dictionary["from"]) if "from" in dictionary else None
        self.sender_chat = Chat(dictionary["sender_chat"]) if "sender_chat" in dictionary else None
        self.date = dictionary["date"] if "date" in dictionary else None
        self.chat = Chat(dictionary["chat"]) if "chat" in dictionary else None
        self.forward_from = User(dictionary["forward_from"]) if "forward_from" in dictionary else None
        self.forward_from_chat = Chat(dictionary["forward_from_chat"]) if "forward_from_chat" in dictionary else None
        self.forward_from_message_id = dictionary["forward_from_message_id"] if "forward_from_message_id" in dictionary else None
        self.forward_signature = dictionary["forward_signature"] if "forward_signature" in dictionary else None
        self.forward_sender_name = dictionary["forward_sender_name"] if "forward_sender_name" in dictionary else None
        self.forward_date = dictionary["forward_date"] if "forward_date" in dictionary else None
        self.is_automatic_forward = dictionary["is_automatic_forward"] if "is_automatic_forward" in dictionary else None
        self.reply_to_message = Message(dictionary["reply_to_message"]) if "reply_to_message" in dictionary else None
        self.via_bot = User(dictionary["via_bot"]) if "via_bot" in dictionary else None
        self.edit_date = dictionary["edit_date"] if "edit_date" in dictionary else None
        self.has_protected_content = dictionary["has_protected_content"] if "has_protected_content" in dictionary else None
        self.media_group_id = dictionary["media_group_id"] if "media_group_id" in dictionary else None
        self.author_signature = dictionary["author_signature"] if "author_signature" in dictionary else None
        self.text = dictionary["text"] if "text" in dictionary else None
        self.entities = list(dictionary["entities"]) if "entities" in dictionary else None
        self.animation = Animation(dictionary["animation"]) if "animation" in dictionary else None
        self.audio = Audio(dictionary["audio"]) if "audio" in dictionary else None
        self.document = Document(dictionary["document"]) if "document" in dictionary else None
        self.photo = list(dictionary["photo"]) if "photo" in dictionary else None
        self.sticker = Sticker(dictionary["sticker"]) if "sticker" in dictionary else None
        self.video = Video(dictionary["video"]) if "video" in dictionary else None
        self.video_note = VideoNote(dictionary["video_note"]) if "video_note" in dictionary else None
        self.voice = Voice(dictionary["voice"]) if "voice" in dictionary else None
        self.caption = dictionary["caption"] if "caption" in dictionary else None
        self.caption_entities = list(dictionary["caption_entities"]) if "caption_entities" in dictionary else None
        self.contact = Contact(dictionary["contact"]) if "contact" in dictionary else None
        self.dice = Dice(dictionary["dice"]) if "dice" in dictionary else None
        self.game = Game(dictionary["game"]) if "game" in dictionary else None
        self.poll = Poll(dictionary["poll"]) if "poll" in dictionary else None
        self.venue = Venue(dictionary["venue"]) if "venue" in dictionary else None
        self.location = Location(dictionary["location"]) if "location" in dictionary else None
        self.new_chat_members = list(dictionary["new_chat_members"]) if "new_chat_members" in dictionary else None
        self.left_chat_member = User(dictionary["left_chat_member"]) if "left_chat_member" in dictionary else None
        self.new_chat_title = dictionary["new_chat_title"] if "new_chat_title" in dictionary else None
        self.new_chat_photo = list(dictionary["new_chat_photo"]) if "new_chat_photo" in dictionary else None
        self.delete_chat_photo = dictionary["delete_chat_photo"] if "delete_chat_photo" in dictionary else None
        self.group_chat_created = dictionary["group_chat_created"] if "group_chat_created" in dictionary else None
        self.supergroup_chat_created = dictionary["supergroup_chat_created"] if "supergroup_chat_created" in dictionary else None
        self.channel_chat_created = dictionary["channel_chat_created"] if "channel_chat_created" in dictionary else None
        self.message_auto_delete_timer_changed = MessageAutoDeleteTimerChanged(dictionary["message_auto_delete_timer_changed"]) if "message_auto_delete_timer_changed" in dictionary else None
        self.migrate_to_chat_id = dictionary["migrate_to_chat_id"] if "migrate_to_chat_id" in dictionary else None
        self.migrate_from_chat_id = dictionary["migrate_from_chat_id"] if "migrate_from_chat_id" in dictionary else None
        self.pinned_message = Message(dictionary["pinned_message"]) if "pinned_message" in dictionary else None
        self.invoice = Invoice(dictionary["invoice"]) if "invoice" in dictionary else None
        self.successful_payment = SuccessfulPayment(dictionary["successful_payment"]) if "successful_payment" in dictionary else None
        self.connected_website = dictionary["connected_website"] if "connected_website" in dictionary else None
        self.passport_data = PassportData(dictionary["passport_data"]) if "passport_data" in dictionary else None
        self.proximity_alert_triggered = ProximityAlertTriggered(dictionary["proximity_alert_triggered"]) if "proximity_alert_triggered" in dictionary else None
        self.voice_chat_scheduled = VoiceChatScheduled(dictionary["voice_chat_scheduled"]) if "voice_chat_scheduled" in dictionary else None
        self.voice_chat_started = VoiceChatStarted(dictionary["voice_chat_started"]) if "voice_chat_started" in dictionary else None
        self.voice_chat_ended = VoiceChatEnded(dictionary["voice_chat_ended"]) if "voice_chat_ended" in dictionary else None
        self.voice_chat_participants_invited = VoiceChatParticipantsInvited(dictionary["voice_chat_participants_invited"]) if "voice_chat_participants_invited" in dictionary else None
        self.reply_markup = InlineKeyboardMarkup(dictionary["reply_markup"]) if "reply_markup" in dictionary else None

        for index, value in self.dict.items():
            if not hasattr(self, index):
                setattr(self, index, helper.setBvar(value))


class MessageId:
    """This object represents a unique message identifier.[See on Telegram API](https://core.telegram.org/bots/api#messageid)

    - - - - -
    **Fields**:

    - `message_id`: `int` - Unique message identifier
    """

    def __init__(self, dictionary=None):
        if dictionary is None:
            dictionary = {}
        self.dict = dictionary
        self.message_id = dictionary["message_id"] if "message_id" in dictionary else None

        for index, value in self.dict.items():
            if not hasattr(self, index):
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
        self.type = dictionary["type"] if "type" in dictionary else None
        self.offset = dictionary["offset"] if "offset" in dictionary else None
        self.length = dictionary["length"] if "length" in dictionary else None
        self.url = dictionary["url"] if "url" in dictionary else None
        self.user = User(dictionary["from"]) if "from" in dictionary else None
        self.language = dictionary["language"] if "language" in dictionary else None

        for index, value in self.dict.items():
            if not hasattr(self, index):
                setattr(self, index, helper.setBvar(value))


class PhotoSize:
    """This object represents one size of a photo or a file / sticker thumbnail.[See on Telegram API](https://core.telegram.org/bots/api#photosize)

    - - - - -
    **Fields**:

    - `file_id`: `string` - Identifier for this file, which can be used to download or reuse the file
    - `file_unique_id`: `string` - Unique identifier for this file, which is supposed to be the same over time and for different bots. Can't be used to download or reuse the file.
    - `width`: `int` - Photo width
    - `height`: `int` - Photo height
    - `file_size`: `int` - Optional. File size in bytes
    """

    def __init__(self, dictionary=None):
        if dictionary is None:
            dictionary = {}
        self.dict = dictionary
        self.file_id = dictionary["file_id"] if "file_id" in dictionary else None
        self.file_unique_id = dictionary["file_unique_id"] if "file_unique_id" in dictionary else None
        self.width = dictionary["width"] if "width" in dictionary else None
        self.height = dictionary["height"] if "height" in dictionary else None
        self.file_size = dictionary["file_size"] if "file_size" in dictionary else None

        for index, value in self.dict.items():
            if not hasattr(self, index):
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
    - `file_size`: `int` - Optional. File size in bytes
    """

    def __init__(self, dictionary=None):
        if dictionary is None:
            dictionary = {}
        self.dict = dictionary
        self.file_id = dictionary["file_id"] if "file_id" in dictionary else None
        self.file_unique_id = dictionary["file_unique_id"] if "file_unique_id" in dictionary else None
        self.width = dictionary["width"] if "width" in dictionary else None
        self.height = dictionary["height"] if "height" in dictionary else None
        self.duration = dictionary["duration"] if "duration" in dictionary else None
        self.thumb = PhotoSize(dictionary["thumb"]) if "thumb" in dictionary else None
        self.file_name = dictionary["file_name"] if "file_name" in dictionary else None
        self.mime_type = dictionary["mime_type"] if "mime_type" in dictionary else None
        self.file_size = dictionary["file_size"] if "file_size" in dictionary else None

        for index, value in self.dict.items():
            if not hasattr(self, index):
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
    - `file_name`: `string` - Optional. Original filename as defined by sender
    - `mime_type`: `string` - Optional. MIME type of the file as defined by sender
    - `file_size`: `int` - Optional. File size in bytes
    - `thumb`: `PhotoSize` - Optional. Thumbnail of the album cover to which the music file belongs
    """

    def __init__(self, dictionary=None):
        if dictionary is None:
            dictionary = {}
        self.dict = dictionary
        self.file_id = dictionary["file_id"] if "file_id" in dictionary else None
        self.file_unique_id = dictionary["file_unique_id"] if "file_unique_id" in dictionary else None
        self.duration = dictionary["duration"] if "duration" in dictionary else None
        self.performer = dictionary["performer"] if "performer" in dictionary else None
        self.title = dictionary["title"] if "title" in dictionary else None
        self.file_name = dictionary["file_name"] if "file_name" in dictionary else None
        self.mime_type = dictionary["mime_type"] if "mime_type" in dictionary else None
        self.file_size = dictionary["file_size"] if "file_size" in dictionary else None
        self.thumb = PhotoSize(dictionary["thumb"]) if "thumb" in dictionary else None

        for index, value in self.dict.items():
            if not hasattr(self, index):
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
    - `file_size`: `int` - Optional. File size in bytes
    """

    def __init__(self, dictionary=None):
        if dictionary is None:
            dictionary = {}
        self.dict = dictionary
        self.file_id = dictionary["file_id"] if "file_id" in dictionary else None
        self.file_unique_id = dictionary["file_unique_id"] if "file_unique_id" in dictionary else None
        self.thumb = PhotoSize(dictionary["thumb"]) if "thumb" in dictionary else None
        self.file_name = dictionary["file_name"] if "file_name" in dictionary else None
        self.mime_type = dictionary["mime_type"] if "mime_type" in dictionary else None
        self.file_size = dictionary["file_size"] if "file_size" in dictionary else None

        for index, value in self.dict.items():
            if not hasattr(self, index):
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
    - `file_name`: `string` - Optional. Original filename as defined by sender
    - `mime_type`: `string` - Optional. Mime type of a file as defined by sender
    - `file_size`: `int` - Optional. File size in bytes
    """

    def __init__(self, dictionary=None):
        if dictionary is None:
            dictionary = {}
        self.dict = dictionary
        self.file_id = dictionary["file_id"] if "file_id" in dictionary else None
        self.file_unique_id = dictionary["file_unique_id"] if "file_unique_id" in dictionary else None
        self.width = dictionary["width"] if "width" in dictionary else None
        self.height = dictionary["height"] if "height" in dictionary else None
        self.duration = dictionary["duration"] if "duration" in dictionary else None
        self.thumb = PhotoSize(dictionary["thumb"]) if "thumb" in dictionary else None
        self.file_name = dictionary["file_name"] if "file_name" in dictionary else None
        self.mime_type = dictionary["mime_type"] if "mime_type" in dictionary else None
        self.file_size = dictionary["file_size"] if "file_size" in dictionary else None

        for index, value in self.dict.items():
            if not hasattr(self, index):
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
    - `file_size`: `int` - Optional. File size in bytes
    """

    def __init__(self, dictionary=None):
        if dictionary is None:
            dictionary = {}
        self.dict = dictionary
        self.file_id = dictionary["file_id"] if "file_id" in dictionary else None
        self.file_unique_id = dictionary["file_unique_id"] if "file_unique_id" in dictionary else None
        self.length = dictionary["length"] if "length" in dictionary else None
        self.duration = dictionary["duration"] if "duration" in dictionary else None
        self.thumb = PhotoSize(dictionary["thumb"]) if "thumb" in dictionary else None
        self.file_size = dictionary["file_size"] if "file_size" in dictionary else None

        for index, value in self.dict.items():
            if not hasattr(self, index):
                setattr(self, index, helper.setBvar(value))


class Voice:
    """This object represents a voice note.[See on Telegram API](https://core.telegram.org/bots/api#voice)

    - - - - -
    **Fields**:

    - `file_id`: `string` - Identifier for this file, which can be used to download or reuse the file
    - `file_unique_id`: `string` - Unique identifier for this file, which is supposed to be the same over time and for different bots. Can't be used to download or reuse the file.
    - `duration`: `int` - Duration of the audio in seconds as defined by sender
    - `mime_type`: `string` - Optional. MIME type of the file as defined by sender
    - `file_size`: `int` - Optional. File size in bytes
    """

    def __init__(self, dictionary=None):
        if dictionary is None:
            dictionary = {}
        self.dict = dictionary
        self.file_id = dictionary["file_id"] if "file_id" in dictionary else None
        self.file_unique_id = dictionary["file_unique_id"] if "file_unique_id" in dictionary else None
        self.duration = dictionary["duration"] if "duration" in dictionary else None
        self.mime_type = dictionary["mime_type"] if "mime_type" in dictionary else None
        self.file_size = dictionary["file_size"] if "file_size" in dictionary else None

        for index, value in self.dict.items():
            if not hasattr(self, index):
                setattr(self, index, helper.setBvar(value))


class Contact:
    """This object represents a phone contact.[See on Telegram API](https://core.telegram.org/bots/api#contact)

    - - - - -
    **Fields**:

    - `phone_number`: `string` - Contact's phone number
    - `first_name`: `string` - Contact's first name
    - `last_name`: `string` - Optional. Contact's last name
    - `user_id`: `int` - Optional. Contact's user identifier in Telegram. This number may have more than 32 significant bits and some programming languages may have difficulty/silent defects in interpreting it. But it has at most 52 significant bits, so a 64-bit integer or double-precision float type are safe for storing this identifier.
    - `vcard`: `string` - Optional. Additional data about the contact in the form of a vCard
    """

    def __init__(self, dictionary=None):
        if dictionary is None:
            dictionary = {}
        self.dict = dictionary
        self.phone_number = dictionary["phone_number"] if "phone_number" in dictionary else None
        self.first_name = dictionary["first_name"] if "first_name" in dictionary else None
        self.last_name = dictionary["last_name"] if "last_name" in dictionary else None
        self.user_id = dictionary["user_id"] if "user_id" in dictionary else None
        self.vcard = dictionary["vcard"] if "vcard" in dictionary else None

        for index, value in self.dict.items():
            if not hasattr(self, index):
                setattr(self, index, helper.setBvar(value))


class Dice:
    """This object represents an animated emoji that displays a random value.[See on Telegram API](https://core.telegram.org/bots/api#dice)

    - - - - -
    **Fields**:

    - `emoji`: `string` - Emoji on which the dice throw animation is based
    - `value`: `int` - Value of the dice, 1-6 for “”, “” and “” base emoji, 1-5 for “” and “” base emoji, 1-64 for “” base emoji
    """

    def __init__(self, dictionary=None):
        if dictionary is None:
            dictionary = {}
        self.dict = dictionary
        self.emoji = dictionary["emoji"] if "emoji" in dictionary else None
        self.value = dictionary["value"] if "value" in dictionary else None

        for index, value in self.dict.items():
            if not hasattr(self, index):
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
        self.text = dictionary["text"] if "text" in dictionary else None
        self.voter_count = dictionary["voter_count"] if "voter_count" in dictionary else None

        for index, value in self.dict.items():
            if not hasattr(self, index):
                setattr(self, index, helper.setBvar(value))


class PollAnswer:
    """This object represents an answer of a user in a non-anonymous poll.[See on Telegram API](https://core.telegram.org/bots/api#pollanswer)

    - - - - -
    **Fields**:

    - `poll_id`: `string` - Unique poll identifier
    - `user`: `User` - The user, who changed the answer to the poll
    - `option_ids`: `list` - 0-based identifiers of answer options, chosen by the user. May be empty if the user retracted their vote.
    """

    def __init__(self, dictionary=None):
        if dictionary is None:
            dictionary = {}
        self.dict = dictionary
        self.poll_id = dictionary["poll_id"] if "poll_id" in dictionary else None
        self.user = User(dictionary["from"]) if "from" in dictionary else None
        self.option_ids = list(dictionary["option_ids"]) if "option_ids" in dictionary else None

        for index, value in self.dict.items():
            if not hasattr(self, index):
                setattr(self, index, helper.setBvar(value))


class Poll:
    """This object contains information about a poll.[See on Telegram API](https://core.telegram.org/bots/api#poll)

    - - - - -
    **Fields**:

    - `id`: `string` - Unique poll identifier
    - `question`: `string` - Poll question, 1-300 characters
    - `options`: `list` - List of poll options
    - `total_voter_count`: `int` - Total number of users that voted in the poll
    - `is_closed`: `bool` - True, if the poll is closed
    - `is_anonymous`: `bool` - True, if the poll is anonymous
    - `type`: `string` - Poll type, currently can be “regular” or “quiz”
    - `allows_multiple_answers`: `bool` - True, if the poll allows multiple answers
    - `correct_option_id`: `int` - Optional. 0-based identifier of the correct answer option. Available only for polls in the quiz mode, which are closed, or was sent (not forwarded) by the bot or to the private chat with the bot.
    - `explanation`: `string` - Optional. Text that is shown when a user chooses an incorrect answer or taps on the lamp icon in a quiz-style poll, 0-200 characters
    - `explanation_entities`: `list` - Optional. Special entities like usernames, URLs, bot commands, etc. that appear in the explanation
    - `open_period`: `int` - Optional. Amount of time in seconds the poll will be active after creation
    - `close_date`: `int` - Optional. Point in time (Unix timestamp) when the poll will be automatically closed
    """

    def __init__(self, dictionary=None):
        if dictionary is None:
            dictionary = {}
        self.dict = dictionary
        self.id = dictionary["id"] if "id" in dictionary else None
        self.question = dictionary["question"] if "question" in dictionary else None
        self.options = list(dictionary["options"]) if "options" in dictionary else None
        self.total_voter_count = dictionary["total_voter_count"] if "total_voter_count" in dictionary else None
        self.is_closed = dictionary["is_closed"] if "is_closed" in dictionary else None
        self.is_anonymous = dictionary["is_anonymous"] if "is_anonymous" in dictionary else None
        self.type = dictionary["type"] if "type" in dictionary else None
        self.allows_multiple_answers = dictionary["allows_multiple_answers"] if "allows_multiple_answers" in dictionary else None
        self.correct_option_id = dictionary["correct_option_id"] if "correct_option_id" in dictionary else None
        self.explanation = dictionary["explanation"] if "explanation" in dictionary else None
        self.explanation_entities = list(dictionary["explanation_entities"]) if "explanation_entities" in dictionary else None
        self.open_period = dictionary["open_period"] if "open_period" in dictionary else None
        self.close_date = dictionary["close_date"] if "close_date" in dictionary else None

        for index, value in self.dict.items():
            if not hasattr(self, index):
                setattr(self, index, helper.setBvar(value))


class Location:
    """This object represents a point on the map.[See on Telegram API](https://core.telegram.org/bots/api#location)

    - - - - -
    **Fields**:

    - `longitude`: `float` - Longitude as defined by sender
    - `latitude`: `float` - Latitude as defined by sender
    - `horizontal_accuracy`: `float` - Optional. The radius of uncertainty for the location, measured in meters; 0-1500
    - `live_period`: `int` - Optional. Time relative to the message sending date, during which the location can be updated; in seconds. For active live locations only.
    - `heading`: `int` - Optional. The direction in which user is moving, in degrees; 1-360. For active live locations only.
    - `proximity_alert_radius`: `int` - Optional. Maximum distance for proximity alerts about approaching another chat member, in meters. For sent live locations only.
    """

    def __init__(self, dictionary=None):
        if dictionary is None:
            dictionary = {}
        self.dict = dictionary
        self.longitude = dictionary["longitude"] if "longitude" in dictionary else None
        self.latitude = dictionary["latitude"] if "latitude" in dictionary else None
        self.horizontal_accuracy = dictionary["horizontal_accuracy"] if "horizontal_accuracy" in dictionary else None
        self.live_period = dictionary["live_period"] if "live_period" in dictionary else None
        self.heading = dictionary["heading"] if "heading" in dictionary else None
        self.proximity_alert_radius = dictionary["proximity_alert_radius"] if "proximity_alert_radius" in dictionary else None

        for index, value in self.dict.items():
            if not hasattr(self, index):
                setattr(self, index, helper.setBvar(value))


class Venue:
    """This object represents a venue.[See on Telegram API](https://core.telegram.org/bots/api#venue)

    - - - - -
    **Fields**:

    - `location`: `Location` - Venue location. Can't be a live location
    - `title`: `string` - Name of the venue
    - `address`: `string` - Address of the venue
    - `foursquare_id`: `string` - Optional. Foursquare identifier of the venue
    - `foursquare_type`: `string` - Optional. Foursquare type of the venue. (For example, “arts_entertainment/default”, “arts_entertainment/aquarium” or “food/icecream”.)
    - `google_place_id`: `string` - Optional. Google Places identifier of the venue
    - `google_place_type`: `string` - Optional. Google Places type of the venue. (See supported types.)
    """

    def __init__(self, dictionary=None):
        if dictionary is None:
            dictionary = {}
        self.dict = dictionary
        self.location = Location(dictionary["location"]) if "location" in dictionary else None
        self.title = dictionary["title"] if "title" in dictionary else None
        self.address = dictionary["address"] if "address" in dictionary else None
        self.foursquare_id = dictionary["foursquare_id"] if "foursquare_id" in dictionary else None
        self.foursquare_type = dictionary["foursquare_type"] if "foursquare_type" in dictionary else None
        self.google_place_id = dictionary["google_place_id"] if "google_place_id" in dictionary else None
        self.google_place_type = dictionary["google_place_type"] if "google_place_type" in dictionary else None

        for index, value in self.dict.items():
            if not hasattr(self, index):
                setattr(self, index, helper.setBvar(value))


class ProximityAlertTriggered:
    """This object represents the content of a service message, sent whenever a user in the chat triggers a proximity alert set by another user.[See on Telegram API](https://core.telegram.org/bots/api#proximityalerttriggered)

    - - - - -
    **Fields**:

    - `traveler`: `User` - User that triggered the alert
    - `watcher`: `User` - User that set the alert
    - `distance`: `int` - The distance between the users
    """

    def __init__(self, dictionary=None):
        if dictionary is None:
            dictionary = {}
        self.dict = dictionary
        self.traveler = User(dictionary["traveler"]) if "traveler" in dictionary else None
        self.watcher = User(dictionary["watcher"]) if "watcher" in dictionary else None
        self.distance = dictionary["distance"] if "distance" in dictionary else None

        for index, value in self.dict.items():
            if not hasattr(self, index):
                setattr(self, index, helper.setBvar(value))


class MessageAutoDeleteTimerChanged:
    """This object represents a service message about a change in auto-delete timer settings.[See on Telegram API](https://core.telegram.org/bots/api#messageautodeletetimerchanged)

    - - - - -
    **Fields**:

    - `message_auto_delete_time`: `int` - New auto-delete time for messages in the chat; in seconds
    """

    def __init__(self, dictionary=None):
        if dictionary is None:
            dictionary = {}
        self.dict = dictionary
        self.message_auto_delete_time = dictionary["message_auto_delete_time"] if "message_auto_delete_time" in dictionary else None

        for index, value in self.dict.items():
            if not hasattr(self, index):
                setattr(self, index, helper.setBvar(value))


class VoiceChatScheduled:
    """This object represents a service message about a voice chat scheduled in the chat.[See on Telegram API](https://core.telegram.org/bots/api#voicechatscheduled)

    - - - - -
    **Fields**:

    - `start_date`: `int` - Point in time (Unix timestamp) when the voice chat is supposed to be started by a chat administrator
    """

    def __init__(self, dictionary=None):
        if dictionary is None:
            dictionary = {}
        self.dict = dictionary
        self.start_date = dictionary["start_date"] if "start_date" in dictionary else None

        for index, value in self.dict.items():
            if not hasattr(self, index):
                setattr(self, index, helper.setBvar(value))


class VoiceChatStarted:
    """This object represents a service message about a voice chat started in the chat. Currently holds no information.[See on Telegram API](https://core.telegram.org/bots/api#voicechatstarted)

    - - - - -
    **Fields**:

    """

    def __init__(self, dictionary=None):
        if dictionary is None:
            dictionary = {}
        self.dict = dictionary

        for index, value in self.dict.items():
            if not hasattr(self, index):
                setattr(self, index, helper.setBvar(value))


class VoiceChatEnded:
    """This object represents a service message about a voice chat ended in the chat.[See on Telegram API](https://core.telegram.org/bots/api#voicechatended)

    - - - - -
    **Fields**:

    - `duration`: `int` - Voice chat duration in seconds
    """

    def __init__(self, dictionary=None):
        if dictionary is None:
            dictionary = {}
        self.dict = dictionary
        self.duration = dictionary["duration"] if "duration" in dictionary else None

        for index, value in self.dict.items():
            if not hasattr(self, index):
                setattr(self, index, helper.setBvar(value))


class VoiceChatParticipantsInvited:
    """This object represents a service message about new members invited to a voice chat.[See on Telegram API](https://core.telegram.org/bots/api#voicechatparticipantsinvited)

    - - - - -
    **Fields**:

    - `users`: `list` - Optional. New members that were invited to the voice chat
    """

    def __init__(self, dictionary=None):
        if dictionary is None:
            dictionary = {}
        self.dict = dictionary
        self.users = list(dictionary["users"]) if "users" in dictionary else None

        for index, value in self.dict.items():
            if not hasattr(self, index):
                setattr(self, index, helper.setBvar(value))


class UserProfilePhotos:
    """This object represent a user's profile pictures.[See on Telegram API](https://core.telegram.org/bots/api#userprofilephotos)

    - - - - -
    **Fields**:

    - `total_count`: `int` - Total number of profile pictures the target user has
    - `photos`: `list` - Requested profile pictures (in up to 4 sizes each)
    """

    def __init__(self, dictionary=None):
        if dictionary is None:
            dictionary = {}
        self.dict = dictionary
        self.total_count = dictionary["total_count"] if "total_count" in dictionary else None
        self.photos = list(dictionary["photos"]) if "photos" in dictionary else None

        for index, value in self.dict.items():
            if not hasattr(self, index):
                setattr(self, index, helper.setBvar(value))


class File:
    """This object represents a file ready to be downloaded. The file can be downloaded via the link https://api.telegram.org/file/bot<token>/<file_path>. It is guaranteed that the link will be valid for at least 1 hour. When the link expires, a new one can be requested by calling getFile.[See on Telegram API](https://core.telegram.org/bots/api#file)

    - - - - -
    **Fields**:

    - `file_id`: `string` - Identifier for this file, which can be used to download or reuse the file
    - `file_unique_id`: `string` - Unique identifier for this file, which is supposed to be the same over time and for different bots. Can't be used to download or reuse the file.
    - `file_size`: `int` - Optional. File size in bytes, if known
    - `file_path`: `string` - Optional. File path. Use https://api.telegram.org/file/bot<token>/<file_path> to get the file.
    """

    def __init__(self, dictionary=None):
        if dictionary is None:
            dictionary = {}
        self.dict = dictionary
        self.file_id = dictionary["file_id"] if "file_id" in dictionary else None
        self.file_unique_id = dictionary["file_unique_id"] if "file_unique_id" in dictionary else None
        self.file_size = dictionary["file_size"] if "file_size" in dictionary else None
        self.file_path = dictionary["file_path"] if "file_path" in dictionary else None

        for index, value in self.dict.items():
            if not hasattr(self, index):
                setattr(self, index, helper.setBvar(value))


class ReplyKeyboardMarkup(objects.ReplyKeyboardMarkup):
    """This object represents a custom keyboard with reply options (see Introduction to bots for details and examples).[See on Telegram API](https://core.telegram.org/bots/api#replykeyboardmarkup)

    - - - - -
    **Fields**:

    - `keyboard`: `list` - Array of button rows, each represented by an Array of KeyboardButton objects
    - `resize_keyboard`: `bool` - Optional. Requests clients to resize the keyboard vertically for optimal fit (e.g., make the keyboard smaller if there are just two rows of buttons). Defaults to false, in which case the custom keyboard is always of the same height as the app's standard keyboard.
    - `one_time_keyboard`: `bool` - Optional. Requests clients to hide the keyboard as soon as it's been used. The keyboard will still be available, but clients will automatically display the usual letter-keyboard in the chat – the user can press a special button in the input field to see the custom keyboard again. Defaults to false.
    - `input_field_placeholder`: `string` - Optional. The placeholder to be shown in the input field when the keyboard is active; 1-64 characters
    - `selective`: `bool` - Optional. Use this parameter if you want to show the keyboard to specific users only. Targets: 1) users that are @mentioned in the text of the Message object; 2) if the bot's message is a reply (has reply_to_message_id), sender of the original message.Example: A user requests to change the bot's language, bot replies to the request with a keyboard to select the new language. Other users in the group don't see the keyboard.
    """

    def __init__(self, dictionary=None):
        if dictionary is None:
            dictionary = {}
        self.dict = dictionary
        self.keyboard = list(dictionary["keyboard"]) if "keyboard" in dictionary else None
        self.resize_keyboard = dictionary["resize_keyboard"] if "resize_keyboard" in dictionary else None
        self.one_time_keyboard = dictionary["one_time_keyboard"] if "one_time_keyboard" in dictionary else None
        self.input_field_placeholder = dictionary["input_field_placeholder"] if "input_field_placeholder" in dictionary else None
        self.selective = dictionary["selective"] if "selective" in dictionary else None

        for index, value in self.dict.items():
            if not hasattr(self, index):
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
        self.text = dictionary["text"] if "text" in dictionary else None
        self.request_contact = dictionary["request_contact"] if "request_contact" in dictionary else None
        self.request_location = dictionary["request_location"] if "request_location" in dictionary else None
        self.request_poll = KeyboardButtonPollType(dictionary["request_poll"]) if "request_poll" in dictionary else None

        for index, value in self.dict.items():
            if not hasattr(self, index):
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
        self.type = dictionary["type"] if "type" in dictionary else None

        for index, value in self.dict.items():
            if not hasattr(self, index):
                setattr(self, index, helper.setBvar(value))


class ReplyKeyboardRemove:
    """Upon receiving a message with this object, Telegram clients will remove the current custom keyboard and display the default letter-keyboard. By default, custom keyboards are displayed until a new keyboard is sent by a bot. An exception is made for one-time keyboards that are hidden immediately after the user presses a button (see ReplyKeyboardMarkup).[See on Telegram API](https://core.telegram.org/bots/api#replykeyboardremove)

    - - - - -
    **Fields**:

    - `remove_keyboard`: `bool` - Requests clients to remove the custom keyboard (user will not be able to summon this keyboard; if you want to hide the keyboard from sight but keep it accessible, use one_time_keyboard in ReplyKeyboardMarkup)
    - `selective`: `bool` - Optional. Use this parameter if you want to remove the keyboard for specific users only. Targets: 1) users that are @mentioned in the text of the Message object; 2) if the bot's message is a reply (has reply_to_message_id), sender of the original message.Example: A user votes in a poll, bot returns confirmation message in reply to the vote and removes the keyboard for that user, while still showing the keyboard with poll options to users who haven't voted yet.
    """

    def __init__(self, dictionary=None):
        if dictionary is None:
            dictionary = {}
        self.dict = dictionary
        self.remove_keyboard = dictionary["remove_keyboard"] if "remove_keyboard" in dictionary else None
        self.selective = dictionary["selective"] if "selective" in dictionary else None

        for index, value in self.dict.items():
            if not hasattr(self, index):
                setattr(self, index, helper.setBvar(value))


class InlineKeyboardMarkup(objects.InlineKeyboardMarkup):
    """This object represents an inline keyboard that appears right next to the message it belongs to.[See on Telegram API](https://core.telegram.org/bots/api#inlinekeyboardmarkup)

    - - - - -
    **Fields**:

    - `inline_keyboard`: `list` - Array of button rows, each represented by an Array of InlineKeyboardButton objects
    """

    def __init__(self, dictionary=None):
        if dictionary is None:
            dictionary = {}
        self.dict = dictionary
        self.inline_keyboard = list(dictionary["inline_keyboard"]) if "inline_keyboard" in dictionary else None

        for index, value in self.dict.items():
            if not hasattr(self, index):
                setattr(self, index, helper.setBvar(value))


class InlineKeyboardButton:
    """This object represents one button of an inline keyboard. You must use exactly one of the optional fields.[See on Telegram API](https://core.telegram.org/bots/api#inlinekeyboardbutton)

    - - - - -
    **Fields**:

    - `text`: `string` - Label text on the button
    - `url`: `string` - Optional. HTTP or tg:// url to be opened when the button is pressed. Links tg://user?id=<user_id> can be used to mention a user by their ID without using a username, if this is allowed by their privacy settings.
    - `login_url`: `LoginUrl` - Optional. An HTTP URL used to automatically authorize the user. Can be used as a replacement for the Telegram Login Widget.
    - `callback_data`: `string` - Optional. Data to be sent in a callback query to the bot when button is pressed, 1-64 bytes
    - `switch_inline_query`: `string` - Optional. If set, pressing the button will prompt the user to select one of their chats, open that chat and insert the bot's username and the specified inline query in the input field. Can be empty, in which case just the bot's username will be inserted.Note: This offers an easy way for users to start using your bot in inline mode when they are currently in a private chat with it. Especially useful when combined with switch_pm… actions – in this case the user will be automatically returned to the chat they switched from, skipping the chat selection screen.
    - `switch_inline_query_current_chat`: `string` - Optional. If set, pressing the button will insert the bot's username and the specified inline query in the current chat's input field. Can be empty, in which case only the bot's username will be inserted.This offers a quick way for the user to open your bot in inline mode in the same chat – good for selecting something from multiple options.
    - `callback_game`: `CallbackGame` - Optional. Description of the game that will be launched when the user presses the button.NOTE: This type of button must always be the first button in the first row.
    - `pay`: `bool` - Optional. Specify True, to send a Pay button.NOTE: This type of button must always be the first button in the first row and can only be used in invoice messages.
    """

    def __init__(self, dictionary=None):
        if dictionary is None:
            dictionary = {}
        self.dict = dictionary
        self.text = dictionary["text"] if "text" in dictionary else None
        self.url = dictionary["url"] if "url" in dictionary else None
        self.login_url = LoginUrl(dictionary["login_url"]) if "login_url" in dictionary else None
        self.callback_data = dictionary["callback_data"] if "callback_data" in dictionary else None
        self.switch_inline_query = dictionary["switch_inline_query"] if "switch_inline_query" in dictionary else None
        self.switch_inline_query_current_chat = dictionary["switch_inline_query_current_chat"] if "switch_inline_query_current_chat" in dictionary else None
        self.callback_game = CallbackGame(dictionary["callback_game"]) if "callback_game" in dictionary else None
        self.pay = dictionary["pay"] if "pay" in dictionary else None

        for index, value in self.dict.items():
            if not hasattr(self, index):
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
        self.url = dictionary["url"] if "url" in dictionary else None
        self.forward_text = dictionary["forward_text"] if "forward_text" in dictionary else None
        self.bot_username = dictionary["bot_username"] if "bot_username" in dictionary else None
        self.request_write_access = dictionary["request_write_access"] if "request_write_access" in dictionary else None

        for index, value in self.dict.items():
            if not hasattr(self, index):
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
        self.id = dictionary["id"] if "id" in dictionary else None
        self.user = User(dictionary["from"]) if "from" in dictionary else None
        self.message = Message(dictionary["message"]) if "message" in dictionary else None
        self.inline_message_id = dictionary["inline_message_id"] if "inline_message_id" in dictionary else None
        self.chat_instance = dictionary["chat_instance"] if "chat_instance" in dictionary else None
        self.data = dictionary["data"] if "data" in dictionary else None
        self.game_short_name = dictionary["game_short_name"] if "game_short_name" in dictionary else None

        for index, value in self.dict.items():
            if not hasattr(self, index):
                setattr(self, index, helper.setBvar(value))


class ForceReply:
    """Upon receiving a message with this object, Telegram clients will display a reply interface to the user (act as if the user has selected the bot's message and tapped 'Reply'). This can be extremely useful if you want to create user-friendly step-by-step interfaces without having to sacrifice privacy mode.[See on Telegram API](https://core.telegram.org/bots/api#forcereply)

    - - - - -
    **Fields**:

    - `force_reply`: `bool` - Shows reply interface to the user, as if they manually selected the bot's message and tapped 'Reply'
    - `input_field_placeholder`: `string` - Optional. The placeholder to be shown in the input field when the reply is active; 1-64 characters
    - `selective`: `bool` - Optional. Use this parameter if you want to force reply from specific users only. Targets: 1) users that are @mentioned in the text of the Message object; 2) if the bot's message is a reply (has reply_to_message_id), sender of the original message.
    """

    def __init__(self, dictionary=None):
        if dictionary is None:
            dictionary = {}
        self.dict = dictionary
        self.force_reply = dictionary["force_reply"] if "force_reply" in dictionary else None
        self.input_field_placeholder = dictionary["input_field_placeholder"] if "input_field_placeholder" in dictionary else None
        self.selective = dictionary["selective"] if "selective" in dictionary else None

        for index, value in self.dict.items():
            if not hasattr(self, index):
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
        self.small_file_id = dictionary["small_file_id"] if "small_file_id" in dictionary else None
        self.small_file_unique_id = dictionary["small_file_unique_id"] if "small_file_unique_id" in dictionary else None
        self.big_file_id = dictionary["big_file_id"] if "big_file_id" in dictionary else None
        self.big_file_unique_id = dictionary["big_file_unique_id"] if "big_file_unique_id" in dictionary else None

        for index, value in self.dict.items():
            if not hasattr(self, index):
                setattr(self, index, helper.setBvar(value))


class ChatInviteLink:
    """Represents an invite link for a chat.[See on Telegram API](https://core.telegram.org/bots/api#chatinvitelink)

    - - - - -
    **Fields**:

    - `invite_link`: `string` - The invite link. If the link was created by another chat administrator, then the second part of the link will be replaced with “…”.
    - `creator`: `User` - Creator of the link
    - `creates_join_request`: `bool` - True, if users joining the chat via the link need to be approved by chat administrators
    - `is_primary`: `bool` - True, if the link is primary
    - `is_revoked`: `bool` - True, if the link is revoked
    - `name`: `string` - Optional. Invite link name
    - `expire_date`: `int` - Optional. Point in time (Unix timestamp) when the link will expire or has been expired
    - `member_limit`: `int` - Optional. Maximum number of users that can be members of the chat simultaneously after joining the chat via this invite link; 1-99999
    - `pending_join_request_count`: `int` - Optional. Number of pending join requests created using this link
    """

    def __init__(self, dictionary=None):
        if dictionary is None:
            dictionary = {}
        self.dict = dictionary
        self.invite_link = dictionary["invite_link"] if "invite_link" in dictionary else None
        self.creator = User(dictionary["creator"]) if "creator" in dictionary else None
        self.creates_join_request = dictionary["creates_join_request"] if "creates_join_request" in dictionary else None
        self.is_primary = dictionary["is_primary"] if "is_primary" in dictionary else None
        self.is_revoked = dictionary["is_revoked"] if "is_revoked" in dictionary else None
        self.name = dictionary["name"] if "name" in dictionary else None
        self.expire_date = dictionary["expire_date"] if "expire_date" in dictionary else None
        self.member_limit = dictionary["member_limit"] if "member_limit" in dictionary else None
        self.pending_join_request_count = dictionary["pending_join_request_count"] if "pending_join_request_count" in dictionary else None

        for index, value in self.dict.items():
            if not hasattr(self, index):
                setattr(self, index, helper.setBvar(value))


class ChatMember:
    """This object contains information about one member of a chat. Currently, the following 6 types of chat members are supported:[See on Telegram API](https://core.telegram.org/bots/api#chatmember)

    - - - - -
    **Fields**:

    """

    def __init__(self, dictionary=None):
        if dictionary is None:
            dictionary = {}
        self.dict = dictionary

        for index, value in self.dict.items():
            if not hasattr(self, index):
                setattr(self, index, helper.setBvar(value))


class ChatMemberOwner:
    """Represents a chat member that owns the chat and has all administrator privileges.[See on Telegram API](https://core.telegram.org/bots/api#chatmemberowner)

    - - - - -
    **Fields**:

    - `status`: `string` - The member's status in the chat, always “creator”
    - `user`: `User` - Information about the user
    - `is_anonymous`: `bool` - True, if the user's presence in the chat is hidden
    - `custom_title`: `string` - Optional. Custom title for this user
    """

    def __init__(self, dictionary=None):
        if dictionary is None:
            dictionary = {}
        self.dict = dictionary
        self.status = dictionary["status"] if "status" in dictionary else None
        self.user = User(dictionary["from"]) if "from" in dictionary else None
        self.is_anonymous = dictionary["is_anonymous"] if "is_anonymous" in dictionary else None
        self.custom_title = dictionary["custom_title"] if "custom_title" in dictionary else None

        for index, value in self.dict.items():
            if not hasattr(self, index):
                setattr(self, index, helper.setBvar(value))


class ChatMemberAdministrator:
    """Represents a chat member that has some additional privileges.[See on Telegram API](https://core.telegram.org/bots/api#chatmemberadministrator)

    - - - - -
    **Fields**:

    - `status`: `string` - The member's status in the chat, always “administrator”
    - `user`: `User` - Information about the user
    - `can_be_edited`: `bool` - True, if the bot is allowed to edit administrator privileges of that user
    - `is_anonymous`: `bool` - True, if the user's presence in the chat is hidden
    - `can_manage_chat`: `bool` - True, if the administrator can access the chat event log, chat statistics, message statistics in channels, see channel members, see anonymous administrators in supergroups and ignore slow mode. Implied by any other administrator privilege
    - `can_delete_messages`: `bool` - True, if the administrator can delete messages of other users
    - `can_manage_voice_chats`: `bool` - True, if the administrator can manage voice chats
    - `can_restrict_members`: `bool` - True, if the administrator can restrict, ban or unban chat members
    - `can_promote_members`: `bool` - True, if the administrator can add new administrators with a subset of their own privileges or demote administrators that he has promoted, directly or indirectly (promoted by administrators that were appointed by the user)
    - `can_change_info`: `bool` - True, if the user is allowed to change the chat title, photo and other settings
    - `can_invite_users`: `bool` - True, if the user is allowed to invite new users to the chat
    - `can_post_messages`: `bool` - Optional. True, if the administrator can post in the channel; channels only
    - `can_edit_messages`: `bool` - Optional. True, if the administrator can edit messages of other users and can pin messages; channels only
    - `can_pin_messages`: `bool` - Optional. True, if the user is allowed to pin messages; groups and supergroups only
    - `custom_title`: `string` - Optional. Custom title for this user
    """

    def __init__(self, dictionary=None):
        if dictionary is None:
            dictionary = {}
        self.dict = dictionary
        self.status = dictionary["status"] if "status" in dictionary else None
        self.user = User(dictionary["from"]) if "from" in dictionary else None
        self.can_be_edited = dictionary["can_be_edited"] if "can_be_edited" in dictionary else None
        self.is_anonymous = dictionary["is_anonymous"] if "is_anonymous" in dictionary else None
        self.can_manage_chat = dictionary["can_manage_chat"] if "can_manage_chat" in dictionary else None
        self.can_delete_messages = dictionary["can_delete_messages"] if "can_delete_messages" in dictionary else None
        self.can_manage_voice_chats = dictionary["can_manage_voice_chats"] if "can_manage_voice_chats" in dictionary else None
        self.can_restrict_members = dictionary["can_restrict_members"] if "can_restrict_members" in dictionary else None
        self.can_promote_members = dictionary["can_promote_members"] if "can_promote_members" in dictionary else None
        self.can_change_info = dictionary["can_change_info"] if "can_change_info" in dictionary else None
        self.can_invite_users = dictionary["can_invite_users"] if "can_invite_users" in dictionary else None
        self.can_post_messages = dictionary["can_post_messages"] if "can_post_messages" in dictionary else None
        self.can_edit_messages = dictionary["can_edit_messages"] if "can_edit_messages" in dictionary else None
        self.can_pin_messages = dictionary["can_pin_messages"] if "can_pin_messages" in dictionary else None
        self.custom_title = dictionary["custom_title"] if "custom_title" in dictionary else None

        for index, value in self.dict.items():
            if not hasattr(self, index):
                setattr(self, index, helper.setBvar(value))


class ChatMemberMember:
    """Represents a chat member that has no additional privileges or restrictions.[See on Telegram API](https://core.telegram.org/bots/api#chatmembermember)

    - - - - -
    **Fields**:

    - `status`: `string` - The member's status in the chat, always “member”
    - `user`: `User` - Information about the user
    """

    def __init__(self, dictionary=None):
        if dictionary is None:
            dictionary = {}
        self.dict = dictionary
        self.status = dictionary["status"] if "status" in dictionary else None
        self.user = User(dictionary["from"]) if "from" in dictionary else None

        for index, value in self.dict.items():
            if not hasattr(self, index):
                setattr(self, index, helper.setBvar(value))


class ChatMemberRestricted:
    """Represents a chat member that is under certain restrictions in the chat. Supergroups only.[See on Telegram API](https://core.telegram.org/bots/api#chatmemberrestricted)

    - - - - -
    **Fields**:

    - `status`: `string` - The member's status in the chat, always “restricted”
    - `user`: `User` - Information about the user
    - `is_member`: `bool` - True, if the user is a member of the chat at the moment of the request
    - `can_change_info`: `bool` - True, if the user is allowed to change the chat title, photo and other settings
    - `can_invite_users`: `bool` - True, if the user is allowed to invite new users to the chat
    - `can_pin_messages`: `bool` - True, if the user is allowed to pin messages
    - `can_send_messages`: `bool` - True, if the user is allowed to send text messages, contacts, locations and venues
    - `can_send_media_messages`: `bool` - True, if the user is allowed to send audios, documents, photos, videos, video notes and voice notes
    - `can_send_polls`: `bool` - True, if the user is allowed to send polls
    - `can_send_other_messages`: `bool` - True, if the user is allowed to send animations, games, stickers and use inline bots
    - `can_add_web_page_previews`: `bool` - True, if the user is allowed to add web page previews to their messages
    - `until_date`: `int` - Date when restrictions will be lifted for this user; unix time. If 0, then the user is restricted forever
    """

    def __init__(self, dictionary=None):
        if dictionary is None:
            dictionary = {}
        self.dict = dictionary
        self.status = dictionary["status"] if "status" in dictionary else None
        self.user = User(dictionary["from"]) if "from" in dictionary else None
        self.is_member = dictionary["is_member"] if "is_member" in dictionary else None
        self.can_change_info = dictionary["can_change_info"] if "can_change_info" in dictionary else None
        self.can_invite_users = dictionary["can_invite_users"] if "can_invite_users" in dictionary else None
        self.can_pin_messages = dictionary["can_pin_messages"] if "can_pin_messages" in dictionary else None
        self.can_send_messages = dictionary["can_send_messages"] if "can_send_messages" in dictionary else None
        self.can_send_media_messages = dictionary["can_send_media_messages"] if "can_send_media_messages" in dictionary else None
        self.can_send_polls = dictionary["can_send_polls"] if "can_send_polls" in dictionary else None
        self.can_send_other_messages = dictionary["can_send_other_messages"] if "can_send_other_messages" in dictionary else None
        self.can_add_web_page_previews = dictionary["can_add_web_page_previews"] if "can_add_web_page_previews" in dictionary else None
        self.until_date = dictionary["until_date"] if "until_date" in dictionary else None

        for index, value in self.dict.items():
            if not hasattr(self, index):
                setattr(self, index, helper.setBvar(value))


class ChatMemberLeft:
    """Represents a chat member that isn't currently a member of the chat, but may join it themselves.[See on Telegram API](https://core.telegram.org/bots/api#chatmemberleft)

    - - - - -
    **Fields**:

    - `status`: `string` - The member's status in the chat, always “left”
    - `user`: `User` - Information about the user
    """

    def __init__(self, dictionary=None):
        if dictionary is None:
            dictionary = {}
        self.dict = dictionary
        self.status = dictionary["status"] if "status" in dictionary else None
        self.user = User(dictionary["from"]) if "from" in dictionary else None

        for index, value in self.dict.items():
            if not hasattr(self, index):
                setattr(self, index, helper.setBvar(value))


class ChatMemberBanned:
    """Represents a chat member that was banned in the chat and can't return to the chat or view chat messages.[See on Telegram API](https://core.telegram.org/bots/api#chatmemberbanned)

    - - - - -
    **Fields**:

    - `status`: `string` - The member's status in the chat, always “kicked”
    - `user`: `User` - Information about the user
    - `until_date`: `int` - Date when restrictions will be lifted for this user; unix time. If 0, then the user is banned forever
    """

    def __init__(self, dictionary=None):
        if dictionary is None:
            dictionary = {}
        self.dict = dictionary
        self.status = dictionary["status"] if "status" in dictionary else None
        self.user = User(dictionary["from"]) if "from" in dictionary else None
        self.until_date = dictionary["until_date"] if "until_date" in dictionary else None

        for index, value in self.dict.items():
            if not hasattr(self, index):
                setattr(self, index, helper.setBvar(value))


class ChatMemberUpdated:
    """This object represents changes in the status of a chat member.[See on Telegram API](https://core.telegram.org/bots/api#chatmemberupdated)

    - - - - -
    **Fields**:

    - `chat`: `Chat` - Chat the user belongs to
    - `user`: `User` - Performer of the action, which resulted in the change
    - `date`: `int` - Date the change was done in Unix time
    - `old_chat_member`: `ChatMember` - Previous information about the chat member
    - `new_chat_member`: `ChatMember` - New information about the chat member
    - `invite_link`: `ChatInviteLink` - Optional. Chat invite link, which was used by the user to join the chat; for joining by invite link events only.
    """

    def __init__(self, dictionary=None):
        if dictionary is None:
            dictionary = {}
        self.dict = dictionary
        self.chat = Chat(dictionary["chat"]) if "chat" in dictionary else None
        self.user = User(dictionary["from"]) if "from" in dictionary else None
        self.date = dictionary["date"] if "date" in dictionary else None
        self.old_chat_member = ChatMember(dictionary["old_chat_member"]) if "old_chat_member" in dictionary else None
        self.new_chat_member = ChatMember(dictionary["new_chat_member"]) if "new_chat_member" in dictionary else None
        self.invite_link = ChatInviteLink(dictionary["invite_link"]) if "invite_link" in dictionary else None

        for index, value in self.dict.items():
            if not hasattr(self, index):
                setattr(self, index, helper.setBvar(value))


class ChatJoinRequest:
    """Represents a join request sent to a chat.[See on Telegram API](https://core.telegram.org/bots/api#chatjoinrequest)

    - - - - -
    **Fields**:

    - `chat`: `Chat` - Chat to which the request was sent
    - `user`: `User` - User that sent the join request
    - `date`: `int` - Date the request was sent in Unix time
    - `bio`: `string` - Optional. Bio of the user.
    - `invite_link`: `ChatInviteLink` - Optional. Chat invite link that was used by the user to send the join request
    """

    def __init__(self, dictionary=None):
        if dictionary is None:
            dictionary = {}
        self.dict = dictionary
        self.chat = Chat(dictionary["chat"]) if "chat" in dictionary else None
        self.user = User(dictionary["from"]) if "from" in dictionary else None
        self.date = dictionary["date"] if "date" in dictionary else None
        self.bio = dictionary["bio"] if "bio" in dictionary else None
        self.invite_link = ChatInviteLink(dictionary["invite_link"]) if "invite_link" in dictionary else None

        for index, value in self.dict.items():
            if not hasattr(self, index):
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
        self.can_send_messages = dictionary["can_send_messages"] if "can_send_messages" in dictionary else None
        self.can_send_media_messages = dictionary["can_send_media_messages"] if "can_send_media_messages" in dictionary else None
        self.can_send_polls = dictionary["can_send_polls"] if "can_send_polls" in dictionary else None
        self.can_send_other_messages = dictionary["can_send_other_messages"] if "can_send_other_messages" in dictionary else None
        self.can_add_web_page_previews = dictionary["can_add_web_page_previews"] if "can_add_web_page_previews" in dictionary else None
        self.can_change_info = dictionary["can_change_info"] if "can_change_info" in dictionary else None
        self.can_invite_users = dictionary["can_invite_users"] if "can_invite_users" in dictionary else None
        self.can_pin_messages = dictionary["can_pin_messages"] if "can_pin_messages" in dictionary else None

        for index, value in self.dict.items():
            if not hasattr(self, index):
                setattr(self, index, helper.setBvar(value))


class ChatLocation:
    """Represents a location to which a chat is connected.[See on Telegram API](https://core.telegram.org/bots/api#chatlocation)

    - - - - -
    **Fields**:

    - `location`: `Location` - The location to which the supergroup is connected. Can't be a live location.
    - `address`: `string` - Location address; 1-64 characters, as defined by the chat owner
    """

    def __init__(self, dictionary=None):
        if dictionary is None:
            dictionary = {}
        self.dict = dictionary
        self.location = Location(dictionary["location"]) if "location" in dictionary else None
        self.address = dictionary["address"] if "address" in dictionary else None

        for index, value in self.dict.items():
            if not hasattr(self, index):
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
        self.command = dictionary["command"] if "command" in dictionary else None
        self.description = dictionary["description"] if "description" in dictionary else None

        for index, value in self.dict.items():
            if not hasattr(self, index):
                setattr(self, index, helper.setBvar(value))


class BotCommandScope:
    """This object represents the scope to which bot commands are applied. Currently, the following 7 scopes are supported:[See on Telegram API](https://core.telegram.org/bots/api#botcommandscope)

    - - - - -
    **Fields**:

    """

    def __init__(self, dictionary=None):
        if dictionary is None:
            dictionary = {}
        self.dict = dictionary

        for index, value in self.dict.items():
            if not hasattr(self, index):
                setattr(self, index, helper.setBvar(value))


class BotCommandScopeDefault:
    """Represents the default scope of bot commands. Default commands are used if no commands with a narrower scope are specified for the user.[See on Telegram API](https://core.telegram.org/bots/api#botcommandscopedefault)

    - - - - -
    **Fields**:

    - `type`: `string` - Scope type, must be default
    """

    def __init__(self, dictionary=None):
        if dictionary is None:
            dictionary = {}
        self.dict = dictionary
        self.type = dictionary["type"] if "type" in dictionary else None

        for index, value in self.dict.items():
            if not hasattr(self, index):
                setattr(self, index, helper.setBvar(value))


class BotCommandScopeAllPrivateChats:
    """Represents the scope of bot commands, covering all private chats.[See on Telegram API](https://core.telegram.org/bots/api#botcommandscopeallprivatechats)

    - - - - -
    **Fields**:

    - `type`: `string` - Scope type, must be all_private_chats
    """

    def __init__(self, dictionary=None):
        if dictionary is None:
            dictionary = {}
        self.dict = dictionary
        self.type = dictionary["type"] if "type" in dictionary else None

        for index, value in self.dict.items():
            if not hasattr(self, index):
                setattr(self, index, helper.setBvar(value))


class BotCommandScopeAllGroupChats:
    """Represents the scope of bot commands, covering all group and supergroup chats.[See on Telegram API](https://core.telegram.org/bots/api#botcommandscopeallgroupchats)

    - - - - -
    **Fields**:

    - `type`: `string` - Scope type, must be all_group_chats
    """

    def __init__(self, dictionary=None):
        if dictionary is None:
            dictionary = {}
        self.dict = dictionary
        self.type = dictionary["type"] if "type" in dictionary else None

        for index, value in self.dict.items():
            if not hasattr(self, index):
                setattr(self, index, helper.setBvar(value))


class BotCommandScopeAllChatAdministrators:
    """Represents the scope of bot commands, covering all group and supergroup chat administrators.[See on Telegram API](https://core.telegram.org/bots/api#botcommandscopeallchatadministrators)

    - - - - -
    **Fields**:

    - `type`: `string` - Scope type, must be all_chat_administrators
    """

    def __init__(self, dictionary=None):
        if dictionary is None:
            dictionary = {}
        self.dict = dictionary
        self.type = dictionary["type"] if "type" in dictionary else None

        for index, value in self.dict.items():
            if not hasattr(self, index):
                setattr(self, index, helper.setBvar(value))


class BotCommandScopeChat:
    """Represents the scope of bot commands, covering a specific chat.[See on Telegram API](https://core.telegram.org/bots/api#botcommandscopechat)

    - - - - -
    **Fields**:

    - `type`: `string` - Scope type, must be chat
    """

    def __init__(self, dictionary=None):
        if dictionary is None:
            dictionary = {}
        self.dict = dictionary
        self.type = dictionary["type"] if "type" in dictionary else None

        for index, value in self.dict.items():
            if not hasattr(self, index):
                setattr(self, index, helper.setBvar(value))


class BotCommandScopeChatAdministrators:
    """Represents the scope of bot commands, covering all administrators of a specific group or supergroup chat.[See on Telegram API](https://core.telegram.org/bots/api#botcommandscopechatadministrators)

    - - - - -
    **Fields**:

    - `type`: `string` - Scope type, must be chat_administrators
    """

    def __init__(self, dictionary=None):
        if dictionary is None:
            dictionary = {}
        self.dict = dictionary
        self.type = dictionary["type"] if "type" in dictionary else None

        for index, value in self.dict.items():
            if not hasattr(self, index):
                setattr(self, index, helper.setBvar(value))


class BotCommandScopeChatMember:
    """Represents the scope of bot commands, covering a specific member of a group or supergroup chat.[See on Telegram API](https://core.telegram.org/bots/api#botcommandscopechatmember)

    - - - - -
    **Fields**:

    - `type`: `string` - Scope type, must be chat_member
    - `user_id`: `int` - Unique identifier of the target user
    """

    def __init__(self, dictionary=None):
        if dictionary is None:
            dictionary = {}
        self.dict = dictionary
        self.type = dictionary["type"] if "type" in dictionary else None
        self.user_id = dictionary["user_id"] if "user_id" in dictionary else None

        for index, value in self.dict.items():
            if not hasattr(self, index):
                setattr(self, index, helper.setBvar(value))


class ResponseParameters:
    """Contains information about why a request was unsuccessful.[See on Telegram API](https://core.telegram.org/bots/api#responseparameters)

    - - - - -
    **Fields**:

    - `migrate_to_chat_id`: `int` - Optional. The group has been migrated to a supergroup with the specified identifier. This number may have more than 32 significant bits and some programming languages may have difficulty/silent defects in interpreting it. But it has at most 52 significant bits, so a signed 64-bit integer or double-precision float type are safe for storing this identifier.
    - `retry_after`: `int` - Optional. In case of exceeding flood control, the number of seconds left to wait before the request can be repeated
    """

    def __init__(self, dictionary=None):
        if dictionary is None:
            dictionary = {}
        self.dict = dictionary
        self.migrate_to_chat_id = dictionary["migrate_to_chat_id"] if "migrate_to_chat_id" in dictionary else None
        self.retry_after = dictionary["retry_after"] if "retry_after" in dictionary else None

        for index, value in self.dict.items():
            if not hasattr(self, index):
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
            if not hasattr(self, index):
                setattr(self, index, helper.setBvar(value))


class InputMediaPhoto:
    """Represents a photo to be sent.[See on Telegram API](https://core.telegram.org/bots/api#inputmediaphoto)

    - - - - -
    **Fields**:

    - `type`: `string` - Type of the result, must be photo
    - `media`: `string` - File to send. Pass a file_id to send a file that exists on the Telegram servers (recommended), pass an HTTP URL for Telegram to get a file from the Internet, or pass “attach://<file_attach_name>” to upload a new one using multipart/form-data under <file_attach_name> name. More info on Sending Files »
    - `caption`: `string` - Optional. Caption of the photo to be sent, 0-1024 characters after entities parsing
    - `parse_mode`: `string` - Optional. Mode for parsing entities in the photo caption. See formatting options for more details.
    - `caption_entities`: `list` - Optional. List of special entities that appear in the caption, which can be specified instead of parse_mode
    """

    def __init__(self, dictionary=None):
        if dictionary is None:
            dictionary = {}
        self.dict = dictionary
        self.type = dictionary["type"] if "type" in dictionary else None
        self.media = dictionary["media"] if "media" in dictionary else None
        self.caption = dictionary["caption"] if "caption" in dictionary else None
        self.parse_mode = dictionary["parse_mode"] if "parse_mode" in dictionary else None
        self.caption_entities = list(dictionary["caption_entities"]) if "caption_entities" in dictionary else None

        for index, value in self.dict.items():
            if not hasattr(self, index):
                setattr(self, index, helper.setBvar(value))


class InputMediaVideo:
    """Represents a video to be sent.[See on Telegram API](https://core.telegram.org/bots/api#inputmediavideo)

    - - - - -
    **Fields**:

    - `type`: `string` - Type of the result, must be video
    - `media`: `string` - File to send. Pass a file_id to send a file that exists on the Telegram servers (recommended), pass an HTTP URL for Telegram to get a file from the Internet, or pass “attach://<file_attach_name>” to upload a new one using multipart/form-data under <file_attach_name> name. More info on Sending Files »
    - `caption`: `string` - Optional. Caption of the video to be sent, 0-1024 characters after entities parsing
    - `parse_mode`: `string` - Optional. Mode for parsing entities in the video caption. See formatting options for more details.
    - `caption_entities`: `list` - Optional. List of special entities that appear in the caption, which can be specified instead of parse_mode
    - `width`: `int` - Optional. Video width
    - `height`: `int` - Optional. Video height
    - `duration`: `int` - Optional. Video duration in seconds
    - `supports_streaming`: `bool` - Optional. Pass True, if the uploaded video is suitable for streaming
    """

    def __init__(self, dictionary=None):
        if dictionary is None:
            dictionary = {}
        self.dict = dictionary
        self.type = dictionary["type"] if "type" in dictionary else None
        self.media = dictionary["media"] if "media" in dictionary else None
        self.caption = dictionary["caption"] if "caption" in dictionary else None
        self.parse_mode = dictionary["parse_mode"] if "parse_mode" in dictionary else None
        self.caption_entities = list(dictionary["caption_entities"]) if "caption_entities" in dictionary else None
        self.width = dictionary["width"] if "width" in dictionary else None
        self.height = dictionary["height"] if "height" in dictionary else None
        self.duration = dictionary["duration"] if "duration" in dictionary else None
        self.supports_streaming = dictionary["supports_streaming"] if "supports_streaming" in dictionary else None

        for index, value in self.dict.items():
            if not hasattr(self, index):
                setattr(self, index, helper.setBvar(value))


class InputMediaAnimation:
    """Represents an animation file (GIF or H.264/MPEG-4 AVC video without sound) to be sent.[See on Telegram API](https://core.telegram.org/bots/api#inputmediaanimation)

    - - - - -
    **Fields**:

    - `type`: `string` - Type of the result, must be animation
    - `media`: `string` - File to send. Pass a file_id to send a file that exists on the Telegram servers (recommended), pass an HTTP URL for Telegram to get a file from the Internet, or pass “attach://<file_attach_name>” to upload a new one using multipart/form-data under <file_attach_name> name. More info on Sending Files »
    - `caption`: `string` - Optional. Caption of the animation to be sent, 0-1024 characters after entities parsing
    - `parse_mode`: `string` - Optional. Mode for parsing entities in the animation caption. See formatting options for more details.
    - `caption_entities`: `list` - Optional. List of special entities that appear in the caption, which can be specified instead of parse_mode
    - `width`: `int` - Optional. Animation width
    - `height`: `int` - Optional. Animation height
    - `duration`: `int` - Optional. Animation duration in seconds
    """

    def __init__(self, dictionary=None):
        if dictionary is None:
            dictionary = {}
        self.dict = dictionary
        self.type = dictionary["type"] if "type" in dictionary else None
        self.media = dictionary["media"] if "media" in dictionary else None
        self.caption = dictionary["caption"] if "caption" in dictionary else None
        self.parse_mode = dictionary["parse_mode"] if "parse_mode" in dictionary else None
        self.caption_entities = list(dictionary["caption_entities"]) if "caption_entities" in dictionary else None
        self.width = dictionary["width"] if "width" in dictionary else None
        self.height = dictionary["height"] if "height" in dictionary else None
        self.duration = dictionary["duration"] if "duration" in dictionary else None

        for index, value in self.dict.items():
            if not hasattr(self, index):
                setattr(self, index, helper.setBvar(value))


class InputMediaAudio:
    """Represents an audio file to be treated as music to be sent.[See on Telegram API](https://core.telegram.org/bots/api#inputmediaaudio)

    - - - - -
    **Fields**:

    - `type`: `string` - Type of the result, must be audio
    - `media`: `string` - File to send. Pass a file_id to send a file that exists on the Telegram servers (recommended), pass an HTTP URL for Telegram to get a file from the Internet, or pass “attach://<file_attach_name>” to upload a new one using multipart/form-data under <file_attach_name> name. More info on Sending Files »
    - `caption`: `string` - Optional. Caption of the audio to be sent, 0-1024 characters after entities parsing
    - `parse_mode`: `string` - Optional. Mode for parsing entities in the audio caption. See formatting options for more details.
    - `caption_entities`: `list` - Optional. List of special entities that appear in the caption, which can be specified instead of parse_mode
    - `duration`: `int` - Optional. Duration of the audio in seconds
    - `performer`: `string` - Optional. Performer of the audio
    - `title`: `string` - Optional. Title of the audio
    """

    def __init__(self, dictionary=None):
        if dictionary is None:
            dictionary = {}
        self.dict = dictionary
        self.type = dictionary["type"] if "type" in dictionary else None
        self.media = dictionary["media"] if "media" in dictionary else None
        self.caption = dictionary["caption"] if "caption" in dictionary else None
        self.parse_mode = dictionary["parse_mode"] if "parse_mode" in dictionary else None
        self.caption_entities = list(dictionary["caption_entities"]) if "caption_entities" in dictionary else None
        self.duration = dictionary["duration"] if "duration" in dictionary else None
        self.performer = dictionary["performer"] if "performer" in dictionary else None
        self.title = dictionary["title"] if "title" in dictionary else None

        for index, value in self.dict.items():
            if not hasattr(self, index):
                setattr(self, index, helper.setBvar(value))


class InputMediaDocument:
    """Represents a general file to be sent.[See on Telegram API](https://core.telegram.org/bots/api#inputmediadocument)

    - - - - -
    **Fields**:

    - `type`: `string` - Type of the result, must be document
    - `media`: `string` - File to send. Pass a file_id to send a file that exists on the Telegram servers (recommended), pass an HTTP URL for Telegram to get a file from the Internet, or pass “attach://<file_attach_name>” to upload a new one using multipart/form-data under <file_attach_name> name. More info on Sending Files »
    - `caption`: `string` - Optional. Caption of the document to be sent, 0-1024 characters after entities parsing
    - `parse_mode`: `string` - Optional. Mode for parsing entities in the document caption. See formatting options for more details.
    - `caption_entities`: `list` - Optional. List of special entities that appear in the caption, which can be specified instead of parse_mode
    - `disable_content_type_detection`: `bool` - Optional. Disables automatic server-side content type detection for files uploaded using multipart/form-data. Always True, if the document is sent as part of an album.
    """

    def __init__(self, dictionary=None):
        if dictionary is None:
            dictionary = {}
        self.dict = dictionary
        self.type = dictionary["type"] if "type" in dictionary else None
        self.media = dictionary["media"] if "media" in dictionary else None
        self.caption = dictionary["caption"] if "caption" in dictionary else None
        self.parse_mode = dictionary["parse_mode"] if "parse_mode" in dictionary else None
        self.caption_entities = list(dictionary["caption_entities"]) if "caption_entities" in dictionary else None
        self.disable_content_type_detection = dictionary["disable_content_type_detection"] if "disable_content_type_detection" in dictionary else None

        for index, value in self.dict.items():
            if not hasattr(self, index):
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
            if not hasattr(self, index):
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
    - `file_size`: `int` - Optional. File size in bytes
    """

    def __init__(self, dictionary=None):
        if dictionary is None:
            dictionary = {}
        self.dict = dictionary
        self.file_id = dictionary["file_id"] if "file_id" in dictionary else None
        self.file_unique_id = dictionary["file_unique_id"] if "file_unique_id" in dictionary else None
        self.width = dictionary["width"] if "width" in dictionary else None
        self.height = dictionary["height"] if "height" in dictionary else None
        self.is_animated = dictionary["is_animated"] if "is_animated" in dictionary else None
        self.thumb = PhotoSize(dictionary["thumb"]) if "thumb" in dictionary else None
        self.emoji = dictionary["emoji"] if "emoji" in dictionary else None
        self.set_name = dictionary["set_name"] if "set_name" in dictionary else None
        self.mask_position = MaskPosition(dictionary["mask_position"]) if "mask_position" in dictionary else None
        self.file_size = dictionary["file_size"] if "file_size" in dictionary else None

        for index, value in self.dict.items():
            if not hasattr(self, index):
                setattr(self, index, helper.setBvar(value))


class StickerSet:
    """This object represents a sticker set.[See on Telegram API](https://core.telegram.org/bots/api#stickerset)

    - - - - -
    **Fields**:

    - `name`: `string` - Sticker set name
    - `title`: `string` - Sticker set title
    - `is_animated`: `bool` - True, if the sticker set contains animated stickers
    - `contains_masks`: `bool` - True, if the sticker set contains masks
    - `stickers`: `list` - List of all set stickers
    - `thumb`: `PhotoSize` - Optional. Sticker set thumbnail in the .WEBP or .TGS format
    """

    def __init__(self, dictionary=None):
        if dictionary is None:
            dictionary = {}
        self.dict = dictionary
        self.name = dictionary["name"] if "name" in dictionary else None
        self.title = dictionary["title"] if "title" in dictionary else None
        self.is_animated = dictionary["is_animated"] if "is_animated" in dictionary else None
        self.contains_masks = dictionary["contains_masks"] if "contains_masks" in dictionary else None
        self.stickers = list(dictionary["stickers"]) if "stickers" in dictionary else None
        self.thumb = PhotoSize(dictionary["thumb"]) if "thumb" in dictionary else None

        for index, value in self.dict.items():
            if not hasattr(self, index):
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
        self.point = dictionary["point"] if "point" in dictionary else None
        self.x_shift = dictionary["x_shift"] if "x_shift" in dictionary else None
        self.y_shift = dictionary["y_shift"] if "y_shift" in dictionary else None
        self.scale = dictionary["scale"] if "scale" in dictionary else None

        for index, value in self.dict.items():
            if not hasattr(self, index):
                setattr(self, index, helper.setBvar(value))


class InlineQuery:
    """This object represents an incoming inline query. When the user sends an empty query, your bot could return some default or trending results.[See on Telegram API](https://core.telegram.org/bots/api#inlinequery)

    - - - - -
    **Fields**:

    - `id`: `string` - Unique identifier for this query
    - `user`: `User` - Sender
    - `query`: `string` - Text of the query (up to 256 characters)
    - `offset`: `string` - Offset of the results to be returned, can be controlled by the bot
    - `chat_type`: `string` - Optional. Type of the chat, from which the inline query was sent. Can be either “sender” for a private chat with the inline query sender, “private”, “group”, “supergroup”, or “channel”. The chat type should be always known for requests sent from official clients and most third-party clients, unless the request was sent from a secret chat
    - `location`: `Location` - Optional. Sender location, only for bots that request user location
    """

    def __init__(self, dictionary=None):
        if dictionary is None:
            dictionary = {}
        self.dict = dictionary
        self.id = dictionary["id"] if "id" in dictionary else None
        self.user = User(dictionary["from"]) if "from" in dictionary else None
        self.query = dictionary["query"] if "query" in dictionary else None
        self.offset = dictionary["offset"] if "offset" in dictionary else None
        self.chat_type = dictionary["chat_type"] if "chat_type" in dictionary else None
        self.location = Location(dictionary["location"]) if "location" in dictionary else None

        for index, value in self.dict.items():
            if not hasattr(self, index):
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
            if not hasattr(self, index):
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
        self.type = dictionary["type"] if "type" in dictionary else None
        self.id = dictionary["id"] if "id" in dictionary else None
        self.title = dictionary["title"] if "title" in dictionary else None
        self.input_message_content = InputMessageContent(dictionary["input_message_content"]) if "input_message_content" in dictionary else None
        self.reply_markup = InlineKeyboardMarkup(dictionary["reply_markup"]) if "reply_markup" in dictionary else None
        self.url = dictionary["url"] if "url" in dictionary else None
        self.hide_url = dictionary["hide_url"] if "hide_url" in dictionary else None
        self.description = dictionary["description"] if "description" in dictionary else None
        self.thumb_url = dictionary["thumb_url"] if "thumb_url" in dictionary else None
        self.thumb_width = dictionary["thumb_width"] if "thumb_width" in dictionary else None
        self.thumb_height = dictionary["thumb_height"] if "thumb_height" in dictionary else None

        for index, value in self.dict.items():
            if not hasattr(self, index):
                setattr(self, index, helper.setBvar(value))


class InlineQueryResultPhoto:
    """Represents a link to a photo. By default, this photo will be sent by the user with optional caption. Alternatively, you can use input_message_content to send a message with the specified content instead of the photo.[See on Telegram API](https://core.telegram.org/bots/api#inlinequeryresultphoto)

    - - - - -
    **Fields**:

    - `type`: `string` - Type of the result, must be photo
    - `id`: `string` - Unique identifier for this result, 1-64 bytes
    - `photo_url`: `string` - A valid URL of the photo. Photo must be in JPEG format. Photo size must not exceed 5MB
    - `thumb_url`: `string` - URL of the thumbnail for the photo
    - `photo_width`: `int` - Optional. Width of the photo
    - `photo_height`: `int` - Optional. Height of the photo
    - `title`: `string` - Optional. Title for the result
    - `description`: `string` - Optional. Short description of the result
    - `caption`: `string` - Optional. Caption of the photo to be sent, 0-1024 characters after entities parsing
    - `parse_mode`: `string` - Optional. Mode for parsing entities in the photo caption. See formatting options for more details.
    - `caption_entities`: `list` - Optional. List of special entities that appear in the caption, which can be specified instead of parse_mode
    - `reply_markup`: `InlineKeyboardMarkup` - Optional. Inline keyboard attached to the message
    - `input_message_content`: `InputMessageContent` - Optional. Content of the message to be sent instead of the photo
    """

    def __init__(self, dictionary=None):
        if dictionary is None:
            dictionary = {}
        self.dict = dictionary
        self.type = dictionary["type"] if "type" in dictionary else None
        self.id = dictionary["id"] if "id" in dictionary else None
        self.photo_url = dictionary["photo_url"] if "photo_url" in dictionary else None
        self.thumb_url = dictionary["thumb_url"] if "thumb_url" in dictionary else None
        self.photo_width = dictionary["photo_width"] if "photo_width" in dictionary else None
        self.photo_height = dictionary["photo_height"] if "photo_height" in dictionary else None
        self.title = dictionary["title"] if "title" in dictionary else None
        self.description = dictionary["description"] if "description" in dictionary else None
        self.caption = dictionary["caption"] if "caption" in dictionary else None
        self.parse_mode = dictionary["parse_mode"] if "parse_mode" in dictionary else None
        self.caption_entities = list(dictionary["caption_entities"]) if "caption_entities" in dictionary else None
        self.reply_markup = InlineKeyboardMarkup(dictionary["reply_markup"]) if "reply_markup" in dictionary else None
        self.input_message_content = InputMessageContent(dictionary["input_message_content"]) if "input_message_content" in dictionary else None

        for index, value in self.dict.items():
            if not hasattr(self, index):
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
    - `gif_duration`: `int` - Optional. Duration of the GIF in seconds
    - `thumb_url`: `string` - URL of the static (JPEG or GIF) or animated (MPEG4) thumbnail for the result
    - `thumb_mime_type`: `string` - Optional. MIME type of the thumbnail, must be one of “image/jpeg”, “image/gif”, or “video/mp4”. Defaults to “image/jpeg”
    - `title`: `string` - Optional. Title for the result
    - `caption`: `string` - Optional. Caption of the GIF file to be sent, 0-1024 characters after entities parsing
    - `parse_mode`: `string` - Optional. Mode for parsing entities in the caption. See formatting options for more details.
    - `caption_entities`: `list` - Optional. List of special entities that appear in the caption, which can be specified instead of parse_mode
    - `reply_markup`: `InlineKeyboardMarkup` - Optional. Inline keyboard attached to the message
    - `input_message_content`: `InputMessageContent` - Optional. Content of the message to be sent instead of the GIF animation
    """

    def __init__(self, dictionary=None):
        if dictionary is None:
            dictionary = {}
        self.dict = dictionary
        self.type = dictionary["type"] if "type" in dictionary else None
        self.id = dictionary["id"] if "id" in dictionary else None
        self.gif_url = dictionary["gif_url"] if "gif_url" in dictionary else None
        self.gif_width = dictionary["gif_width"] if "gif_width" in dictionary else None
        self.gif_height = dictionary["gif_height"] if "gif_height" in dictionary else None
        self.gif_duration = dictionary["gif_duration"] if "gif_duration" in dictionary else None
        self.thumb_url = dictionary["thumb_url"] if "thumb_url" in dictionary else None
        self.thumb_mime_type = dictionary["thumb_mime_type"] if "thumb_mime_type" in dictionary else None
        self.title = dictionary["title"] if "title" in dictionary else None
        self.caption = dictionary["caption"] if "caption" in dictionary else None
        self.parse_mode = dictionary["parse_mode"] if "parse_mode" in dictionary else None
        self.caption_entities = list(dictionary["caption_entities"]) if "caption_entities" in dictionary else None
        self.reply_markup = InlineKeyboardMarkup(dictionary["reply_markup"]) if "reply_markup" in dictionary else None
        self.input_message_content = InputMessageContent(dictionary["input_message_content"]) if "input_message_content" in dictionary else None

        for index, value in self.dict.items():
            if not hasattr(self, index):
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
    - `mpeg4_duration`: `int` - Optional. Video duration in seconds
    - `thumb_url`: `string` - URL of the static (JPEG or GIF) or animated (MPEG4) thumbnail for the result
    - `thumb_mime_type`: `string` - Optional. MIME type of the thumbnail, must be one of “image/jpeg”, “image/gif”, or “video/mp4”. Defaults to “image/jpeg”
    - `title`: `string` - Optional. Title for the result
    - `caption`: `string` - Optional. Caption of the MPEG-4 file to be sent, 0-1024 characters after entities parsing
    - `parse_mode`: `string` - Optional. Mode for parsing entities in the caption. See formatting options for more details.
    - `caption_entities`: `list` - Optional. List of special entities that appear in the caption, which can be specified instead of parse_mode
    - `reply_markup`: `InlineKeyboardMarkup` - Optional. Inline keyboard attached to the message
    - `input_message_content`: `InputMessageContent` - Optional. Content of the message to be sent instead of the video animation
    """

    def __init__(self, dictionary=None):
        if dictionary is None:
            dictionary = {}
        self.dict = dictionary
        self.type = dictionary["type"] if "type" in dictionary else None
        self.id = dictionary["id"] if "id" in dictionary else None
        self.mpeg4_url = dictionary["mpeg4_url"] if "mpeg4_url" in dictionary else None
        self.mpeg4_width = dictionary["mpeg4_width"] if "mpeg4_width" in dictionary else None
        self.mpeg4_height = dictionary["mpeg4_height"] if "mpeg4_height" in dictionary else None
        self.mpeg4_duration = dictionary["mpeg4_duration"] if "mpeg4_duration" in dictionary else None
        self.thumb_url = dictionary["thumb_url"] if "thumb_url" in dictionary else None
        self.thumb_mime_type = dictionary["thumb_mime_type"] if "thumb_mime_type" in dictionary else None
        self.title = dictionary["title"] if "title" in dictionary else None
        self.caption = dictionary["caption"] if "caption" in dictionary else None
        self.parse_mode = dictionary["parse_mode"] if "parse_mode" in dictionary else None
        self.caption_entities = list(dictionary["caption_entities"]) if "caption_entities" in dictionary else None
        self.reply_markup = InlineKeyboardMarkup(dictionary["reply_markup"]) if "reply_markup" in dictionary else None
        self.input_message_content = InputMessageContent(dictionary["input_message_content"]) if "input_message_content" in dictionary else None

        for index, value in self.dict.items():
            if not hasattr(self, index):
                setattr(self, index, helper.setBvar(value))


class InlineQueryResultVideo:
    """Represents a link to a page containing an embedded video player or a video file. By default, this video file will be sent by the user with an optional caption. Alternatively, you can use input_message_content to send a message with the specified content instead of the video.[See on Telegram API](https://core.telegram.org/bots/api#inlinequeryresultvideo)

    - - - - -
    **Fields**:

    - `type`: `string` - Type of the result, must be video
    - `id`: `string` - Unique identifier for this result, 1-64 bytes
    - `video_url`: `string` - A valid URL for the embedded video player or video file
    - `mime_type`: `string` - Mime type of the content of video url, “text/html” or “video/mp4”
    - `thumb_url`: `string` - URL of the thumbnail (JPEG only) for the video
    - `title`: `string` - Title for the result
    - `caption`: `string` - Optional. Caption of the video to be sent, 0-1024 characters after entities parsing
    - `parse_mode`: `string` - Optional. Mode for parsing entities in the video caption. See formatting options for more details.
    - `caption_entities`: `list` - Optional. List of special entities that appear in the caption, which can be specified instead of parse_mode
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
        self.type = dictionary["type"] if "type" in dictionary else None
        self.id = dictionary["id"] if "id" in dictionary else None
        self.video_url = dictionary["video_url"] if "video_url" in dictionary else None
        self.mime_type = dictionary["mime_type"] if "mime_type" in dictionary else None
        self.thumb_url = dictionary["thumb_url"] if "thumb_url" in dictionary else None
        self.title = dictionary["title"] if "title" in dictionary else None
        self.caption = dictionary["caption"] if "caption" in dictionary else None
        self.parse_mode = dictionary["parse_mode"] if "parse_mode" in dictionary else None
        self.caption_entities = list(dictionary["caption_entities"]) if "caption_entities" in dictionary else None
        self.video_width = dictionary["video_width"] if "video_width" in dictionary else None
        self.video_height = dictionary["video_height"] if "video_height" in dictionary else None
        self.video_duration = dictionary["video_duration"] if "video_duration" in dictionary else None
        self.description = dictionary["description"] if "description" in dictionary else None
        self.reply_markup = InlineKeyboardMarkup(dictionary["reply_markup"]) if "reply_markup" in dictionary else None
        self.input_message_content = InputMessageContent(dictionary["input_message_content"]) if "input_message_content" in dictionary else None

        for index, value in self.dict.items():
            if not hasattr(self, index):
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
    - `caption_entities`: `list` - Optional. List of special entities that appear in the caption, which can be specified instead of parse_mode
    - `performer`: `string` - Optional. Performer
    - `audio_duration`: `int` - Optional. Audio duration in seconds
    - `reply_markup`: `InlineKeyboardMarkup` - Optional. Inline keyboard attached to the message
    - `input_message_content`: `InputMessageContent` - Optional. Content of the message to be sent instead of the audio
    """

    def __init__(self, dictionary=None):
        if dictionary is None:
            dictionary = {}
        self.dict = dictionary
        self.type = dictionary["type"] if "type" in dictionary else None
        self.id = dictionary["id"] if "id" in dictionary else None
        self.audio_url = dictionary["audio_url"] if "audio_url" in dictionary else None
        self.title = dictionary["title"] if "title" in dictionary else None
        self.caption = dictionary["caption"] if "caption" in dictionary else None
        self.parse_mode = dictionary["parse_mode"] if "parse_mode" in dictionary else None
        self.caption_entities = list(dictionary["caption_entities"]) if "caption_entities" in dictionary else None
        self.performer = dictionary["performer"] if "performer" in dictionary else None
        self.audio_duration = dictionary["audio_duration"] if "audio_duration" in dictionary else None
        self.reply_markup = InlineKeyboardMarkup(dictionary["reply_markup"]) if "reply_markup" in dictionary else None
        self.input_message_content = InputMessageContent(dictionary["input_message_content"]) if "input_message_content" in dictionary else None

        for index, value in self.dict.items():
            if not hasattr(self, index):
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
    - `caption_entities`: `list` - Optional. List of special entities that appear in the caption, which can be specified instead of parse_mode
    - `voice_duration`: `int` - Optional. Recording duration in seconds
    - `reply_markup`: `InlineKeyboardMarkup` - Optional. Inline keyboard attached to the message
    - `input_message_content`: `InputMessageContent` - Optional. Content of the message to be sent instead of the voice recording
    """

    def __init__(self, dictionary=None):
        if dictionary is None:
            dictionary = {}
        self.dict = dictionary
        self.type = dictionary["type"] if "type" in dictionary else None
        self.id = dictionary["id"] if "id" in dictionary else None
        self.voice_url = dictionary["voice_url"] if "voice_url" in dictionary else None
        self.title = dictionary["title"] if "title" in dictionary else None
        self.caption = dictionary["caption"] if "caption" in dictionary else None
        self.parse_mode = dictionary["parse_mode"] if "parse_mode" in dictionary else None
        self.caption_entities = list(dictionary["caption_entities"]) if "caption_entities" in dictionary else None
        self.voice_duration = dictionary["voice_duration"] if "voice_duration" in dictionary else None
        self.reply_markup = InlineKeyboardMarkup(dictionary["reply_markup"]) if "reply_markup" in dictionary else None
        self.input_message_content = InputMessageContent(dictionary["input_message_content"]) if "input_message_content" in dictionary else None

        for index, value in self.dict.items():
            if not hasattr(self, index):
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
    - `caption_entities`: `list` - Optional. List of special entities that appear in the caption, which can be specified instead of parse_mode
    - `document_url`: `string` - A valid URL for the file
    - `mime_type`: `string` - Mime type of the content of the file, either “application/pdf” or “application/zip”
    - `description`: `string` - Optional. Short description of the result
    - `reply_markup`: `InlineKeyboardMarkup` - Optional. Inline keyboard attached to the message
    - `input_message_content`: `InputMessageContent` - Optional. Content of the message to be sent instead of the file
    - `thumb_url`: `string` - Optional. URL of the thumbnail (JPEG only) for the file
    - `thumb_width`: `int` - Optional. Thumbnail width
    - `thumb_height`: `int` - Optional. Thumbnail height
    """

    def __init__(self, dictionary=None):
        if dictionary is None:
            dictionary = {}
        self.dict = dictionary
        self.type = dictionary["type"] if "type" in dictionary else None
        self.id = dictionary["id"] if "id" in dictionary else None
        self.title = dictionary["title"] if "title" in dictionary else None
        self.caption = dictionary["caption"] if "caption" in dictionary else None
        self.parse_mode = dictionary["parse_mode"] if "parse_mode" in dictionary else None
        self.caption_entities = list(dictionary["caption_entities"]) if "caption_entities" in dictionary else None
        self.document_url = dictionary["document_url"] if "document_url" in dictionary else None
        self.mime_type = dictionary["mime_type"] if "mime_type" in dictionary else None
        self.description = dictionary["description"] if "description" in dictionary else None
        self.reply_markup = InlineKeyboardMarkup(dictionary["reply_markup"]) if "reply_markup" in dictionary else None
        self.input_message_content = InputMessageContent(dictionary["input_message_content"]) if "input_message_content" in dictionary else None
        self.thumb_url = dictionary["thumb_url"] if "thumb_url" in dictionary else None
        self.thumb_width = dictionary["thumb_width"] if "thumb_width" in dictionary else None
        self.thumb_height = dictionary["thumb_height"] if "thumb_height" in dictionary else None

        for index, value in self.dict.items():
            if not hasattr(self, index):
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
    - `horizontal_accuracy`: `float` - Optional. The radius of uncertainty for the location, measured in meters; 0-1500
    - `live_period`: `int` - Optional. Period in seconds for which the location can be updated, should be between 60 and 86400.
    - `heading`: `int` - Optional. For live locations, a direction in which the user is moving, in degrees. Must be between 1 and 360 if specified.
    - `proximity_alert_radius`: `int` - Optional. For live locations, a maximum distance for proximity alerts about approaching another chat member, in meters. Must be between 1 and 100000 if specified.
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
        self.type = dictionary["type"] if "type" in dictionary else None
        self.id = dictionary["id"] if "id" in dictionary else None
        self.latitude = dictionary["latitude"] if "latitude" in dictionary else None
        self.longitude = dictionary["longitude"] if "longitude" in dictionary else None
        self.title = dictionary["title"] if "title" in dictionary else None
        self.horizontal_accuracy = dictionary["horizontal_accuracy"] if "horizontal_accuracy" in dictionary else None
        self.live_period = dictionary["live_period"] if "live_period" in dictionary else None
        self.heading = dictionary["heading"] if "heading" in dictionary else None
        self.proximity_alert_radius = dictionary["proximity_alert_radius"] if "proximity_alert_radius" in dictionary else None
        self.reply_markup = InlineKeyboardMarkup(dictionary["reply_markup"]) if "reply_markup" in dictionary else None
        self.input_message_content = InputMessageContent(dictionary["input_message_content"]) if "input_message_content" in dictionary else None
        self.thumb_url = dictionary["thumb_url"] if "thumb_url" in dictionary else None
        self.thumb_width = dictionary["thumb_width"] if "thumb_width" in dictionary else None
        self.thumb_height = dictionary["thumb_height"] if "thumb_height" in dictionary else None

        for index, value in self.dict.items():
            if not hasattr(self, index):
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
    - `google_place_id`: `string` - Optional. Google Places identifier of the venue
    - `google_place_type`: `string` - Optional. Google Places type of the venue. (See supported types.)
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
        self.type = dictionary["type"] if "type" in dictionary else None
        self.id = dictionary["id"] if "id" in dictionary else None
        self.latitude = dictionary["latitude"] if "latitude" in dictionary else None
        self.longitude = dictionary["longitude"] if "longitude" in dictionary else None
        self.title = dictionary["title"] if "title" in dictionary else None
        self.address = dictionary["address"] if "address" in dictionary else None
        self.foursquare_id = dictionary["foursquare_id"] if "foursquare_id" in dictionary else None
        self.foursquare_type = dictionary["foursquare_type"] if "foursquare_type" in dictionary else None
        self.google_place_id = dictionary["google_place_id"] if "google_place_id" in dictionary else None
        self.google_place_type = dictionary["google_place_type"] if "google_place_type" in dictionary else None
        self.reply_markup = InlineKeyboardMarkup(dictionary["reply_markup"]) if "reply_markup" in dictionary else None
        self.input_message_content = InputMessageContent(dictionary["input_message_content"]) if "input_message_content" in dictionary else None
        self.thumb_url = dictionary["thumb_url"] if "thumb_url" in dictionary else None
        self.thumb_width = dictionary["thumb_width"] if "thumb_width" in dictionary else None
        self.thumb_height = dictionary["thumb_height"] if "thumb_height" in dictionary else None

        for index, value in self.dict.items():
            if not hasattr(self, index):
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
        self.type = dictionary["type"] if "type" in dictionary else None
        self.id = dictionary["id"] if "id" in dictionary else None
        self.phone_number = dictionary["phone_number"] if "phone_number" in dictionary else None
        self.first_name = dictionary["first_name"] if "first_name" in dictionary else None
        self.last_name = dictionary["last_name"] if "last_name" in dictionary else None
        self.vcard = dictionary["vcard"] if "vcard" in dictionary else None
        self.reply_markup = InlineKeyboardMarkup(dictionary["reply_markup"]) if "reply_markup" in dictionary else None
        self.input_message_content = InputMessageContent(dictionary["input_message_content"]) if "input_message_content" in dictionary else None
        self.thumb_url = dictionary["thumb_url"] if "thumb_url" in dictionary else None
        self.thumb_width = dictionary["thumb_width"] if "thumb_width" in dictionary else None
        self.thumb_height = dictionary["thumb_height"] if "thumb_height" in dictionary else None

        for index, value in self.dict.items():
            if not hasattr(self, index):
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
        self.type = dictionary["type"] if "type" in dictionary else None
        self.id = dictionary["id"] if "id" in dictionary else None
        self.game_short_name = dictionary["game_short_name"] if "game_short_name" in dictionary else None
        self.reply_markup = InlineKeyboardMarkup(dictionary["reply_markup"]) if "reply_markup" in dictionary else None

        for index, value in self.dict.items():
            if not hasattr(self, index):
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
    - `caption_entities`: `list` - Optional. List of special entities that appear in the caption, which can be specified instead of parse_mode
    - `reply_markup`: `InlineKeyboardMarkup` - Optional. Inline keyboard attached to the message
    - `input_message_content`: `InputMessageContent` - Optional. Content of the message to be sent instead of the photo
    """

    def __init__(self, dictionary=None):
        if dictionary is None:
            dictionary = {}
        self.dict = dictionary
        self.type = dictionary["type"] if "type" in dictionary else None
        self.id = dictionary["id"] if "id" in dictionary else None
        self.photo_file_id = dictionary["photo_file_id"] if "photo_file_id" in dictionary else None
        self.title = dictionary["title"] if "title" in dictionary else None
        self.description = dictionary["description"] if "description" in dictionary else None
        self.caption = dictionary["caption"] if "caption" in dictionary else None
        self.parse_mode = dictionary["parse_mode"] if "parse_mode" in dictionary else None
        self.caption_entities = list(dictionary["caption_entities"]) if "caption_entities" in dictionary else None
        self.reply_markup = InlineKeyboardMarkup(dictionary["reply_markup"]) if "reply_markup" in dictionary else None
        self.input_message_content = InputMessageContent(dictionary["input_message_content"]) if "input_message_content" in dictionary else None

        for index, value in self.dict.items():
            if not hasattr(self, index):
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
    - `caption_entities`: `list` - Optional. List of special entities that appear in the caption, which can be specified instead of parse_mode
    - `reply_markup`: `InlineKeyboardMarkup` - Optional. Inline keyboard attached to the message
    - `input_message_content`: `InputMessageContent` - Optional. Content of the message to be sent instead of the GIF animation
    """

    def __init__(self, dictionary=None):
        if dictionary is None:
            dictionary = {}
        self.dict = dictionary
        self.type = dictionary["type"] if "type" in dictionary else None
        self.id = dictionary["id"] if "id" in dictionary else None
        self.gif_file_id = dictionary["gif_file_id"] if "gif_file_id" in dictionary else None
        self.title = dictionary["title"] if "title" in dictionary else None
        self.caption = dictionary["caption"] if "caption" in dictionary else None
        self.parse_mode = dictionary["parse_mode"] if "parse_mode" in dictionary else None
        self.caption_entities = list(dictionary["caption_entities"]) if "caption_entities" in dictionary else None
        self.reply_markup = InlineKeyboardMarkup(dictionary["reply_markup"]) if "reply_markup" in dictionary else None
        self.input_message_content = InputMessageContent(dictionary["input_message_content"]) if "input_message_content" in dictionary else None

        for index, value in self.dict.items():
            if not hasattr(self, index):
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
    - `caption_entities`: `list` - Optional. List of special entities that appear in the caption, which can be specified instead of parse_mode
    - `reply_markup`: `InlineKeyboardMarkup` - Optional. Inline keyboard attached to the message
    - `input_message_content`: `InputMessageContent` - Optional. Content of the message to be sent instead of the video animation
    """

    def __init__(self, dictionary=None):
        if dictionary is None:
            dictionary = {}
        self.dict = dictionary
        self.type = dictionary["type"] if "type" in dictionary else None
        self.id = dictionary["id"] if "id" in dictionary else None
        self.mpeg4_file_id = dictionary["mpeg4_file_id"] if "mpeg4_file_id" in dictionary else None
        self.title = dictionary["title"] if "title" in dictionary else None
        self.caption = dictionary["caption"] if "caption" in dictionary else None
        self.parse_mode = dictionary["parse_mode"] if "parse_mode" in dictionary else None
        self.caption_entities = list(dictionary["caption_entities"]) if "caption_entities" in dictionary else None
        self.reply_markup = InlineKeyboardMarkup(dictionary["reply_markup"]) if "reply_markup" in dictionary else None
        self.input_message_content = InputMessageContent(dictionary["input_message_content"]) if "input_message_content" in dictionary else None

        for index, value in self.dict.items():
            if not hasattr(self, index):
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
        self.type = dictionary["type"] if "type" in dictionary else None
        self.id = dictionary["id"] if "id" in dictionary else None
        self.sticker_file_id = dictionary["sticker_file_id"] if "sticker_file_id" in dictionary else None
        self.reply_markup = InlineKeyboardMarkup(dictionary["reply_markup"]) if "reply_markup" in dictionary else None
        self.input_message_content = InputMessageContent(dictionary["input_message_content"]) if "input_message_content" in dictionary else None

        for index, value in self.dict.items():
            if not hasattr(self, index):
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
    - `caption_entities`: `list` - Optional. List of special entities that appear in the caption, which can be specified instead of parse_mode
    - `reply_markup`: `InlineKeyboardMarkup` - Optional. Inline keyboard attached to the message
    - `input_message_content`: `InputMessageContent` - Optional. Content of the message to be sent instead of the file
    """

    def __init__(self, dictionary=None):
        if dictionary is None:
            dictionary = {}
        self.dict = dictionary
        self.type = dictionary["type"] if "type" in dictionary else None
        self.id = dictionary["id"] if "id" in dictionary else None
        self.title = dictionary["title"] if "title" in dictionary else None
        self.document_file_id = dictionary["document_file_id"] if "document_file_id" in dictionary else None
        self.description = dictionary["description"] if "description" in dictionary else None
        self.caption = dictionary["caption"] if "caption" in dictionary else None
        self.parse_mode = dictionary["parse_mode"] if "parse_mode" in dictionary else None
        self.caption_entities = list(dictionary["caption_entities"]) if "caption_entities" in dictionary else None
        self.reply_markup = InlineKeyboardMarkup(dictionary["reply_markup"]) if "reply_markup" in dictionary else None
        self.input_message_content = InputMessageContent(dictionary["input_message_content"]) if "input_message_content" in dictionary else None

        for index, value in self.dict.items():
            if not hasattr(self, index):
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
    - `caption_entities`: `list` - Optional. List of special entities that appear in the caption, which can be specified instead of parse_mode
    - `reply_markup`: `InlineKeyboardMarkup` - Optional. Inline keyboard attached to the message
    - `input_message_content`: `InputMessageContent` - Optional. Content of the message to be sent instead of the video
    """

    def __init__(self, dictionary=None):
        if dictionary is None:
            dictionary = {}
        self.dict = dictionary
        self.type = dictionary["type"] if "type" in dictionary else None
        self.id = dictionary["id"] if "id" in dictionary else None
        self.video_file_id = dictionary["video_file_id"] if "video_file_id" in dictionary else None
        self.title = dictionary["title"] if "title" in dictionary else None
        self.description = dictionary["description"] if "description" in dictionary else None
        self.caption = dictionary["caption"] if "caption" in dictionary else None
        self.parse_mode = dictionary["parse_mode"] if "parse_mode" in dictionary else None
        self.caption_entities = list(dictionary["caption_entities"]) if "caption_entities" in dictionary else None
        self.reply_markup = InlineKeyboardMarkup(dictionary["reply_markup"]) if "reply_markup" in dictionary else None
        self.input_message_content = InputMessageContent(dictionary["input_message_content"]) if "input_message_content" in dictionary else None

        for index, value in self.dict.items():
            if not hasattr(self, index):
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
    - `caption_entities`: `list` - Optional. List of special entities that appear in the caption, which can be specified instead of parse_mode
    - `reply_markup`: `InlineKeyboardMarkup` - Optional. Inline keyboard attached to the message
    - `input_message_content`: `InputMessageContent` - Optional. Content of the message to be sent instead of the voice message
    """

    def __init__(self, dictionary=None):
        if dictionary is None:
            dictionary = {}
        self.dict = dictionary
        self.type = dictionary["type"] if "type" in dictionary else None
        self.id = dictionary["id"] if "id" in dictionary else None
        self.voice_file_id = dictionary["voice_file_id"] if "voice_file_id" in dictionary else None
        self.title = dictionary["title"] if "title" in dictionary else None
        self.caption = dictionary["caption"] if "caption" in dictionary else None
        self.parse_mode = dictionary["parse_mode"] if "parse_mode" in dictionary else None
        self.caption_entities = list(dictionary["caption_entities"]) if "caption_entities" in dictionary else None
        self.reply_markup = InlineKeyboardMarkup(dictionary["reply_markup"]) if "reply_markup" in dictionary else None
        self.input_message_content = InputMessageContent(dictionary["input_message_content"]) if "input_message_content" in dictionary else None

        for index, value in self.dict.items():
            if not hasattr(self, index):
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
    - `caption_entities`: `list` - Optional. List of special entities that appear in the caption, which can be specified instead of parse_mode
    - `reply_markup`: `InlineKeyboardMarkup` - Optional. Inline keyboard attached to the message
    - `input_message_content`: `InputMessageContent` - Optional. Content of the message to be sent instead of the audio
    """

    def __init__(self, dictionary=None):
        if dictionary is None:
            dictionary = {}
        self.dict = dictionary
        self.type = dictionary["type"] if "type" in dictionary else None
        self.id = dictionary["id"] if "id" in dictionary else None
        self.audio_file_id = dictionary["audio_file_id"] if "audio_file_id" in dictionary else None
        self.caption = dictionary["caption"] if "caption" in dictionary else None
        self.parse_mode = dictionary["parse_mode"] if "parse_mode" in dictionary else None
        self.caption_entities = list(dictionary["caption_entities"]) if "caption_entities" in dictionary else None
        self.reply_markup = InlineKeyboardMarkup(dictionary["reply_markup"]) if "reply_markup" in dictionary else None
        self.input_message_content = InputMessageContent(dictionary["input_message_content"]) if "input_message_content" in dictionary else None

        for index, value in self.dict.items():
            if not hasattr(self, index):
                setattr(self, index, helper.setBvar(value))


class InputMessageContent:
    """This object represents the content of a message to be sent as a result of an inline query. Telegram clients currently support the following 5 types:[See on Telegram API](https://core.telegram.org/bots/api#inputmessagecontent)

    - - - - -
    **Fields**:

    """

    def __init__(self, dictionary=None):
        if dictionary is None:
            dictionary = {}
        self.dict = dictionary

        for index, value in self.dict.items():
            if not hasattr(self, index):
                setattr(self, index, helper.setBvar(value))


class InputTextMessageContent:
    """Represents the content of a text message to be sent as the result of an inline query.[See on Telegram API](https://core.telegram.org/bots/api#inputtextmessagecontent)

    - - - - -
    **Fields**:

    - `message_text`: `string` - Text of the message to be sent, 1-4096 characters
    - `parse_mode`: `string` - Optional. Mode for parsing entities in the message text. See formatting options for more details.
    - `entities`: `list` - Optional. List of special entities that appear in message text, which can be specified instead of parse_mode
    - `disable_web_page_preview`: `bool` - Optional. Disables link previews for links in the sent message
    """

    def __init__(self, dictionary=None):
        if dictionary is None:
            dictionary = {}
        self.dict = dictionary
        self.message_text = dictionary["message_text"] if "message_text" in dictionary else None
        self.parse_mode = dictionary["parse_mode"] if "parse_mode" in dictionary else None
        self.entities = list(dictionary["entities"]) if "entities" in dictionary else None
        self.disable_web_page_preview = dictionary["disable_web_page_preview"] if "disable_web_page_preview" in dictionary else None

        for index, value in self.dict.items():
            if not hasattr(self, index):
                setattr(self, index, helper.setBvar(value))


class InputLocationMessageContent:
    """Represents the content of a location message to be sent as the result of an inline query.[See on Telegram API](https://core.telegram.org/bots/api#inputlocationmessagecontent)

    - - - - -
    **Fields**:

    - `latitude`: `float` - Latitude of the location in degrees
    - `longitude`: `float` - Longitude of the location in degrees
    - `horizontal_accuracy`: `float` - Optional. The radius of uncertainty for the location, measured in meters; 0-1500
    - `live_period`: `int` - Optional. Period in seconds for which the location can be updated, should be between 60 and 86400.
    - `heading`: `int` - Optional. For live locations, a direction in which the user is moving, in degrees. Must be between 1 and 360 if specified.
    - `proximity_alert_radius`: `int` - Optional. For live locations, a maximum distance for proximity alerts about approaching another chat member, in meters. Must be between 1 and 100000 if specified.
    """

    def __init__(self, dictionary=None):
        if dictionary is None:
            dictionary = {}
        self.dict = dictionary
        self.latitude = dictionary["latitude"] if "latitude" in dictionary else None
        self.longitude = dictionary["longitude"] if "longitude" in dictionary else None
        self.horizontal_accuracy = dictionary["horizontal_accuracy"] if "horizontal_accuracy" in dictionary else None
        self.live_period = dictionary["live_period"] if "live_period" in dictionary else None
        self.heading = dictionary["heading"] if "heading" in dictionary else None
        self.proximity_alert_radius = dictionary["proximity_alert_radius"] if "proximity_alert_radius" in dictionary else None

        for index, value in self.dict.items():
            if not hasattr(self, index):
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
    - `google_place_id`: `string` - Optional. Google Places identifier of the venue
    - `google_place_type`: `string` - Optional. Google Places type of the venue. (See supported types.)
    """

    def __init__(self, dictionary=None):
        if dictionary is None:
            dictionary = {}
        self.dict = dictionary
        self.latitude = dictionary["latitude"] if "latitude" in dictionary else None
        self.longitude = dictionary["longitude"] if "longitude" in dictionary else None
        self.title = dictionary["title"] if "title" in dictionary else None
        self.address = dictionary["address"] if "address" in dictionary else None
        self.foursquare_id = dictionary["foursquare_id"] if "foursquare_id" in dictionary else None
        self.foursquare_type = dictionary["foursquare_type"] if "foursquare_type" in dictionary else None
        self.google_place_id = dictionary["google_place_id"] if "google_place_id" in dictionary else None
        self.google_place_type = dictionary["google_place_type"] if "google_place_type" in dictionary else None

        for index, value in self.dict.items():
            if not hasattr(self, index):
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
        self.phone_number = dictionary["phone_number"] if "phone_number" in dictionary else None
        self.first_name = dictionary["first_name"] if "first_name" in dictionary else None
        self.last_name = dictionary["last_name"] if "last_name" in dictionary else None
        self.vcard = dictionary["vcard"] if "vcard" in dictionary else None

        for index, value in self.dict.items():
            if not hasattr(self, index):
                setattr(self, index, helper.setBvar(value))


class InputInvoiceMessageContent:
    """Represents the content of an invoice message to be sent as the result of an inline query.[See on Telegram API](https://core.telegram.org/bots/api#inputinvoicemessagecontent)

    - - - - -
    **Fields**:

    - `title`: `string` - Product name, 1-32 characters
    - `description`: `string` - Product description, 1-255 characters
    - `payload`: `string` - Bot-defined invoice payload, 1-128 bytes. This will not be displayed to the user, use for your internal processes.
    - `provider_token`: `string` - Payment provider token, obtained via Botfather
    - `currency`: `string` - Three-letter ISO 4217 currency code, see more on currencies
    - `prices`: `list` - Price breakdown, a JSON-serialized list of components (e.g. product price, tax, discount, delivery cost, delivery tax, bonus, etc.)
    - `max_tip_amount`: `int` - Optional. The maximum accepted amount for tips in the smallest units of the currency (integer, not float/double). For example, for a maximum tip of US$ 1.45 pass max_tip_amount = 145. See the exp parameter in currencies.json, it shows the number of digits past the decimal point for each currency (2 for the majority of currencies). Defaults to 0
    - `suggested_tip_amounts`: `list` - Optional. A JSON-serialized array of suggested amounts of tip in the smallest units of the currency (integer, not float/double). At most 4 suggested tip amounts can be specified. The suggested tip amounts must be positive, passed in a strictly increased order and must not exceed max_tip_amount.
    - `provider_data`: `string` - Optional. A JSON-serialized object for data about the invoice, which will be shared with the payment provider. A detailed description of the required fields should be provided by the payment provider.
    - `photo_url`: `string` - Optional. URL of the product photo for the invoice. Can be a photo of the goods or a marketing image for a service. People like it better when they see what they are paying for.
    - `photo_size`: `int` - Optional. Photo size
    - `photo_width`: `int` - Optional. Photo width
    - `photo_height`: `int` - Optional. Photo height
    - `need_name`: `bool` - Optional. Pass True, if you require the user's full name to complete the order
    - `need_phone_number`: `bool` - Optional. Pass True, if you require the user's phone number to complete the order
    - `need_email`: `bool` - Optional. Pass True, if you require the user's email address to complete the order
    - `need_shipping_address`: `bool` - Optional. Pass True, if you require the user's shipping address to complete the order
    - `send_phone_number_to_provider`: `bool` - Optional. Pass True, if user's phone number should be sent to provider
    - `send_email_to_provider`: `bool` - Optional. Pass True, if user's email address should be sent to provider
    - `is_flexible`: `bool` - Optional. Pass True, if the final price depends on the shipping method
    """

    def __init__(self, dictionary=None):
        if dictionary is None:
            dictionary = {}
        self.dict = dictionary
        self.title = dictionary["title"] if "title" in dictionary else None
        self.description = dictionary["description"] if "description" in dictionary else None
        self.payload = dictionary["payload"] if "payload" in dictionary else None
        self.provider_token = dictionary["provider_token"] if "provider_token" in dictionary else None
        self.currency = dictionary["currency"] if "currency" in dictionary else None
        self.prices = list(dictionary["prices"]) if "prices" in dictionary else None
        self.max_tip_amount = dictionary["max_tip_amount"] if "max_tip_amount" in dictionary else None
        self.suggested_tip_amounts = list(dictionary["suggested_tip_amounts"]) if "suggested_tip_amounts" in dictionary else None
        self.provider_data = dictionary["provider_data"] if "provider_data" in dictionary else None
        self.photo_url = dictionary["photo_url"] if "photo_url" in dictionary else None
        self.photo_size = dictionary["photo_size"] if "photo_size" in dictionary else None
        self.photo_width = dictionary["photo_width"] if "photo_width" in dictionary else None
        self.photo_height = dictionary["photo_height"] if "photo_height" in dictionary else None
        self.need_name = dictionary["need_name"] if "need_name" in dictionary else None
        self.need_phone_number = dictionary["need_phone_number"] if "need_phone_number" in dictionary else None
        self.need_email = dictionary["need_email"] if "need_email" in dictionary else None
        self.need_shipping_address = dictionary["need_shipping_address"] if "need_shipping_address" in dictionary else None
        self.send_phone_number_to_provider = dictionary["send_phone_number_to_provider"] if "send_phone_number_to_provider" in dictionary else None
        self.send_email_to_provider = dictionary["send_email_to_provider"] if "send_email_to_provider" in dictionary else None
        self.is_flexible = dictionary["is_flexible"] if "is_flexible" in dictionary else None

        for index, value in self.dict.items():
            if not hasattr(self, index):
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
        self.result_id = dictionary["result_id"] if "result_id" in dictionary else None
        self.user = User(dictionary["from"]) if "from" in dictionary else None
        self.location = Location(dictionary["location"]) if "location" in dictionary else None
        self.inline_message_id = dictionary["inline_message_id"] if "inline_message_id" in dictionary else None
        self.query = dictionary["query"] if "query" in dictionary else None

        for index, value in self.dict.items():
            if not hasattr(self, index):
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
        self.label = dictionary["label"] if "label" in dictionary else None
        self.amount = dictionary["amount"] if "amount" in dictionary else None

        for index, value in self.dict.items():
            if not hasattr(self, index):
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
        self.title = dictionary["title"] if "title" in dictionary else None
        self.description = dictionary["description"] if "description" in dictionary else None
        self.start_parameter = dictionary["start_parameter"] if "start_parameter" in dictionary else None
        self.currency = dictionary["currency"] if "currency" in dictionary else None
        self.total_amount = dictionary["total_amount"] if "total_amount" in dictionary else None

        for index, value in self.dict.items():
            if not hasattr(self, index):
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
        self.country_code = dictionary["country_code"] if "country_code" in dictionary else None
        self.state = dictionary["state"] if "state" in dictionary else None
        self.city = dictionary["city"] if "city" in dictionary else None
        self.street_line1 = dictionary["street_line1"] if "street_line1" in dictionary else None
        self.street_line2 = dictionary["street_line2"] if "street_line2" in dictionary else None
        self.post_code = dictionary["post_code"] if "post_code" in dictionary else None

        for index, value in self.dict.items():
            if not hasattr(self, index):
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
        self.name = dictionary["name"] if "name" in dictionary else None
        self.phone_number = dictionary["phone_number"] if "phone_number" in dictionary else None
        self.email = dictionary["email"] if "email" in dictionary else None
        self.shipping_address = ShippingAddress(dictionary["shipping_address"]) if "shipping_address" in dictionary else None

        for index, value in self.dict.items():
            if not hasattr(self, index):
                setattr(self, index, helper.setBvar(value))


class ShippingOption:
    """This object represents one shipping option.[See on Telegram API](https://core.telegram.org/bots/api#shippingoption)

    - - - - -
    **Fields**:

    - `id`: `string` - Shipping option identifier
    - `title`: `string` - Option title
    - `prices`: `list` - List of price portions
    """

    def __init__(self, dictionary=None):
        if dictionary is None:
            dictionary = {}
        self.dict = dictionary
        self.id = dictionary["id"] if "id" in dictionary else None
        self.title = dictionary["title"] if "title" in dictionary else None
        self.prices = list(dictionary["prices"]) if "prices" in dictionary else None

        for index, value in self.dict.items():
            if not hasattr(self, index):
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
        self.currency = dictionary["currency"] if "currency" in dictionary else None
        self.total_amount = dictionary["total_amount"] if "total_amount" in dictionary else None
        self.invoice_payload = dictionary["invoice_payload"] if "invoice_payload" in dictionary else None
        self.shipping_option_id = dictionary["shipping_option_id"] if "shipping_option_id" in dictionary else None
        self.order_info = OrderInfo(dictionary["order_info"]) if "order_info" in dictionary else None
        self.telegram_payment_charge_id = dictionary["telegram_payment_charge_id"] if "telegram_payment_charge_id" in dictionary else None
        self.provider_payment_charge_id = dictionary["provider_payment_charge_id"] if "provider_payment_charge_id" in dictionary else None

        for index, value in self.dict.items():
            if not hasattr(self, index):
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
        self.id = dictionary["id"] if "id" in dictionary else None
        self.user = User(dictionary["from"]) if "from" in dictionary else None
        self.invoice_payload = dictionary["invoice_payload"] if "invoice_payload" in dictionary else None
        self.shipping_address = ShippingAddress(dictionary["shipping_address"]) if "shipping_address" in dictionary else None

        for index, value in self.dict.items():
            if not hasattr(self, index):
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
        self.id = dictionary["id"] if "id" in dictionary else None
        self.user = User(dictionary["from"]) if "from" in dictionary else None
        self.currency = dictionary["currency"] if "currency" in dictionary else None
        self.total_amount = dictionary["total_amount"] if "total_amount" in dictionary else None
        self.invoice_payload = dictionary["invoice_payload"] if "invoice_payload" in dictionary else None
        self.shipping_option_id = dictionary["shipping_option_id"] if "shipping_option_id" in dictionary else None
        self.order_info = OrderInfo(dictionary["order_info"]) if "order_info" in dictionary else None

        for index, value in self.dict.items():
            if not hasattr(self, index):
                setattr(self, index, helper.setBvar(value))


class PassportData:
    """Contains information about Telegram Passport data shared with the bot by the user.[See on Telegram API](https://core.telegram.org/bots/api#passportdata)

    - - - - -
    **Fields**:

    - `data`: `list` - Array with information about documents and other Telegram Passport elements that was shared with the bot
    - `credentials`: `EncryptedCredentials` - Encrypted credentials required to decrypt the data
    """

    def __init__(self, dictionary=None):
        if dictionary is None:
            dictionary = {}
        self.dict = dictionary
        self.data = list(dictionary["data"]) if "data" in dictionary else None
        self.credentials = EncryptedCredentials(dictionary["credentials"]) if "credentials" in dictionary else None

        for index, value in self.dict.items():
            if not hasattr(self, index):
                setattr(self, index, helper.setBvar(value))


class PassportFile:
    """This object represents a file uploaded to Telegram Passport. Currently all Telegram Passport files are in JPEG format when decrypted and don't exceed 10MB.[See on Telegram API](https://core.telegram.org/bots/api#passportfile)

    - - - - -
    **Fields**:

    - `file_id`: `string` - Identifier for this file, which can be used to download or reuse the file
    - `file_unique_id`: `string` - Unique identifier for this file, which is supposed to be the same over time and for different bots. Can't be used to download or reuse the file.
    - `file_size`: `int` - File size in bytes
    - `file_date`: `int` - Unix time when the file was uploaded
    """

    def __init__(self, dictionary=None):
        if dictionary is None:
            dictionary = {}
        self.dict = dictionary
        self.file_id = dictionary["file_id"] if "file_id" in dictionary else None
        self.file_unique_id = dictionary["file_unique_id"] if "file_unique_id" in dictionary else None
        self.file_size = dictionary["file_size"] if "file_size" in dictionary else None
        self.file_date = dictionary["file_date"] if "file_date" in dictionary else None

        for index, value in self.dict.items():
            if not hasattr(self, index):
                setattr(self, index, helper.setBvar(value))


class EncryptedPassportElement:
    """Contains information about documents or other Telegram Passport elements shared with the bot by the user.[See on Telegram API](https://core.telegram.org/bots/api#encryptedpassportelement)

    - - - - -
    **Fields**:

    - `type`: `string` - Element type. One of “personal_details”, “passport”, “driver_license”, “identity_card”, “internal_passport”, “address”, “utility_bill”, “bank_statement”, “rental_agreement”, “passport_registration”, “temporary_registration”, “phone_number”, “email”.
    - `data`: `string` - Optional. Base64-encoded encrypted Telegram Passport element data provided by the user, available for “personal_details”, “passport”, “driver_license”, “identity_card”, “internal_passport” and “address” types. Can be decrypted and verified using the accompanying EncryptedCredentials.
    - `phone_number`: `string` - Optional. User's verified phone number, available only for “phone_number” type
    - `email`: `string` - Optional. User's verified email address, available only for “email” type
    - `files`: `list` - Optional. Array of encrypted files with documents provided by the user, available for “utility_bill”, “bank_statement”, “rental_agreement”, “passport_registration” and “temporary_registration” types. Files can be decrypted and verified using the accompanying EncryptedCredentials.
    - `front_side`: `PassportFile` - Optional. Encrypted file with the front side of the document, provided by the user. Available for “passport”, “driver_license”, “identity_card” and “internal_passport”. The file can be decrypted and verified using the accompanying EncryptedCredentials.
    - `reverse_side`: `PassportFile` - Optional. Encrypted file with the reverse side of the document, provided by the user. Available for “driver_license” and “identity_card”. The file can be decrypted and verified using the accompanying EncryptedCredentials.
    - `selfie`: `PassportFile` - Optional. Encrypted file with the selfie of the user holding a document, provided by the user; available for “passport”, “driver_license”, “identity_card” and “internal_passport”. The file can be decrypted and verified using the accompanying EncryptedCredentials.
    - `translation`: `list` - Optional. Array of encrypted files with translated versions of documents provided by the user. Available if requested for “passport”, “driver_license”, “identity_card”, “internal_passport”, “utility_bill”, “bank_statement”, “rental_agreement”, “passport_registration” and “temporary_registration” types. Files can be decrypted and verified using the accompanying EncryptedCredentials.
    - `hash`: `string` - Base64-encoded element hash for using in PassportElementErrorUnspecified
    """

    def __init__(self, dictionary=None):
        if dictionary is None:
            dictionary = {}
        self.dict = dictionary
        self.type = dictionary["type"] if "type" in dictionary else None
        self.data = dictionary["data"] if "data" in dictionary else None
        self.phone_number = dictionary["phone_number"] if "phone_number" in dictionary else None
        self.email = dictionary["email"] if "email" in dictionary else None
        self.files = list(dictionary["files"]) if "files" in dictionary else None
        self.front_side = PassportFile(dictionary["front_side"]) if "front_side" in dictionary else None
        self.reverse_side = PassportFile(dictionary["reverse_side"]) if "reverse_side" in dictionary else None
        self.selfie = PassportFile(dictionary["selfie"]) if "selfie" in dictionary else None
        self.translation = list(dictionary["translation"]) if "translation" in dictionary else None
        self.hash = dictionary["hash"] if "hash" in dictionary else None

        for index, value in self.dict.items():
            if not hasattr(self, index):
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
        self.data = dictionary["data"] if "data" in dictionary else None
        self.hash = dictionary["hash"] if "hash" in dictionary else None
        self.secret = dictionary["secret"] if "secret" in dictionary else None

        for index, value in self.dict.items():
            if not hasattr(self, index):
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
            if not hasattr(self, index):
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
        self.source = dictionary["source"] if "source" in dictionary else None
        self.type = dictionary["type"] if "type" in dictionary else None
        self.field_name = dictionary["field_name"] if "field_name" in dictionary else None
        self.data_hash = dictionary["data_hash"] if "data_hash" in dictionary else None
        self.message = dictionary["message"] if "message" in dictionary else None

        for index, value in self.dict.items():
            if not hasattr(self, index):
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
        self.source = dictionary["source"] if "source" in dictionary else None
        self.type = dictionary["type"] if "type" in dictionary else None
        self.file_hash = dictionary["file_hash"] if "file_hash" in dictionary else None
        self.message = dictionary["message"] if "message" in dictionary else None

        for index, value in self.dict.items():
            if not hasattr(self, index):
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
        self.source = dictionary["source"] if "source" in dictionary else None
        self.type = dictionary["type"] if "type" in dictionary else None
        self.file_hash = dictionary["file_hash"] if "file_hash" in dictionary else None
        self.message = dictionary["message"] if "message" in dictionary else None

        for index, value in self.dict.items():
            if not hasattr(self, index):
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
        self.source = dictionary["source"] if "source" in dictionary else None
        self.type = dictionary["type"] if "type" in dictionary else None
        self.file_hash = dictionary["file_hash"] if "file_hash" in dictionary else None
        self.message = dictionary["message"] if "message" in dictionary else None

        for index, value in self.dict.items():
            if not hasattr(self, index):
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
        self.source = dictionary["source"] if "source" in dictionary else None
        self.type = dictionary["type"] if "type" in dictionary else None
        self.file_hash = dictionary["file_hash"] if "file_hash" in dictionary else None
        self.message = dictionary["message"] if "message" in dictionary else None

        for index, value in self.dict.items():
            if not hasattr(self, index):
                setattr(self, index, helper.setBvar(value))


class PassportElementErrorFiles:
    """Represents an issue with a list of scans. The error is considered resolved when the list of files containing the scans changes.[See on Telegram API](https://core.telegram.org/bots/api#passportelementerrorfiles)

    - - - - -
    **Fields**:

    - `source`: `string` - Error source, must be files
    - `type`: `string` - The section of the user's Telegram Passport which has the issue, one of “utility_bill”, “bank_statement”, “rental_agreement”, “passport_registration”, “temporary_registration”
    - `file_hashes`: `list` - List of base64-encoded file hashes
    - `message`: `string` - Error message
    """

    def __init__(self, dictionary=None):
        if dictionary is None:
            dictionary = {}
        self.dict = dictionary
        self.source = dictionary["source"] if "source" in dictionary else None
        self.type = dictionary["type"] if "type" in dictionary else None
        self.file_hashes = list(dictionary["file_hashes"]) if "file_hashes" in dictionary else None
        self.message = dictionary["message"] if "message" in dictionary else None

        for index, value in self.dict.items():
            if not hasattr(self, index):
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
        self.source = dictionary["source"] if "source" in dictionary else None
        self.type = dictionary["type"] if "type" in dictionary else None
        self.file_hash = dictionary["file_hash"] if "file_hash" in dictionary else None
        self.message = dictionary["message"] if "message" in dictionary else None

        for index, value in self.dict.items():
            if not hasattr(self, index):
                setattr(self, index, helper.setBvar(value))


class PassportElementErrorTranslationFiles:
    """Represents an issue with the translated version of a document. The error is considered resolved when a file with the document translation change.[See on Telegram API](https://core.telegram.org/bots/api#passportelementerrortranslationfiles)

    - - - - -
    **Fields**:

    - `source`: `string` - Error source, must be translation_files
    - `type`: `string` - Type of element of the user's Telegram Passport which has the issue, one of “passport”, “driver_license”, “identity_card”, “internal_passport”, “utility_bill”, “bank_statement”, “rental_agreement”, “passport_registration”, “temporary_registration”
    - `file_hashes`: `list` - List of base64-encoded file hashes
    - `message`: `string` - Error message
    """

    def __init__(self, dictionary=None):
        if dictionary is None:
            dictionary = {}
        self.dict = dictionary
        self.source = dictionary["source"] if "source" in dictionary else None
        self.type = dictionary["type"] if "type" in dictionary else None
        self.file_hashes = list(dictionary["file_hashes"]) if "file_hashes" in dictionary else None
        self.message = dictionary["message"] if "message" in dictionary else None

        for index, value in self.dict.items():
            if not hasattr(self, index):
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
        self.source = dictionary["source"] if "source" in dictionary else None
        self.type = dictionary["type"] if "type" in dictionary else None
        self.element_hash = dictionary["element_hash"] if "element_hash" in dictionary else None
        self.message = dictionary["message"] if "message" in dictionary else None

        for index, value in self.dict.items():
            if not hasattr(self, index):
                setattr(self, index, helper.setBvar(value))


class Game:
    """This object represents a game. Use BotFather to create and edit games, their short names will act as unique identifiers.[See on Telegram API](https://core.telegram.org/bots/api#game)

    - - - - -
    **Fields**:

    - `title`: `string` - Title of the game
    - `description`: `string` - Description of the game
    - `photo`: `list` - Photo that will be displayed in the game message in chats.
    - `text`: `string` - Optional. Brief description of the game or high scores included in the game message. Can be automatically edited to include current high scores for the game when the bot calls setGameScore, or manually edited using editMessageText. 0-4096 characters.
    - `text_entities`: `list` - Optional. Special entities that appear in text, such as usernames, URLs, bot commands, etc.
    - `animation`: `Animation` - Optional. Animation that will be displayed in the game message in chats. Upload via BotFather
    """

    def __init__(self, dictionary=None):
        if dictionary is None:
            dictionary = {}
        self.dict = dictionary
        self.title = dictionary["title"] if "title" in dictionary else None
        self.description = dictionary["description"] if "description" in dictionary else None
        self.photo = list(dictionary["photo"]) if "photo" in dictionary else None
        self.text = dictionary["text"] if "text" in dictionary else None
        self.text_entities = list(dictionary["text_entities"]) if "text_entities" in dictionary else None
        self.animation = Animation(dictionary["animation"]) if "animation" in dictionary else None

        for index, value in self.dict.items():
            if not hasattr(self, index):
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
            if not hasattr(self, index):
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
        self.position = dictionary["position"] if "position" in dictionary else None
        self.user = User(dictionary["from"]) if "from" in dictionary else None
        self.score = dictionary["score"] if "score" in dictionary else None

        for index, value in self.dict.items():
            if not hasattr(self, index):
                setattr(self, index, helper.setBvar(value))


