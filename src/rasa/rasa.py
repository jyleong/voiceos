from enum import Enum

class OSState(Enum):
    Home: 1
    Cat: 2
    Pizza: 3


class RasaResult(object):

    def __init__(self, msg, intent, confidence):
        self.msg = msg
        self.intent = intent
        self.confidence = confidence



