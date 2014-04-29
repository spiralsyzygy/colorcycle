CLover Wireless Coding Challenge:
=================================

Requires Django==1.6 and python => 2.7.6

Server side:
------------
Create's a list of random 9 digit numbers, 9 elements long and returns it as a json response. 
* The 9 digit numbers are actually created from concatenation of 3 random numbers, each ranging from 100 to 255.

Client side:
------------
An Ajax request to server gets json list with the 9 numbers.
A table with 3 rows of 3 cells each is created from the list of numbers.
Each cell has a class of "colorCyclable".
A list of table cells with the class "colorCylable" is created.
The numbers are split into RGB values. 
They are then mapped in order on to the style.backgroundColor property for each cell.

When the Cycle Colors button is pressed: 

The current color is read from each table cell style.backgroundColor property with an class "colorCyclable" into a list.
The first element of the colors are copied to the second element of a new list, skipping the first element.
Each subsequent element is copied, with the last element from the current color list, copied to the first element of the new color list. 

The new color list is then applied to each table cell element's style.background property.


