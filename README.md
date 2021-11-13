# 0x00. AirBnB clone - The console
<div id="top"></div>

<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
  </ol>
</details>


<!-- ABOUT THE PROJECT -->
## About The Project

The console is the first segment of the AirBnB project at Holberton School that will collectively cover fundamental concepts of higher level programming. The goal of AirBnB project is to eventually deploy our server a simple copy of the AirBnB Website(HBnB). A command interpreter is created in this segment to manage objects for the AirBnB(HBnB) website.

#### Functionalities that the console will have :

* `quit:` Quit command to exit the program
* `EOF:` method to EOF to exit with `(CTRL + D)`
* `empyline:` an empty line + ENTER shouldn’t execute anything
* `create:` Create a new object (ex: a new User or a new Place)
* `show:` Prints the string representation of an instance based on the class name and id. 
* `destroy:` Deletes an instance based on the class name and id
* `all:` Prints all string representation of all instances based or not on the class name. 
* `update:` Update attributes of an object

<! -- Instalation -->
## Installation
* Clone this repository: `git clone "https://github.com/rodriguezalexp/AirBnB_clone.git"`
* Access AirBnb directory: `cd AirBnB_clone`
* Run hbnb(interactively): `./console` and enter command
* Run hbnb(non-interactively): `echo "<command>" | ./console.py`

<!-- GETTING STARTED -->
## Getting Started

This is an example of how you may give instructions on setting up your project locally.
To get a local copy up and running follow these simple example steps.

## Usage

## Examples of use
```
vagrantAirBnB_clone$./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  all  create  destroy  help  quit  show  update

(hbnb) all MyModel
** class doesn't exist **
(hbnb) create BaseModel
7da56403-cc45-4f1c-ad32-bfafeb2bb050
(hbnb) all BaseModel
[[BaseModel] (7da56403-cc45-4f1c-ad32-bfafeb2bb050) {'updated_at': datetime.datetime(2021, 11, 13, 20, 44, 44, 79052), 'id': '7da56403-cc45-4f1c-ad32-bfafeb2bb050', 'created_at': datetime.datetime(2021, 11, 13, 20, 44, 44, 789078)}]
(hbnb) show BaseModel 7da56403-cc45-4f1c-ad32-bfafeb2bb050
[BaseModel] (7da56403-cc45-4f1c-ad32-bfafeb2bb050) {'updated_at': datetime.datetime(2021, 11, 13, 20, 44, 44, 79052), 'id': '7da56403-cc45-4f1c-ad32-bfafeb2bb050', 'created_at': datetime.datetime(2021, 11, 13, 20, 44, 44, 789078)}
(hbnb) destroy BaseModel 7da56403-cc45-4f1c-ad32-bfafeb2bb050
(hbnb) show BaseModel 7da56403-cc45-4f1c-ad32-bfafeb2bb050
** no instance found **
(hbnb) quit
```

<!-- AUTHORS -->
## AUTHORS

Distributed under the MIT License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#top">back to top</a>)</p>

Yael Uribe - [Github](https://github.com/YaelUribe) / [Twitter](https://twitter.com/NeisseriaGI) 
Alexander Rodriguez - [Github](https://github.com/rodriguezalexp) / [Twitter](https://twitter.com/rodriguezalexp) 


Project Link: [https://github.com/rodriguezalexp/AirBnB_clone](https://github.com/rodriguezalexp/AirBnB_clone)


