


class Bot:



    def __init__(self, wrapper, actions):
        self.wrapper = wrapper
        self.actions = actions


    def addAction(self, action):
        self.actions.append(action)


    def help(self):
        out = ''
        for action in self.actions:
            out += f'{action.trigger}: {action.help_text}'
        return out


    def process(self, message):
        for action in self.actions:
            action.process(message)
