class pizzaApp(object):
    def __init__(self):
        self.name = "pizzaApp"

    def handle(self, str):
        return {"actionType": "speak",
                "actionDetail": "pepperoni"}

    def onStart(self):
        return "I have order an ten inch pepperoni cheese thich crush pizza. Estimated arrival is 20 mins"