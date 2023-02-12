# create class Bot
class Bot:
    def __init__(self, name):
        self.name = name

    def say_name(self):
        print(self.name)

    def send_message(self, message):
        print(message)


some_bot = Bot('Marvin')
some_bot.say_name()
some_bot.send_message('Hello guys')

# Create class TelegramBot inherited from Bot


class TelegramBot(Bot):

    def __init__(self, name, url=None, chat_id=None):
        self.url = url
        self.chat_id = chat_id
        super().__init__(name)

    def send_message(self, message):
        print(f'{self.name} bot says {message} to chat {self.chat_id} using {self.url}')

    def set_url(self, url):
        self.url = url

    def set_chat_id(self, chat_id):
        self.chat_id = chat_id


telegram_bot = TelegramBot('TG')

telegram_bot.say_name()
telegram_bot.send_message('Hello')
telegram_bot.set_chat_id(1)
telegram_bot.send_message('Hello')
telegram_bot.set_chat_id(2)
telegram_bot.send_message('Bye')

# Create a class MyStr(str), which overrides the __str__ method


class MyStr(str):

    def __str__(self):
        return self.upper()


my_str = MyStr('test')
print(my_str)

# Create a class User, which overrides the __eq__ method


class User:
    def __init__(self, name):
        self.name = name

    def __eq__(self, other):
        return self.name.upper() == other.name.upper()


first_user = User('ValenTyna')
second_user = User('valentYNA')

print(first_user == second_user)

# create class with type


def init_func(self, name):
    self.name = name


def say_name_func(self):
    print(self.name)


def send_message_func(self, message):
    print(message)


new_bot = type(
    'MyBot',
    (),
    {
        '__init__': init_func,
        'say_name': say_name_func,
        'send_message': send_message_func

    }
)

type_bot = new_bot('MarvelBot')
type_bot.say_name()
type_bot.send_message('Hello guys')


def init_func_tg(self, name, url=None, chat_id=None):
    self.url = url
    self.chat_id = chat_id
    self.name = name


def send_message_func_tg(self, message):
    print(f'{self.name} bot says {message} to chat {self.chat_id} using {self.url}')


def set_url_func_tg(self, url):
    self.url = url


def set_chat_id_func_tg(self, chat_id):
    self.chat_id = chat_id


new_tg_bot = type(
    'MyTelegramBot',
    (Bot,),
    {
        '__init__': init_func_tg,
        'say_name': say_name_func,
        'send_message': send_message_func_tg,
        'set_url': set_url_func_tg,
        'set_chat_id': set_chat_id_func_tg
    }
)

tg_bot = new_tg_bot('Star')
tg_bot.say_name()
tg_bot.send_message('Bye')
tg_bot.set_chat_id(1)
tg_bot.send_message('Hello')
