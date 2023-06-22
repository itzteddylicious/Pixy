# __Pixy : A Virtual Assistant__
#### Video Demo: <https://youtu.be/mgx6XlZIhmM>

## __Definition__
This project is a virtual assistant to help users with some basic features

Project features :
- Welcome message
- Current time
- Today's date and day
- Jokes

## __Libraries__

__RICH__ : Render rich text, tables, progress bars, syntax highlighting, markdown and more to the terminal.[(Read more)](https://pypi.org/project/rich/)

__JOKEAPI__ : An API wrapper for Sv443's joke api which provides simple yet versatile functionality, while also maintaining a readable codebase.[(Read more)](https://pypi.org/project/jokeapi/)

__ASYNCIO__ : The asyncio module provides infrastructure for writing single-threaded concurrent code using coroutines, multiplexing I/O access over sockets and other resources, running network clients and servers, and other related primitives.[(Read more)](https://pypi.org/project/asyncio/)

__AIOHTTP__ : Async http client/server framework (asyncio).[(Read more)](https://pypi.org/project/aiohttp/)

__ART__ : ART is a Python lib for text converting to ASCII art.[(Read more)](https://pyypi.org/project/art/)

## **Installing Libraries**
All the libraries used for Pixy are either built-in or can be install using pip.

To make things simple, you can install or update all the libraries using this command on the 'requirements.txt' file :

```pip install -r requirements.txt```

## __Usage__

```python project.py```
```
 _     _ _______                _____         _____      _______ _______       _____  _____ _     _ __   __
 |_____| |______ |      |      |     |          |        |_____| |  |  |      |_____]   |    \___/    \_/
 |     | |______ |_____ |_____ |_____| .      __|__      |     | |  |  |      |       __|__ _/   \_    |
                                       '
How can I help you?
>
```
Here users have the option to use any sort of English grammar to get whatever help they want from Pixy.
#### NOTE : Pixy currently supports only a handful of features. They are mentioned above.

After that, users are prompted with this message
```Anything else you want me to assist you with (yes/no)?```

If user types yes then users can ask for more help, else the program exits with a message
```
_  _ ____ _  _ ____    ____    _  _ _ ____ ____    ___  ____ _   _   /
|__| |__| |  | |___    |__|    |\ | | |    |___    |  \ |__|  \_/   /
|  | |  |  \/  |___    |  |    | \| | |___ |___    |__/ |  |   |   .


Hope to see you soon!
```

## __Functioning__

In the file ```project.py```, you can see a main function and 5 more functions.

### __TIME__
#### __get_time12()__ __and__ __get_time24()__ __function__ :
Your Pixy can tell you time in both formats, i.e, 12 hr and 24 hr clock

### __DATE__
#### __get_date()__ __and__ __get_day()__ __function__ :
What's today's date?
Pixy can tell you that!
Oh! it also knows today's day!

### __Jokes__
#### __get_joke()__ __function__ :
Bored with all the work?
Take a break!
Let Pixy crack you up with a joke!

### __Pixy has more functionality but minimal. So tinker around with Pixy and see what else it has to offer__

### Brain behind Pixy : Yash Firke.
