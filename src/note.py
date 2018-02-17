import time

#want this dict into a class so that we may swap out this implementation later.

#Today, Yesterday, Last Week, Last Month, Last Year.
#{eatetime: int, data:str}

class Notes:
    noteDict = {}
    def __init__(self):
        self.noteDict = makeDummyNotes()

    def pushNote(self, note):
        self.noteDict[int(time.time())] = note

    def popNote(self, time):
        return self.noteDict.pop(time, "None")

    def lastNote(self):
        return list(self.noteDict.values())[-1]

    def lastBunchofNotes(self):
        if len(self.noteDict) > 10:
            return list(self.noteDict.values())[-10:]
        else:
            return list(self.noteDict.values())[-1:]

    def findInRange(self, begin, end):
        retDict = {}
        for key in self.noteDict:
            if key >= begin and key <= end:
                retDict[key] = self.noteDict[key]
        return retDict

    def getAll(self):
        return self.noteDict

def makeDummyNotes():
    dummyNotes = {
            1502827221: "I need to go buy a stove, some insulation, and some wood paneling for my van.",
            1516046421: "It's pretty cold outside, I'm glad my van is well insulated.",
            1517515221: "I'm hosting a party next week so I'd better plan out the menu.",
            1518206421: "tomorrow I'm going to a hackathon so I'd better not get too drunk.",
            1518292578: "today I was pulled over by the cops on the way to a hackathon and got a speeding ticket"}
    return dummyNotes
