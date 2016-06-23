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

Slap the student thus increasing its energy level.

#### Arguments

student object

#### Return value
    None

### ```teach```

    Teaches the student thus increasing its knowledge level but decreasing its energy level.

#### Arguments

    student object

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

    Determines the average knowledge level in class.

#### Arguments

    list of students

#### Return value

    float

### ```check_energy```

    Determines the average energy level in class.

#### Arguments

    list of students

#### Return value

    float
