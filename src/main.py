from bot import Bot
from wrapper import Wrapper
import json


def main():
    # Notes teehee here will go code that will store each incoming message and pass it to the bot
    # who will handle the shit from there
    pass


if __name__ == '__main__':

    config = json.loads('../data/bot_config.json')
    actions = []
    b = Bot(Wrapper(**config),actions)


    while True:
        main()
