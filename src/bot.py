


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

            action.preprocess(message) #perform action on all messages

            response = action.process(message) #respond to specific calls
            if response is not '' or response is not None
                self.wrapper.send_message(response)
