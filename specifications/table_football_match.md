# table_football_match

## Description
This class represents the table-football matches played in Codecool. One instance is one match.

## Parent class
None

## Attributes

* ```proper_time```
  * data type: boolean
  * description: stores the time when the match is played. It's true if it's played in a period when it's allowed based on the House Rules of Codecool.
* ```if_official```
  * data type: boolean
  * description: stores the boolean value of the match: is it played by official Codecool rules or not?
* ```players```
   * data type: integer
   * description: stores the number of players playing the match (2 or 4)



## Class methods

## ```generate_list ```

It generates a list with all the table-football matches in it.

### Argument

a csv file

### Return Value

list with all the matches in it


## Instance methods

###

### ```is_played```

This method chooses a match. It chooses random match.players players. It observes its proper_time value; if it is False, it chooses a random mentor to run the mentor.slap function on all the random players.
If it's True, it sums up the teammates' table_football_level. The higher wins.
Players' energy_level rises or falls more if the match is official and less if unofficial.

#### Arguments

table_football_match

#### Return value

None
