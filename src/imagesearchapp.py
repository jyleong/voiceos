class imageSearchApp(object):
    def __init__(self):
        self.name = "imageSearchApp"

    def handle(self, str):
        return {"actionType": "speak",
                "actionDetail": "image image"}

    def onStart(self):
        return "searching images... oops looks that part of me is not yet implemented"