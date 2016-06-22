# Student

## Description
This class represents students at Codecool.

## Parent class
Person

## Attributes

* ```depend_level```
   * data type: string(never,all_matches,only_interesting)
   * description: stores the person's gamble addict level

* ```table_football_level```
  * data type: integer
  * description: stores the person's play skill(1-10)

* ```is_bet_on_expected_result```
  * data type: boolean
  * description: stores what does the person bet on

* ```knowledge_level```
  * data type: integer
  * description: stores knowledge level of the student

* ```energy_level```
  * data type: integer
  * description: stores energy level of the student




## Instance methods

### ```__init__```
The constructor of the object.

#### Arguments

All of the arguments of the class itself.

#### Return value
None


### ```bet```

match is an instance of Match class
observes self.depend_level and match.is_interesting to decide if the student bet
if he did: observes self.is_bet_on_surprise_result and match.is_surprising
#### Arguments
self, match

#### Return value
None
