# Mentor

## Description
This class represents mentors at Codecool.

## Parent class
Person

## Attributes

* ```nick_name```
  * data type: string
  * description: stores the nick name of mentor

* ```slap_rate```
  * data type: integer(1-5)
  * description: stores the slap rate of mentors

## Instance methods

### ```__init__```

    The constructor of the object.

#### Arguments

    All of the arguments of the class itself.

#### Return value

    None

### ```slap```

    Slap students thus increasing their energy level.

#### Arguments

    list of student objects

#### Return value
    None

### ```teach```

    Teaches students thus increasing their knowledge level but decreasing their energy level.

#### Arguments

    list of student objects

#### Return value

    None




## Class methods

### ```feedback```

    The mentors give positive feedback to the whole class thus increasing every students energy.

#### Arguments

    Codecool class

#### Return value

    None

### ```generate_list```

    Creates a list of mentors.

#### Arguments

    csv file

#### Return value   

    List of mentors.





## Static methods

### ```check_knowledge```

    Determines the average knowledge level in class, and returns the students who are below that by a certain amount.

#### Arguments

    list of students

#### Return value

    list of students


### ```check_energy```

    Determines the average energy level in class, and returns the students who are below that by a certain amount.

#### Arguments

    list of students

#### Return value

    list of students
