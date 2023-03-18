[ReadMe Home](.././README.md)

# EdgeNodes.py

> - [isType()](#istypetypeneeded-int-value)
> - [getID()](#getid)
> - [setID()](#setidid-str)
> - [getColor()](#getcolor)
> - [setColor()](#setcolorcolor)

Abstract class to handle aspects of Nodes and Edges that are common including color and ID.

## isType(typeNeeded: int, value)
---
Type check to ensure input is of a specific type:
- 1 = int
- 2 = str

Returns True if type matches requested type and False if types do not match.

Raises ValueError if typeNeeded is outside of range 1-2.

## getID()
---
Returns str of id.

Raises TypeError if id is not str.

## setID(id: str)
---
Set id value.

## getColor()
---
Get str of color.

Raises TypeError if color is not str or None.

## setColor(color)
---
Sets str for color.

Raises TypeError if input is not str or None.