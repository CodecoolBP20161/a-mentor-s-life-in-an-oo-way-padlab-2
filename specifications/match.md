# Match

## Description
This class represents the football matches of the previous day (one instance is one match).

## Parent class
None

## Attributes

* ```match_name```
  * data type: string
  * description: contains the names of the two team
* ```important```
  * data type: boolean
  * description: the match is important or not
* ```expectation_probability```
   * data type: integer (1-10)
   * description: rounded probability of the expected result


##Class methods

### ```generate_list```

Creates a list, with all the matches in it.

#### Arguments
csv file

#### Return value

A list with all matches (objects) in it.

## Instance methods

### ```__init__```
The constructor of the object.

#### Arguments

All of the arguments of the class itself.

#### Return value
None

### ```expected_result```

Gives back a boolean which says that the result is expected or not
#### Arguments
* ```self: a match (object) from match.generate_list (list)```

#### Return value
boolean
