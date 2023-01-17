# PyCanvas
A project to build a class for working with .canvas files such as those used in Obsidian. 

This project is not associated or affiliated with Obsidian.

> - [Nodes Class](#nodes-class)
>> - [getNodeType()](#getnodetypeasint--false)
>> - [setNodeType()](#setnodetypenodetype-int)
>> - [__isType()](#__istypevalue-typeneeded-int)
>> - [__getCoord()](#__getcoordcoordtype-int)
>> - [getX()](#getx)
>> - [setX()](#setxx-int)
>> - [getY()](#gety)
>> - [setY()](#setyy-int)
>> - [getHeight()](#getheight)
>> - [setHeight()](#setheightheight-int)
>> - [getWidth()](#getwidth)
>> - [getID()](#getid)
>> - [setID()](#setidid-int)
>> - [setColor()](#setcolorcolor)
>> - [getAddressValue()](#getaddressvalue)
>> - [setAddressValue()](#setaddressvalueaddressvalue)
>> - [getSubpath()](#getsubpath)
>> - [setSubpath()](#setsubpathsubpath)

## Nodes Class:
---
Class for working with individual nodes.

---

### getNodeType(asInt = False)
---
Get the type of node. Can be: 
- file = 1 
- group = 2
- text = 3
- link = 4

Return type is str by default.

asInt: If asInt is set to True, returns the int value representing the type (1-4).

Raises ValueError if type value is outside of expected range 1-4.

### setNodeType(nodeType: int)
---
Enforces type int value to be within 1-4 range.
1 = file
2 = group
3 = text
4 = link

Raises ValueError if type value is outside of expected range 1-4.

### __isType(value, typeNeeded: int)
---
Type check to ensure input is of a specific type:
- 1 = int
- 2 = str

Returns True if type matches requested type and False if types do not match.

Raises ValueError if typeNeeded is outside of range 1-2.

### __getCoord(coordType: int)
---
Generic function to check type of coord and return value.

coordType: int
- 1: x
- 2: y
- 3: height
- 4: width

Raises TypeError if type is not int.

### getX()
---
Returns the int value of x coordinate.

Raises TypeError if x is not of type int.

### setX(x: int)
---
Set int value for x coordinate.

### getY()
---
Returns the int value of y coordinate.

Raises TypeError if y is not of type int.

### setY(y: int)
---
Set int value for y coordinate.

### getHeight()
---
Returns int value of height coordinate.

Raises TypeError if height is not of type int.

### setHeight(height: int)
---
Set int value for height coordinate.

### getWidth()
---
Returns int value of width.

Raises TypeError if width is not of type int.

### setWidth(width: int)
---
Set int value for width.

### getID()
---
Returns str of id.

Raises TypeError if id is not str.

### setID(id: int)
---
Set id value.

### setColor(color)
---
Get str of color.

Raises TypeError if color is not str.

### getAddressValue()
---
Returns file for file type nodes and label for all other node types.

### setAddressValue(addressValue)
---
Sets addressValue for Node.

Address value correlates to different Node variables depending on type of Node:
- 1: file = file
- 2: group = label - Note: label is optional.
- 3: text = text
- 4: link = url

### getSubpath()
---
 Returns subpath for file types.

If subpath not set, returns None.

Raises error if accessed on Nodes that are not of type file.

### setSubpath(subpath)
---
Sets subpath to provided str. If type provided is not str, sets subpath to None.

Raises error if accessed on Nodes that are not of type file.