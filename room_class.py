from __future__ import annotations

class Room:
    """A template for creating a room object"""
    def __init__(self, roomDesc, objects: list):

        self._roomDesc = roomDesc
        self._objects = objects
        self._westExit = None
        self._eastExit = None
        self._northExit = None
        self._southExit = None
        self._dark = False

    def getDark(self):
        return self._dark
    
    def getRoomDesc(self):
        return self._roomDesc

    def getObjects(self):
        if self._objects:
            return self._objects
 
    def getExitWest(self):
        return self._westExit

    def getExitNorth(self):
       return self._northExit
    
    def getExitSouth(self):  
        return self._southExit

    def getExitEast(self):
        return self._eastExit
    
    def setDark(self, lightStatus):
        """Makes a room dark or illuminated"""
        self._dark = lightStatus
        
    def setExitWest(self, room: Room):
        self._westExit = room
    
    def setExitNorth(self, room: Room):
        self._northExit = room

    def setExitEast(self, room: Room):
        self._eastExit = room
    
    def setExitSouth(self, room: Room):
        self._southExit = room