from termcolor import colored
from dataclasses import dataclass


class PostOffice:
    """A Post Office class. Allows users to message each other and read their messages.

    :ivar int message_id: Incremental id of the last message sent.
    :ivar dict boxes: Users' inboxes.

    :param list usernames: Users for which we should create PO Boxes.
    """

    def __init__(self, usernames: set[str]):
        self.message_id = 0
        self.boxes: dict[str, list[str]] = {user: [] for user in usernames}

    def send_message(self, message) -> int:
        """
        Send a message to a recipient.
        :param message: instance of Message.
        :return: Message id.
        """
        user_box = self.boxes[message.recipient]
        self.message_id = self.message_id + 1
        user_box.insert(0, message) if message.urgent else user_box.append(message)
        return self.message_id

    def read_inbox(self, username, num_of_messages=-1) -> list["Message"]:
        """
        Read the inbox of specific user.
        :param str username: The username of the person's inbox.
        :param int num_of_messages: Number of messages to read.
        :return: The user's unread messages.
        """
        user_box = self.boxes[username]
        num_of_messages = len(user_box) if num_of_messages == -1 else num_of_messages
        unread_messages = [message for message in user_box[:num_of_messages] if not message.read]

        for message in unread_messages:
            message.read = True

        return unread_messages

    def search_inbox(self, username: str, query: str) -> list["Message"]:
        """
        :param str username: The username of the person's inbox.
        :param str query: The string that need to be found in the messages.
        :return: The messages that contain the provided query.
        """
        user_box: list["Message"] = self.boxes[username]
        message_with_query = [message for message in user_box
                              if query in message.message_body or query in message.message_title]
        return message_with_query


@dataclass
class Message:
    """A Message class, to keep the message information."""
    sender: str
    recipient: str
    message_title: str
    message_body: str
    urgent: bool = False
    read: bool = False

    def __len__(self):
        """
        :return: Length of the message body.
        """
        return len(self.message_body)

    def __str__(self):
        """
        :return: String of the Message class containing the params.
        """
        boundary = "\n######################\n"
        message = boundary + "Message: " + self.message_title + "\nSender: " + self.sender + "\nRecipient: " + \
            self.recipient + "\nBody: " + self.message_body + boundary
        return message if not self.urgent else colored(message, 'red')


def show_example():
    """Show example of using the PostOffice class and Message class."""
    users = {"Newman", "Jerry"}
    post_office = PostOffice(users)
    message_for_newman = Message("Jerry", "Newman", "Postman", "Hello Newman", True)
    message_for_jerry = Message("Newman", "Jerry", "Seinfeld", "Hello Jerry")
    post_office.send_message(message_for_newman)
    post_office.send_message(message_for_jerry)
    message = post_office.read_inbox("Newman")
    print(*message)
    message = post_office.read_inbox("Jerry")
    print(*message)
    search = post_office.search_inbox("Newman", "Hello")
    print(*search)


if __name__ == "__main__":
    show_example()
