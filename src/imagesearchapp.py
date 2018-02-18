class imageSearchApp(object):
    def __init__(self):
        self.name = "imageSearchApp"

    def handle(self, str):
        return {"actionType": "speak",
                "actionDetail": "image image"}

    def onStart(self):
        return "image image"