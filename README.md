    # MOVIE GUESSING GAME

    #### Video Demo:  <URL HERE>


    #### Description:
    This is my final project for **CS50P**.

    The idea of the game is simple and easy to run. The game starts as soon as we run the command:
    ```
    python project.py
    ```
    Once the program is running the *player* will receive the instructions on how to play. The how to play is a guessing game in which you will have 3 tries to get the movie title right. The game will give to you in each step a tip/more information on the Title (including the very first, second and third try).

    If you get it right the game will confirm it to you and exit, if you get it wrong the game will let you know and give all of the Title information so you might want to watch and that could be your new favorite title!

    I structured the game in 3 python files, in **game_struct.py** you will find some game aesthetic like:
    - The collored print function with the game instructions
    - collored print functions to announce the number of guess that you are attempting in the game
    In the **game_struct.py** you will also find the used libraries:
    ```
    colorama
    ```
    which was used to color our text in the terminal page.

    The second file that I have used is called **get_movie.py**. This file is not my main project but is the pulsing heart of it as it is the one that is getting information on the data base that all of the titles and titles information are store, and this is a crucial file to make it playable.

    In the **get_movie.py** we will fine the following libraries:
    ```
    sqlite3
    os
    ```
    the *os* library was used to locate our path and then used to switch the relative path to the database in order for us to be able to open and create a connection using python with the database.
    The *sqlite3* library was use to do all the work using python in the database.

    In the file **get_movie.py** you will find a main function which I used to call all of my function while creating this file to try and check the progress of other functions that was created to get information from the database. I have also a connection function that will
    ```
    try
    ```
    to connect and if fails it will
    ```
    print(error) as print(err)
    ```
    then I have one function to for each table that contains information that will be used in the game, like:
    - Directors
    - Movie title, release year
    - Actors
    - Ratings

    The function for the *movie title and release year* is returning a *tuple* and the rest of then is returning a *list*. The decision to this was because my program is getting as the first parameter to later be used in all of the other searches the *Movie Title* and while running and trying out the game progress I noticed that some of the tables for some Movies were missing 1 or more information (the most commons were actors and directors). So besides the *movie title and release year* search all of the rest
    ```
    return None
    ```
    if no information found or they will perform a **for loop** to each of the information that was returned by the database and **append** in the *list* to be returned.

    In the *main() function* when the mentioned functions above return their values it will still be treated in order to then return a value that will be used in the **project.py** file.

    What I mean by be treated is that as some function could return **None** values, our *main() function* will be looking for it. **So I created an empty list here to append only the values that exist and pass the None's**. The check of the values will append a dictionary within the created empty list.

    The return of the **get_movie.py** is so a complete list of dictionaries(the definition of complete would be to have only values and not None values, it may be missing on information but that will be handled in the **project.py**).

    Here I want to thank all the **CS50P** and **CS50** team! And extended the thanks even more as the database used in this file was from one of my **PSETs** from **CS50**.

    Now to my **project.py** file. In this file I have imported 1 library and all the other files created:
    ```
    import game_struct
    import get_movie
    import sys
    ```
    The file have a *main() function*, one function to deal with the directors information and another to deal with the actors information.

    The first thing that will happen is that the *main() function* will be printing the game instructions and then will be checking in a *while loop* if the return value of the *get_movie.py* function returned all of the necessary values (which should be 4) or not. If not 4 it will be asking *get_movie.py* for another value until it satisfy the number of values 4 within our list.

    Once we have the necessary number of values we will be processing then, some indexes in the list ([0] and [3]) are always the same, they contain only 2 key/value pair so I have assigned them to the variable without the need of another function.

    As the directors information and actors could have 1 or more, I have created a function to deal with each one of them. Those functions will return a string formated in the following way:
    - for one value found: will return the name in a variable, so:
    ```
    "Name"
    - for more than one value I created an empty string variable to then keep adding more info to it, so could look like this:
    ```
    "Name, Name, Name, "
    ```
    in this last case I would be correcting the end of the string so to return only:
    ```
    "Name, Name, Name"

    Once we have all of the values now stored in a variable in the *main() function* another *while loop* will be running for 3 times as it will be now the game logic.

    In each time it will be using the information that I have prepared in the variables created and printing to the player in the terminal.
