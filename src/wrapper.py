import requests, json, time

class Wrapper:


    base = 'https://api.groupme.com/v3'

    def __init__(self, access_token, bot_id, group_id, **kwargs):
        self.token = access_token
        self.bot_id = bot_id
        self.group_id = group_id


    def send_message(self, text, attachments=None): ### TODO: implement attachments
        url = self.base + '/bots/post'

        payload = {}
        payload['bot_id'] = self.bot_id
        payload['text'] = text

        requests.post(url, data=payload)


    def get_last_message(self):
        url = self.base + f'/groups/{self.group_id}/messages'

        payload = {}
        payload['limit'] = 1
        payload['token'] = self.token

        r = requests.get(url, params=payload)

        return json.loads(r.text)['response']['messages'][0]


    def get_group(self):
        url = self.base + f'/groups/{self.group_id}'

        payload = {}
        payload['token'] = self.token

        r = requests.get(url, params=payload)

        return json.loads(r.text)


    def get_users(self):
        return self.get_group['members']


    def get_all_messages(self):
        url = self.base + f'/groups/{self.group_id}/messages'

        payload = {}
        payload['limit'] = 100
        payload['token'] = self.token

        all_messages = []
        looking = True
        ## TODO: make this less scary
        while looking:
            time.sleep(1)
            r = requests.get(url, params=payload)

            if r.text == "":
                break

            all_messages += json.loads(r.text)['response']['messages']
            payload['before_id'] = json.loads(r.text)['response']['messages'][-1]['id']

        return all_messages
