from EdgeNodes import EdgeNode
from Nodes import Node

class Edge(EdgeNode):
    '''
    A link between two nodes with an arrow pointing from one to the other.
    '''
    def __init__(self, id: str, fromNode: Node, fromSide, toNode: Node, toSide, color = None, label = None):
        # Color and id set during super init within EdgeNode superclass.
        super(Edge, self).__init__(id, color)
        # Nodes must be set before direction.
        self.setNode(fromSide, 1)
        self.setNode(toSide, 2)
        self.setDirection(fromSide, 1)
        self.setDirection(toSide, 2)

    def isNode(self, value):
        '''
        Check if input type is a Node object.

        Returns true if type matches Node, and false if another type of object.
        '''
        if type(value) == Node:
            return True
        else:
            return False
    
    def determineNodeSourceInt(self, nodeSource):
        '''
        Check to see if input is the fromSide Node or the toSide Node.

        Accepts: 
        - string 'fromSide' or 'toSide'
        - int values 1-2
        - Node object if Node is set as fromNode or toNode.

        Returns 1 if node detected is fromSide Node.
        Returns 2 if node detected is toSide Node.

        Raises a ValueError in three conditions:
        - int detected, but outside accepted range.
        - str detected, but does not match required strings.
        - Node detected, but does not match either Node set on object.

        Raises a TypeError if input is not int, str, or Node.

        '''
        node = None
        if self.isType(1, nodeSource):
            if nodeSource < 3 and nodeSource > 0:
                return nodeSource
            else:
                raise ValueError("Int value for fromSide or toSide must be in range 1-2. Int detected: " + str(nodeSource))
        
        elif self.isType(2, nodeSource): 
            if nodeSource == "fromSide":
                return 1
            elif nodeSource == "toSide":
                return 2
            else:
                raise ValueError("Unexpected str. NodeSource must be 'fromSide' or 'toSide'. Input str: " + nodeSource)
        
        elif self.isNode(nodeSource):
            # ToDo: Node checking should call getNode() function.
            if nodeSource == self.fromNode:
                return 1
            elif nodeSource == self.toNode:
                return 2
            else:
                raise ValueError("Unrecognized Node as source. Node found: " + str(nodeSource))
        else:
            raise TypeError("nodeSource must be str: 'fromSide' or 'toSide', int value between 1-2, or Node object. Input detected: " + type(nodeSource))
    
    def determineNodeSourceString(self, nodeSource):
        '''
        Check to see if input is the fromSide Node or the toSide Node.

        Accepts: 
        - string 'fromSide' or 'toSide'
        - int values 1-2
        - Node object if Node is set as fromNode or toNode.

        Returns str "fromSide" if node detected is fromSide Node.
        Returns str "toSide"' if node detected is toSide Node.

        Raises a ValueError in three conditions:
        - int detected, but outside accepted range.
        - str detected, but does not match required strings.
        - Node detected, but does not match either Node set on object.

        Raises a TypeError if input is not int, str, or Node.
        '''
        source = self.determineNodeSourceInt(nodeSource)
        if source == 1:
            return "fromSide"
        elif source == 2:
            return "toSide"
        else:
            raise ValueError("Unexpected input for nodesource: " + str(nodeSource)) 

    def getNode(self, nodeSource, forceAsNode = True):
        '''
         Returns a Node object for either the fromNode or toNode 
         based on passed in int:
         - 1: fromNode
         - 2: toNode

         toNode is the Node object to which the Edge's arrow will be pointing on the canvas.

         If forceAsNode parameter is set to False can also return None.
         forceAsNode parameter is set to True by default.

         Raises ValueError if int input is outside expected range.

         Raises TypeError if type input is unexpected or if requested 
         Node object is set to None with forceAsNode parameter set to True.
        '''
        # Ensure node source is in Int format regardless of input.
        nodeSource = self.determineNodeSourceInt(nodeSource)
        node = None
        if nodeSource == 1:
            node = self.fromNode
        elif nodeSource == 2:
            node = self.toNode
        else:
            raise ValueError("Unexpected input for nodeSource. Must be int 1-2 or string 'fromSide' or 'toSide'. Input:" + type(nodeSource) + " Value:" + str(nodeSource))
        if self.isNode(node):
            return node
        # If forceAsNode is off, allows Node with value of None to be returned as None. 
        # Otherwise forces a TypeError if Node is set to None.
        if node == None and forceAsNode == False:
            return None
        else:
            raise TypeError("Unepected object as nodeSource. Input: " + type(self.node))
    
    def setNode(self, node, nodeSource, forceAsNode = True):
        '''
        Sets Node value based on nodeSource indicating whether Node is set to toNode or fromNode. 
        toNode is the Node object to which the Edge's arrow will be pointing on the canvas.

        If forceAsNode is set to False (opposite of default behavior) Node object can also be set to None.
        None will raise a TypeError if forceAsNode is left at default value of True.
        Any other type of object will raise a TypeError.
        '''
        # Ensure node source is in Int format regardless of input.
        nodeSource = self.determineNodeSourceInt(nodeSource)
        if self.isNode(node):
            if nodeSource == 1:
                self.fromNode = node
            elif nodeSource == 2:
                self.toNode = node
            else:
                raise ValueError("Unexpected int value. Input: " + str(nodeSource))
        elif node == None and forceAsNode == False:
            if nodeSource == 1:
                self.fromNode = None
            elif nodeSource == 2:
                self.toNode = None
            else:
                raise ValueError("Unexpected int value. Input: " + str(nodeSource))
        else:
            raise TypeError("Unexpected type input. Expected Node. Input: " + type(node))
        
    def checkForMatchNode(self, node: Node, nodeSource):
        '''
        Check to see if opposite Node matches. Helps to ensure that the same Node object is 
        not put as both the fromSide and toSide nodes.

        Returns True if the opposite Node is the same.
        '''
        nodeSource = self.determineNodeSourceInt(nodeSource)
        if self.isNode(node):
            if nodeSource == 1:
                if self.getNode(1) != None:
                    if node == self.getNode(2):
                        return True
                    else:
                        return False
            elif nodeSource == 2:
                if node == self.getNode(1):
                    return True
                else: 
                    return False

    def getDirectionfromInt(self, intInput):
        '''
        Based in int input, returns a string for the correlating side.
        Sides are numbered in clock-wise order starting with top:

        - 1: top
        - 2: right
        - 3: bottom
        - 4: right

        Raises value error if input out of range 1-4.
        Raises type error if input not int.
        '''
        if intInput == 1:
            return "top"
        elif intInput == 2:
            return "right"
        elif intInput == 3:
            return "bottom"
        elif intInput == 4:
            return "right"
        elif self.isType(1, intInput):
            raise ValueError("Input out of range. Input must be between 1-4. Input: " + intInput)
        else:
            raise TypeError("Input type not int. Input: " + type(intInput))
        
    def getDirectionfromStr(self, strInput):
        '''
        Based in str input, returns an int for the correlating side.
        Sides are numbered in clock-wise order starting with top:

        - 1: top
        - 2: right
        - 3: bottom
        - 4: right

        Raises value error if input not specified strings.
        Raises type error if input not str.
        '''
        if strInput == "top":
            return 1
        if strInput == "right":
            return 2
        if strInput == "bottom":
            return 3
        if strInput == "left":
            return 4
        elif self.isType(2, strInput):
            raise ValueError("Unexpected string input. Expected 'top', 'right', 'bottom', or 'left'. Input: " + strInput)
        else:
            raise TypeError("Input type not str. Input: " + type(strInput))

    def getDirection(self, nodeSource, asInt = False):
        '''
        Get the direction from which an Edge is coming or going.

        Returns a string for the correlating side if asInt is set to False (default).
        Returns an int for the correlating side if asInt is set to True.

        Sides are numbered in clock-wise order starting with top:

        - 1: top
        - 2: right
        - 3: bottom
        - 4: right

        Accepts: 
        - string 'fromSide' or 'toSide'
        - int values 1-2
        - Node object if Node is set as fromNode or toNode.

        Raises a ValueError in three conditions:
        - int detected, but outside accepted range.
        - str detected, but does not match required strings.
        - Node detected, but does not match either Node set on object.

        Raises a TypeError if input is not int, str, or Node.
        '''
        node = self.determineNodeSourceInt(nodeSource)
        if node == 1:
            if asInt:
                return self.fromSide
            else:
                return self.getDirectionfromInt(self.fromSide)
        elif node == 2:
            if asInt:
                return self.toSide
            else:
                return self.getDirectionfromInt(self.toSide)
        else:
            raise TypeError("Unexpected error getting node direction: " + str(self))

    def setDirection(self, direction, nodeSource):
        '''
        Sets the direction from which an Edge is coming or going.

        Sides are numbered in clock-wise order starting with top:

        - 1: top
        - 2: right
        - 3: bottom
        - 4: right

        Accepts: 
        - string 'fromSide' or 'toSide'
        - int values 1-2
        - Node object if Node is set as fromNode or toNode.

        Raises a ValueError in three conditions:
        - int detected, but outside accepted range.
        - str detected, but does not match required strings.
        - Node detected, but does not match either Node set on object.

        Raises a ValueError if int input for direction is outside expected range (1-4).
        Raises a TypeError if input is not int, str, or Node.
        '''
        node = self.determineNodeSourceInt(nodeSource)

        if self.isType(1, direction):
            if direction > 0 and direction < 5:
                if node == 1:
                    self.fromSide = direction
                elif node == 2:
                    self.toSide = direction
            else:
                raise ValueError("Input out of range. Expected 1-4. Input: " + str(direction))
        elif self.isType(2, direction):
            directionInt = self.getDirectionfromStr(direction)
            if node == 1:
                self.fromSide = directionInt
            elif node == 2:
                self.fromSide = directionInt
        else:
            raise TypeError("Unexpected type as direction. Accepts str, int, or Node. Input: " + type(direction))

