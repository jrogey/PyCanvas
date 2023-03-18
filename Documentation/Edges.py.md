[ReadMe Home](.././README.md)

# Edge Class

> - [isNode()](#isnodevalue)
> - [determineNodeSourceInt()](#determinenodesourceintnodesource)
> - [determineNodeSourceString()](#determinenodesourcestringnodesource)
> - [getNode()](#getnodenodesource-forceasnode--true)
> - [setNode()](#setnodenode-nodesource-forceasnode--true)
> - [checkForMatchNode()](#checkformatchnodenode-node-nodesource)
> - [getDirectionfromInt()](#getdirectionfromintintinput)
> - [getDirectionfromStr()](#getdirectionfromstrstrinput)
> - [getDirection()](#getdirectionnodesource-asint--false)
> - [setDirection()](#setdirectiondirection-nodesource)
> - [invertArrow()](#invertarrow)


## isNode(value)
---
Check if input type is a Node object.

Returns true if type matches Node, and false if another type of object.

## determineNodeSourceInt(nodeSource)
---
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

## determineNodeSourceString(nodeSource)
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

## getNode(nodeSource, forceAsNode = True)
---
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

## setNode(node, nodeSource, forceAsNode = True)
---
Sets Node value based on nodeSource indicating whether Node is set to toNode or fromNode. 
toNode is the Node object to which the Edge's arrow will be pointing on the canvas.

- node: The Node object to which the Edge will be connected
- nodeSource: Determines if the Node being set is being pointed to or from by the Edge.
- forceAsNode: Defaults to True. When False allows specified Node to be set to None.

If forceAsNode is set to False (opposite of default behavior) Node object can also be 
set to None.
None will raise a TypeError if forceAsNode is left at default value of True.

Any other type of object will raise a TypeError.

## checkForMatchNode(node: Node, nodeSource)
---
Check to see if opposite Node matches. Helps to ensure that the same Node object is 
not put as both the fromSide and toSide nodes.

Returns True if the opposite Node is the same.

## getDirectionfromInt(intInput)
---
Based in int input, returns a string for the correlating side.
Sides are numbered in clock-wise order starting with top:

- 1: top
- 2: right
- 3: bottom
- 4: right

Raises value error if input out of range 1-4.
Raises type error if input not int.

## getDirectionfromStr(strInput)
---
Based in str input, returns an int for the correlating side.
Sides are numbered in clock-wise order starting with top:

- 1: top
- 2: right
- 3: bottom
- 4: right

Raises value error if input not specified strings.
Raises type error if input not str.

## getDirection(nodeSource, asInt = False)
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

## setDirection(direction, nodeSource)
---
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

## invertArrow()
---
Inverts the direction for the arrow pointing between two nodes.