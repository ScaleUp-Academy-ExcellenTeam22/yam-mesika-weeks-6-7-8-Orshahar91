class PostOffice:
    """A Post Office class. Allows users to message each other and read their messages.

    :ivar int message_id: Incremental id of the last message sent.
    :ivar dict boxes: Users' inboxes.

    :param list usernames: Users for which we should create PO Boxes.
    """

    def __init__(self, usernames):
        self.message_id = 0
        self.boxes = {user: [] for user in usernames}

    def send_message(self, sender, recipient, message_body, urgent=False):
        """Send a message to a recipient.

        :param str sender: The message sender's username.
        :param str recipient: The message recipient's username.
        :param str message_body: The body of the message.
        :param urgent: The urgency of the message.
        :type urgent: bool, optional
        :return: The message ID, auto incremented number.
        :rtype: int
        :raises KeyError: if the recipient does not exist.
        """
        user_box = self.boxes[recipient]
        self.message_id = self.message_id + 1
        message_details = {
            'id': self.message_id,
            'body': message_body,
            'sender': sender,
            'marked as': "Unread",
        }

        if urgent:
            user_box.insert(0, message_details)
        else:
            user_box.append(message_details)
        return self.message_id

    def read_inbox(self, username, num_of_messages=-1):
        """

        :param str username: The username of the person's inbox.
        :param int num_of_messages: Number of messages to read.
        :return: The user's unread messages
        """
        user_box = self.boxes[username]
        user_inbox_messages = []
        if num_of_messages != -1:
            for message in user_box[:num_of_messages]:
                if message["marked as"] == "Unread":
                    user_inbox_messages.append(message)
                    message["marked as"] = "Read"
            return user_inbox_messages
        else:
            for message in user_box:
                message["marked as"] = "Read"
            return user_box

    def search_inbox(self, username, query):
        """

        :param str username: The username of the person's inbox.
        :param str query: The string that need to be found in the messages.
        :return: The messages that contain the provided query.
        """
        user_box = self.boxes[username]
        message_with_query = []
        for message in user_box:
            if query in message["body"]:
                message_with_query.append(message)
        return message_with_query
