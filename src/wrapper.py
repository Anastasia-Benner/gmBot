import requests, json, time

class Wrapper:


    base = 'https://api.groupme.com/v3'

    def ___init__(self, token, bot_id, group_id):
        self.token = token
        self.bot_id = bot_id
        self.group_id = group_id


    def send_message(self, text, attachments=None): ### TODO: implement attachments
        url = base + '/bots/post'

        payload = {}
        payload['bot_id'] = bot_id
        payload['text'] = text

        requests.post(url, data=payload)


    def get_last_message(self):
        url = base + f'/groups/{self.group_id}/messages'

        payload = {}
        payload['limit'] = 1
        payload['token'] = self.token

        r = requests.get(url, params=payload)

        return json.loads(r.text)['response']['messages'][0]


    def get_group(self):
        url = base + f'/groups/{self.group_id}'

        payload = {}
        payload['token'] = self.token

        r = requests.get(url, params=payload)

        return json.loads(r.text)


    def get_users(self):
        return self.get_group['members']


    def get_all_messages(self):
        url = base + f'/groups/{self.group_id}/messages'

        payload = {}
        payload['limit'] = 100
        payload['token'] = self.token

        all_messages = []
        looking = True

        while looking
            time.sleep(1)
            r = requests.get(url, params=payload)

            if r.text == "":
                break

            all_messages += json.loads(r.text)['response']['messages']
            payload['before_id'] = json.loads(r.text)['response']['messages'][-1]['id']

        return all_messages
