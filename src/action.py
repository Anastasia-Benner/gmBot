

class Action: #lawsuit haha get it



    def __init__(self, trigger, help_text):
        self.trigger = trigger
        self.help_text = help_text


    def check(self, message):
        return message[0] == self.trigger


    def parse(self, message):
        return message[1:].split()


    def do(self):
        pass


    def process(self, message):
        if self.check(message):
            args = self.parse(message)
            self.do(*args)
