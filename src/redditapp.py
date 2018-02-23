from enum import Enum
import urllib.request
import json
import requests

#class CatState(Enum):
    #Active = 0
    #Banned = 1

class RedditApp:
    def __init__(self):
        #self.userState = CatState.Active
        self.lastWord = ""
        self.picsdict = None
        #Grab the top 25 entries from the associated reddit page and display them.
        self.ctr = 0


    def handle(self, incomingtext):
        someDict = dict()
        
        #convert to lower, remove spaces.
        lowerText = incomingtext.lower()
        lowerText = lowerText.replace(" ", "")

        if lowerText == "cat" or lowerText == "cats" or lowerText == "got" or lowerText == "chat":
            
            if self.lastWord != "cat":
                self.picsdict = None
                self.ctr = 0
                self.lastWord = "cat"
            someDict = self.showThing("catsstandingup")
            
        elif lowerText == "dog" or lowerText == "dogs":
            
            if self.lastWord != "dog":
                self.picsdict = None
                self.ctr = 0
                self.lastWord = "dog"
            someDict = self.showThing("dogpictures")
            
        #"Show me something"
        else:
            if self.lastWord != lowerText:
                self.picsdict = None
                self.ctr = 0
            someDict = self.showThing(lowerText)
            
        return someDict

    def getAPicture(self, picType):
        picUrl = ""
        if self.picsdict is None:
            try:
                url = "https://www.reddit.com/r/" + picType + "/.json"
                headers = {'user-agent': 'ChromeCats'}
                r = requests.get(url, headers=headers)
                self.picsdict = r.json()
                print("fetching pics")
            except Exception as e:
                print("Error fetching json: ", e)
                return "https://http.cat/429.jpg"

        i = self.ctr % len(self.picsdict['data']['children'])
        picUrl = self.picsdict['data']['children'][i]['data']['url']
        if picUrl[-1] == "v":
            picUrl = picUrl[:len(picUrl) - 1]
        self.ctr += 1
        return picUrl
        
    #all three of these should return JSON themselves.
    def showPic(self, picType):
        picDict = dict()
        picDict["actionType"] = "show_image"
        actionDetail = dict()
        actionDetail["url"] = self.getAPicture(picType)
        #make a json call for a cat image.
        picDict["actionDetail"] = actionDetail
        #display a cat picture
        return picDict

    def leave(self):
        leaveDict = dict()
        leaveDict["actionType"] = "leave"
        actionDetail = dict()
        actionDetail["actionDetail"] = actionDetail
        return leaveDict
