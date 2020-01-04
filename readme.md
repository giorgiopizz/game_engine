# Game Engine

The game engine is composed of three files. The core of the game engine is in main.py. It reads a file that contains the structure and text of the game and displays it on the console letting the player make his choices. It also reads and writes a file that contains the choices made by the player.
The files are respectively game.dat, choices.dat.
The logic behind a text-based game is that there's a storyline, the choices made can change the path of the story so they must be stored somewhere, 
in case the player wants to pause the game or quit. The game.dat file is composed of every single path. It can be structured in JSON, every branch
of the story is a nested element.
This means that the file will be something like this
```
{
  "title":"Title"
  "text": "...",
  "options": [
    {
      "title":"first opt"
      "text": "...",
      "options": []
    },
    {
      "title":"second opt",
      "text": "...",
      "options": []
    }
  ]
}
```
Note for future upgrade: JSON can only handle 500 levels of nested object, a possible alternative is to divide the game.dat into subfiles. Subfiles may be created
splitting the storyline by chronological order or simply by some big choices, i.e. if one wants to separate file to handle better the story, it can be done by splitting into a first chronological part and into a second one, in which the choices made in the first will be taken into account. Or better if there are some big choices like kill a monster or something really important for the plot, one can divide the file for each possibility of the answer: say the player can either kill the monster or run, there will be a file containing the story after that the player has killed the monster and one with a different story. 
A script to help the screenwriter write the game.dat must be written. 

# Game Writer
The game_writer.py is the file that lets the screenwriter write the game.dat file. The writer is asked a sequence of questions to
determine the structure of the game. He must input for each node title, text and the options. Suppose we want to write the beginning of the story first we need to tell game_writer.py the title of the story, then an introduction and the text until
the first question is asked. At this point we need to include the question in the text, specify in the options section one node
for each possible answer to the question. The title of the node will be the answer, the text and the option of the node created
to answer the question can be modified after all the possible answers to the question have been specified
