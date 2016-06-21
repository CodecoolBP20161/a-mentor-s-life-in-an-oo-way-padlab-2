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

Slap the student thus increasing its knowledge level.

#### Arguments

student object

#### Return value
    None

### ```teach```

    Teaches the student thus increasing its knowledge level and its energy level.

#### Arguments

    student object

#### Return value

        None

### ```decide```

    Decides between slap and teach.

#### Arguments

    None

#### Return value

    teach method or slap method



## Class methods

### ```choose```

    Chooses a mentor to do something.

#### Arguments

    generated list of mentors

#### Return value

    Mentor(Object)
