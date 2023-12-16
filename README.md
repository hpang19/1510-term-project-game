# 1510-term-project-game

Every program needs a README.md

This is written in markdown. Read about markdown here: [markdowncheatsheet](https://www.markdownguide.org/cheat-sheet/)

## Your names:

Hsin Pang (and Joey Cho)

## Your student numbers:

A01368516 (and A01366231)

## Your team's GitHub username:

hpang19 



## Game Title: A Good Strong Cuppa

### Introduction
All human beings need a nice cup of tea to get through their day. Chris, the instructor of British Columbia 
Institute of Technology, is a huge fan of tea. He has a very strong and strict taste of having tea, which is
matcha and ginger tea. 

In this game, player's goal is to make all different kinds of tea required for each level
and hence make the character, aka Chris, maintain his caffeine level. Our final goal is to give Chris
enough tea so that he can go work with good energy.

### Level 1: Saturday Morning
Today is Saturday. Raining hard outside. C'mon! It's Saturday morning. He's worked hard for the entire week.
He wants to stay dry with his cozy blanket and just start his day with some nice cup of tea. 
He decides to make tea by himself at home. 
In this level, the player needs to collect all the required materials to make a cup of matcha tea while maintaining 
positive caffeine level.
There may be some challenges while achieving the goal.
Once making the tea, his caffeine level will increase. The player achieves level 2.

### Level 2: Sunday Dilemma
Today is Sunday. Now he needs some legit matcha. Oops, all of his favourite starbucks stores are closed due to
maintenance issue. He decided to go to the grocery store and get some materials to serve himself a nice good matcha tea.
In this level, the player needs to collect all the required materials to make a cup of matcha tea while maintaining 
positive caffeine level.
There may be some challenges while achieving the goal.
Once making the tea, his caffeine level will increase. The player achieves level 3.

### Level 3: Monday Blues
Today is Monday. Oh, boy. He doesn't feel too well. He must've caught cold while getting groceries yesterday.
He needs warm and soothing ginger-turmeric tea. Ah, a farmers market comes near his house and he heard that the vendor 
that sells the best organic ginger and turmeric that he has ever tried. 
In this level, the player needs to collect all the required materials to make a cup of ginger-turmeric tea while 
maintaining 
positive caffeine level.
There may be some challenges while achieving the goal.
Once making the tea, his caffeine level will increase. The player needs to fight against the final boss, which is 
Joey and Hsin.

### Final Boss Battle
To win the game, you need to win from the battle with Joey and Hsin. They will bother you with 
python-related questions. You have to answer the question right and then make to go work!

*** There will be some bonus item which will cheer you up while playing the game to increase the caffeine level 
before you make and drink the tea. You can make use of it.


# Instructions:

## Running the Program

The graphical user interface (GUI) for this program has been developed using Tkinter. To start playing the game, follow these steps:

1. Open your terminal.
2. Navigate to the directory where the game files are located. For example, if the files are in the "game" directory:

    ```bash
    cd path/to/game/directory
    ```

3. Type the following command to initiate the game:

    ```bash
    python3 ./game_gui.py
    ```

This command will launch the game interface, allowing you to enjoy the gameplay.

## Understanding the Flowchart

The flowchart accurately represents the logic flow of the main function within the game() chart in game.pdf under 
pdf_files directory. 

Please note, however, that the actual main function within the game_gui.py file encompasses numerous 
Tkinter-specific functions. These functions contribute significantly to the graphical interface's functionality but 
are not depicted within the flowchart.

## Gameplay Tips

1. **Movement Controls:** Use directional buttons to navigate the character.
   
2. **Unlocking Map Areas:** As the player levels up, more map areas will become unlocked, offering new challenges.

3. **Navigating Places:** When entering or exiting places like the kitchen, grocery store, or market, ensure to use 
   the "Door" to enter or exit.

4. **Game Progress Save:** Exiting the game before completion saves the player's status locally in the data 
   directory. This data will be restored when the game is resumed later.

5. **Game Duration:** The approximate time required to complete the game ranges from 5 to 10 minutes, providing an engaging short gameplay experience.

6. **Skills Needed:** Success in the game requires proficiency in mathematics and Python. Stay tuned for math and Python challenges!

## Required Components

| Component                                         | File Location (selected)    | Line Number (selected)  |
|---------------------------------------------------|-----------------------------|-------------------------|
| (5b) 10 x 10 grid-based environment               | ./game_gui.py               | 29 - 30                 |
| (5c) character's measurement and abilities        | character/game_character.py | 24 - 31                 |
| (5d) four cardinal directions                     | ./game_gui.py               | 198 - 204               |
| (5e) chance to encounter obstacles                | challenges/foes.py          | 47 - 52                 |
| (5f) character overcome obstacles                 | challenges/foes.py          | 74, 122, 175            |
| (5g) game ends when character achieves final goal | ./game_gui.py               | 137 - 139               |
| (7a) use of immutable data structures (tuple)     | board/game_board.py         | 35, 40, 44, 45          |
| (7b) use of mutable data structures (dictionary)  | board/game_board.py         | 26                      |
| (7c) use of exception handling                    | ./game_gui.py               | 90 - 97                 |
| (7g) use of list / dictionary comprehensions      | character/game_character.py | 64                      |
| (7h) use of if statements                         | character/game_character.py | 101, 106                |
| (7i) use of for loop / while loop                 | board/game_board.py         | 30, 31                  |
| (7j) use of membership operators                  | board/game_board.py         | 104                     |
| (7k) use of range function                        | board/game_board.py         | 30, 31                  |
| (7l) use of functions from itertools              | ./game_gui.py               | 46, 54                  |
| (7m) use of random module                         | challenges/foes.py          | 48, 50, 52              |
| (7n) function annotations                         | all except for game_gui.py  | all functions           |
| (7o) doctests and unit tests                      | almost all functions        | in almost all functions |
| (7p) use of formatted sting                       | levels/level.py             | 27, 30                  |
| **_BONUS_** graphical user interface              | game_gui.py                 | all                     |
| **_BONUS_** save character status in file         | game_gui.py                 | 241 - 253               |
 
