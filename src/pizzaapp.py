class pizzaApp(object):
    def __init__(self):
        self.name = "pizzaApp"

    def handle(self, str):
        return {"actionType": "speak",
                "actionDetail": "pepperoni"}

    def onStart(self):
    	return {"actionType": "speak",
                "actionDetail": "I have ordered an ten inch pepperoni pizza. Estimated arrival is 20 mins"}
         