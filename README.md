![alt text](https://news4c.com/wp-content/uploads/2017/11/Airbnb-Update.png)

# Overview

This is the first part to the AirBnB clone project for the Holbertonschool.
It includes the console which we can use to manage our AirBnB objects. Think, shell!

## Instructions:

First, clone our repo:
`$ git clone https://github.com/yunjuc/AirBnB_clone.git`

Now run the program:
`$ ./console`

## About the Command Interpreter a.k.a the Console

### Description

The console allows us to manage the objects of our project:
*Create a new object
*Retrieve an object from a file
*Do operations on objects
*Update attributes of an object
*Destroy an object

### Usage

Run the console by `./console.py`

### Commands

Commands | Description 
---------|-------------
**create** <class_name>| Creates new instance of class and saves it to JSON file and prints the id 
**quit**| Exits program
**help**| Displays command documents
**destroy** <class_name> <class_id>| Deletes instance
**show** <class_name> <class_id> | Prints __str__
**all** <class_name> <class_id> | Prints str rep of all instances
**update** <class_name> <class_id> <key> <value> | Appends attributes