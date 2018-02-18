class catApp(object):
    def __init__(self):
        self.name = "catApp"

    def handle(self, str):
        return {"actionType":"speak",
                "actionDetail":"meow"}

    def onStart(self):
        return "meow"