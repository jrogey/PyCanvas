class EdgeNode():
    '''
    Class for shared code between Edges and Nodes.
    '''
    def __init__(self, id: str, color = None):
        self.setID(id)
        self.setColor(color)

    def isType(self, typeNeeded: int, value):
        '''
        Type check to ensure input is of a specific type:
        - 1 = int
        - 2 = str

        Returns True if type matches requested type and False if types do not match.

        Raises ValueError if typeNeeded is outside of range 1-2.
        '''
        typeToCheck = None
        if typeNeeded == 1:
            typeToCheck = int
        elif typeNeeded == 2:
            typeToCheck = str
        
        elif typeNeeded > 2 or typeNeeded < 1:
            raise ValueError("Unrecognized value error:" + str(typeNeeded))
            return None
        if type(value) == typeToCheck:
            return True
        else:
            return False
            
    def getID(self):
        '''
        Returns str of id.

        Raises TypeError if id is not str.
        '''
        if self.isType(2, self.id):
            return self.id
        else:
            raise TypeError("Unrecognized type: " + str(type(self.id)))

    def setID(self, id: str):
        '''
        Set id value.
        '''
        self.id = id

    def getColor(self):
        '''
        Get str of color.

        Raises TypeError if color is not str or None.
        '''
        if self.isType(2, self.color):
            return self.color
        elif self.color == None:
            return self.color
        else:
            raise TypeError("Unrecognized type:" + type(self.color))
    
    def setColor(self, color):
        '''
        Sets str for color.
        '''
        if self.isType(2, color):
            self.color = color
        elif color == None:
            self.color = None
        else:
            raise TypeError("Unrecognized type for color: " + type(color))