from EdgeNodes import EdgeNode

class Node(EdgeNode):
    '''
    An individual object in a Canvas such as a file, group, text, or link.
    '''
    def __init__(self, id: str, x: int, y: int, width: int, height: int, nodeType: int, addressValue = None, color = None, subpath = None):
        # Color and id set during super init within EdgeNode superclass.
        super(Node, self).__init__(id, color)
        self.setX(x)
        self.setY(y)
        self.setWidth(width)
        self.setHeight(height)
        self.setNodeType(nodeType)
        self.setAddressValue(addressValue)
        if self.getNodeType(True) == 1:
            self.setSubpath(subpath)
        
    

    def getNodeType(self, asInt = False):
        '''
        Get the type of node. Can be: 
        - file = 1 
        - group = 2
        - text = 3
        - link = 4

        Return type is str by default.

        asInt: If asInt is set to True, returns the int value representing the type (1-4).
        
        Raises ValueError if type value is outside of expected range 1-4.
        '''
        if self.nodeType == 1:
            if asInt == True:
                return 1
            else: return "file"
        elif self.nodeType == 2:
            if asInt == True:
                return 2
            else:
                return "group"
        elif self.nodeType == 3:
            if asInt == True:
                return 3
            else:
                return "text"
        elif self.nodeType == 4:
            if asInt == True:
                return 4
            else:
                return "link"
        else:
            raise ValueError("Unrecognized value error: " + str(self.nodeType))

    def setNodeType(self, nodeType: int):
        '''
        Enforces type int value to be within 1-4 range.
        1 = file
        2 = group
        3 = text
        4 = link

        Raises ValueError if type value is outside of expected range 1-4.
        '''
        if self.isType(1, nodeType):
            if nodeType < 1 or nodeType > 4:
                raise ValueError("Unrecognized value error"  + str(nodeType))
            else:
                self.nodeType = nodeType
        else:
            raise TypeError("Unrecognized type: " + str(type(nodeType)))

    def getCoord(self, coordType: int):
        '''
        Generic function to check type of coord and return value.

        coordType: int
        - 1: x
        - 2: y
        - 3: height
        - 4: width
        
        Raises TypeError if type is not int.
        '''
        if self.isType(coordType, 1):
            if coordType == 1:
                return self.x
            elif coordType == 2:
                return self.y
            elif coordType == 3:
                return self.height
            elif coordType == 4:
                return self.width
        else:
            raise TypeError("Unrecognized type:" + type(self.x))

    def getX(self):
        '''
        Returns the int value of x coordinate.

        Raises TypeError if x is not of type int.
        '''
        return self.getCoord(1)

    def setX(self, x: int):
        '''
        Set int value for x coordinate.
        '''
        self.x = x

    def getY(self):
        '''
        Returns the int value of y coordinate.

        Raises TypeError if y is not of type int.
        '''
        return self.getCoord(2)

    def setY(self, y: int):
        '''
        Set int value for y coordinate.
        '''
        self.y = y

    def getHeight(self):
        '''
        Returns int value of height coordinate.

        Raises TypeError if height is not of type int.
        '''
        return self.getCoord(3)

    def setHeight(self, height: int):
        '''
        Set int value for height coordinate.
        '''
        self.height = height

    def getWidth(self):
        '''
        Returns int value of width.

        Raises TypeError if width is not of type int.
        '''
        return self.getCoord(4)

    def setWidth(self, width: int):
        '''
        Set int value for width.
        '''
        self.width = width

    def getAddressValue(self):
        '''
        Returns file for file type nodes and label for all other node types.
        '''
        if self.isType(2, self.addressValue):
            return self.addressValue

    def setAddressValue(self, addressValue):
        '''
        Sets addressValue for Node.

        Address value correlates to different Node variables depending on type of Node:
        - 1: file = file
        - 2: group = label - Note: label is optional.
        - 3: text = text
        - 4: link = url
        '''
        if self.getNodeType(True) == 2 and (addressValue == None or addressValue == ""):
            self.addressValue = None
        elif self.isType(2, addressValue):
            self.addressValue = addressValue
        else:
            raise TypeError("Unrecognized type for Node type addressValue: Node type is: " + type(self.getNodeType()) + ", and addressValue type is: " + type(addressValue))

    def getSubpath(self):
        '''
        Returns subpath for file types.

        If subpath not set, returns None.

        Raises error if accessed on Nodes that are not of type file.
        '''
        if self.nodeType(True) == 1:
            if self.isType(2, self.subpath):
                return self.subpath
            else:
                return None
        else:
            raise TypeError("Cannot access subpath on non-file Node: Node type is" + self.getNodeType() + "subpath type is: " + type(self.subpath))

    def setSubpath(self, subpath):
        '''
        Sets subpath to provided str. If type provided is not str, sets subpath to None.

        Raises error if accessed on Nodes that are not of type file.
        '''
        if self.getNodeType(True) == 1:
            if self.isType(2, subpath):
                self.subpath = subpath
            else:
                self.subpath = None
        elif subpath == None:
                self.subpath = None
        else:
            raise TypeError("Cannot access subpath on non-file Node: Node type is" + self.getNodeType() + "subpath type is: " + type(subpath))
        
# node = Node("ff7e7775bba2d8a5", -628, -200, 400, 400, 1, "Software/Software.md")

# print(str(node.getX()))
