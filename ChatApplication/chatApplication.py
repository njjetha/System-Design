class User:
    def __init__(self, username):
        self.username=username
        self.contacts=[]

    def add_contact(self, user):
        self.contacts.append(user)
    
    def __repr__(self):
        return self.username
    
class Message:
    def __init__(self, sender, content, timestamp):
        self.sender=sender
        self.content=content
        self.timestamp=timestamp
    
    def __repr__(self):
        print(f"{self.timestamp} - {self.sender}: {self.content}")
        return
    
from datetime import datetime

class Chat:
    def __init__(self, name, users):
        self.name=name
        self.users=users
        self.messages=[]
    
    def send_message(self, sender, content):
        if sender not in self.users:
            raise ValueError("Sender is not part of this chat")
        timestamp = datetime.now()
        message = Message(sender, content, timestamp)
        self.messages.append(message)
        print(f"Chat: {self.name}, User:{', '.join([user.username for user in self.users])}")
    
    def search_message(self, keyword):
        return [message for message in self.messages if keyword.lower() in message.content.lower()]

    def __repr__(self) -> str:
        print(f"Chat: {self.name}, User:{', '.join([user.username for user in self.users])}")
        return

class ChatApplication:
    def __init__(self) -> None:
        self.users=[]
        self.chats=[]
    
    def register_user(self, username):
        user=User(username)
        self.users.append(user)
        return user
    
    def create_chat(self, name, users):
        chat=Chat(name, users)
        self.chats.append(chat)
        return chat

    def find_chat_by_name(self, name):
        for chat in self.chats:
            if chat.name==name:
                return chat
        return None

if __name__=='__main__':
    app=ChatApplication()
    alice=app.register_user("Alice")
    bob=app.register_user("Bob")
    carol=app.register_user("carol")


    alice.add_contact(bob)
    alice.add_contact(carol)
    bob.add_contact(alice)
    carol.add_contact(alice)

    chat_1_to_1=app.create_chat("Alice and Bob", [alice,bob])
    chat_1_to_1.send_message(alice, "Hi Bob!")
    chat_1_to_1.send_message(bob,"Hi alice !")
