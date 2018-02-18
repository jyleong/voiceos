from enum import Enum
import urllib.request
import json
import requests

class CatState(Enum):
    Active = 0
    Banned = 1

class CatApp:

    def __init__(self):
        self.userState = CatState.Active
        self.catsdict = None
        self.ctr = 0

    def onStart(self):
        return {"actionType": 'speak', "actionDetail": 'meow'}


    def handle(self, incomingtext):
        if self.userState == CatState.Active:
            someDict = dict()
            lowerText = incomingtext.lower()
            possibles = ['cast', 'cat', 'cats', 'got', 'chat']
            if any([lowerText == possible for possible in possibles]):
                someDict = self.showCat()
            elif lowerText == "dog":
                someDict = self.permaban()
            elif lowerText == "i don't like cats":
                someDict = self.leave()
            else:
                someDict = {"actionType":"nothing"}
            return someDict
        else:
            return {"actionType":"nothing"}

    def getCatPicture(self):
        picUrl = ""



        if self.catsdict is None:
            try:
                url = "https://www.reddit.com/r/catsstandingup/.json"
                headers = {'user-agent': 'ChromeCats'}
                # r = requests.get(url, headers=headers)
                # self.catsdict = r.json()
                print("not fetching cats")
            except Exception as e:
                print("Error fetching json: ", e)
                return "https://http.cat/429.jpg"

                ####
        # children = self.catsdict['data']['children']
        children = ['https://i.imgur.com/tH4w188.jpg', 'https://i.redd.it/768esmx26yg01.jpg', 'https://i.imgur.com/kd1MyPI.gifv', 'https://imgur.com/5iKEdPH', 'https://i.redd.it/fft2o3lhuug01.jpg', 'https://i.redd.it/5ajndikg2vg01.jpg', 'https://i.redd.it/088nngi7vrg01.jpg', 'https://i.redd.it/d2kkf4x5qsg01.gif', 'https://i.redd.it/psaov5cegug01.jpg', 'https://i.imgur.com/HCgpdP8.gifv', 'https://i.redd.it/09py3m419vg01.jpg', 'https://v.redd.it/m4163k9qmpg01', 'https://i.redd.it/yzjuo2k2ktg01.jpg', 'https://i.imgur.com/EEiSVN5.jpg', 'https://imgur.com/85AcYJQ', 'https://i.redd.it/rhr53xunikc01.jpg', 'https://i.redd.it/c20j46lk7tg01.jpg', 'https://i.redd.it/1g2ez2kmgng01.jpg', 'https://i.imgur.com/YYxyOzh.gifv', 'https://i.imgur.com/DKQwWx9.jpg', 'https://i.redd.it/v4a597jn2pg01.jpg', 'https://i.imgur.com/C0bentL.mp4', 'https://i.redd.it/nv7xb1fpblg01.jpg', 'https://i.redd.it/0xxd530lrlg01.jpg', 'https://i.imgur.com/dWQ4YW1.jpg']
        i = self.ctr % len(children)
               ####

        # print ([child['data']['url'] for child in children])
        # picUrl = children[i]['data']['url']
        picUrl = children[i]
        if picUrl[-1] == "v":
            picUrl = picUrl[:len(picUrl) - 1]
        self.ctr += 1

        #this is the first cat picture.
        return picUrl
        #return catdict['data']['children'][0]['data']['url']

    #all three of these should return JSON themselves.
    def showCat(self):
        return {"actionType": "show_image",
        "actionDetail": { "url": self.getCatPicture() } }

    def permaban(self):
        #display a 'you are banned' sad cat picture
        #it is up the user to say 'take me home' to exit.banDict = dict()
        banDict = dict()
        banDict["actionType"] = "show_image"
        actionDetail = dict()
        actionDetail["url"] = "https://i.imgflip.com/24rtuf.jpg"
        banDict["actionDetail"] = actionDetail
        self.userState = CatState.Banned
        return banDict

    def leave(self):
        leaveDict = dict()
        leaveDict["actionType"] = "leave"
        actionDetail = dict()
        actionDetail["actionDetail"] = actionDetail
        return leaveDict
        #go up one level, not home.
