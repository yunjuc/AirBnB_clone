![alt text](https://news4c.com/wp-content/uploads/2017/11/Airbnb-Update.png)

# Overview

This is the first part to the AirBnB clone project for the Holbertonschool.
It includes the console which we can use to manage our AirBnB objects. Thanks, shell!

## Instructions

First, clone our repo:
`$ git clone https://github.com/yunjuc/AirBnB_clone.git`

To start the console, run:
`$ ./console.py`

## Usage

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

_*List of class: BaseModel, User, City, State, Place, Review, Amenity_

### Examples

The console allows us to manage the objects of our project:
* Create a new object
```
(hbnb) create BaseModel
4cd2bf8f-69b7-440f-8df9-5cc8f223776a
(hbnb)
```
* Retrieve an object from a file
```
(hbnb) show BaseModel 4cd2bf8f-69b7-440f-8df9-5cc8f223776a
[BaseModel] (4cd2bf8f-69b7-440f-8df9-5cc8f223776a) {'updated_at': datetime.datetime(2018, 2, 15, 9, 14, 38, 621710), 'id': '4cd2bf8f-69b7-440f-8df9-5cc8f223776a', 'created_at': datetime.datetime(2018, 2, 15, 9, 14, 38, 621701)}
(hbnb)
```
* Update attributes of an object
```
(hbnb) update BaseModel 4cd2bf8f-69b7-440f-8df9-5cc8f223776a name Holberton
(hbnb) show BaseModel 4cd2bf8f-69b7-440f-8df9-5cc8f223776a
[BaseModel] (4cd2bf8f-69b7-440f-8df9-5cc8f223776a) {'name': 'Holberton', 'updated_at': datetime.datetime(2018, 2, 15, 9, 14, 38, 621710), 'id': '4cd2bf8f-69b7-440f-8df9-5cc8f223776a', 'created_at': datetime.datetime(2018, 2, 15, 9, 14, 38, 621701)}
(hbnb)
```
* Destroy an object
```
(hbnb) destroy BaseModel 4cd2bf8f-69b7-440f-8df9-5cc8f223776a
(hbnb) show BaseModel 4cd2bf8f-69b7-440f-8df9-5cc8f223776a
** no instance found **
(hbnb)
```


