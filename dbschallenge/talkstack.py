import json

import requests


class TalkStack:
    url = "https://talkstackcall-staging-d3b17e085e0a.herokuapp.com/parallel/calls"

    def __init__(self, number):
        self.number = number

    def post(self):
        data = [
            {
                "to": f"+65{self.number}",
                "from": "+6531298349",
                "projectId": "4851ffde-3a6b-4ea5-8912-a125b966b0fc",
                "language": "English",
                "message": "Hi",
                "test": True,
                "extraVariables": {"phone": "+393928208218"},
                "speechProvider": "talkstack",
                "endpointing": 500,
                "useGateway": True,
                "interruptable": False,
                "voiceId": "uwDFppbC174JuppN5J9N",
                "voiceProvider": "elevenlabs",
                "voiceQuality": 4,
                "voiceEngine": "eleven_turbo_v2",
            }
        ]
        response = requests.post(self.url, json=json.dumps(data))

        try:
            response = requests.post(self.url, json=data)
            response.raise_for_status()
            print("POST request successful")
            print(response.text)
            return response.text
        except requests.exceptions.RequestException as e:
            print(f"POST request failed: {e}")
