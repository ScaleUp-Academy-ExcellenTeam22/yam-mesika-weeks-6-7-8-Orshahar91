from termcolor import colored


class PostOffice:
    """A Post Office class. Allows users to message each other and read their messages.

    :ivar int message_id: Incremental id of the last message sent.
    :ivar dict boxes: Users' inboxes.

    :param list usernames: Users for which we should create PO Boxes.
    """

    def __init__(self, usernames):
        self.message_id = 0
        self.boxes = {user: [] for user in usernames}

    def send_message(self, message):
        """
        Send a message to a recipient.
        :param message: instance of Message class
        :return: message id
        """
        user_box = self.boxes[message.recipient]
        self.message_id = self.message_id + 1
        if message.urgent:
            user_box.insert(0, message)
        else:
            user_box.append(message)
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
                if not message.read:
                    user_inbox_messages.append(message)
                    message.read = True
            return user_inbox_messages
        else:
            for message in user_box:
                message.read = True
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
            if query in (message.message_body or message.title):
                message_with_query.append(message)
        return message_with_query


class Message:
    """A Message class. Holds the message information.
    """

    def __init__(self, sender, recipient, message_title, message_body, urgent=False, read=False):
        """
        :param sender: Sender's username
        :param recipient: Recipient username
        :param message_title: Message title
        :param message_body: Message body
        :param urgent: Flag for urgent message
        :param read: Flag for read/unread
        """
        self.sender = sender
        self.recipient = recipient
        self.message_title = message_title
        self.message_body = message_body
        self.urgent = urgent
        self.read = read

    def __len__(self):
        """
        :return: Length of the message body
        """
        return len(self.message_body)

    def __str__(self):
        """
        :return: String of the Message class containing the params.
        """
        message = "Message: " + self.message_title + "\nSender: " + self.sender + "\nRecipient: " + self.recipient + \
                  "\nBody: " + self.message_body
        return message if not self.urgent else colored(message, 'red')


def show_example():
    """Show example of using the PostOffice class and Message class."""
    users = ('Newman', 'Mr. Peanutbutter')
    PostOffice(users)
    msg = Message("Mr. Peanutbutter", "Newman", "New Title", "New Body")
    print(msg)


show_example()
