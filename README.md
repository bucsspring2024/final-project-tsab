Final-Project-tsab  Spring 2024

## Team Members
Tarif Sabur


## Project Description

This is a soccer game where two users can play against each other to see who can get more goals within two minutes.  Once the ball is hit once  in the beginning of the game the ball will move around and the users have move around to get the ball to go to the other person's goal.  Each time a user score, the scoreboard updates and the players reset to their respective starting positions; however note that the ball will begin moving from the center once the players reset.  Once the 120 seconds are up whoever scores the most goals wins the game.  Player 1 uses ASWD and plays as the Manblue team while player 2 uses UP DOWN LEFT and RIGHT buttons and plays are Manred team.  The two teams are supposed to represent both real life Premier League teams based in Manchester based off of their respective team colors.  First download all contents within the assets folder to make the gui, each player, the ball, and the goals.  Run the code for each asset.  Then download all the contents in the src and make sure to run the classes first before running the the main controller.  Finally the main.py code will launch the game.



## GUI Design

### Initial Design

![initial gui](assets/gui.jpg)

### Final Design

![final gui](assets/gui.jpg)(assets/player1.jpg)(assets/player2.jpg)(assets/ball.jpg)(assets/goal1.jpg)(assets/goal2.jpg)


## Program Design

### Features

1. Movable characters
2. obstacle collisions
3. game over screen
4. score bar on screen
5. end screen with score

### Classes

Player Class- The player class represent a player in the game. In this game there are only two players.  It loads and draws the player's image.  It also handles how the player moves.  

Ball Class- The ball class represents the soccer ball in tha game.  It loads and draws the ball's image.  It keeps track of it's velocity and gandles the physics of the ball.  It also handles how the ball bounces off the walls and slows down.

Goal Class-  Represent the two goals where the players are trying to score.  It loads and draws both goals.  It checks for any collisions with the ball.

Controller Class- This is the main game controller.  It manages the game and handles all interactions between the elements of the game.  It initializes teh game and sets up the display and game clock.  It draws the background, the players, the goals, and the ball  It manages all the states of the game, which are the menu, actual game play, and the game over screen.  It handles all the movement of the players based off the user inputs and manages the collisions between the players and the ball.  It also updates the timer and the scoreboard.  


## ATP
Test 1: Menu Navigation Test Description: Test the navigation through the game's main menu.
| Step                 |Procedure             |Expected Results                   |
|----------------------|:--------------------:|----------------------------------:|
|  1                   | Run Game             |The game should take the user to the menu |
|  2                   | click the space bar   | Game should start up         |

Test 2: Player movement Test Description: Verify that both players can move up, down, left, and right as expected
| Step                 |Procedure             |Expected Results                   |
|----------------------|:--------------------:|----------------------------------:|
|  1                   |Press the W, A, S, D key.|Player 1 should move|
|  2                  |Press the UP, LEFT, DOWN, RIGHT arrow keys |Player 2 should move|


Test 3: Ball Movement and Collision with Players Test Description: Ensure that the ball moves when hit by a player and that collisions between the ball and the players are handled correctly.
| Step                 |Procedure             |Expected Results                   |
|----------------------|:--------------------:|----------------------------------:|
|  1                   |Have player 1 collide with ball |Ball should move forward|
|  2                  |Have player 2 collide with ball |Ball should move forward|

Test 4: Goal reset Condition Test Description: See if the game resets when a goal is scored.
| Step                 |Procedure             |Expected Results                   |
|----------------------|:--------------------:|----------------------------------:|
|  1             |  Have player 1 score with ball |Ball should reset to middle and players sould reset to their initial positions|
|  2                  |Have player 2 score with ball |Ball should reset to middle and players sould reset to their initial positions|

Test 5: Game Over Condition Test Description: See if the game goes to the game over screen with final score
| Step                 |Procedure             |Expected Results                   |
|----------------------|:--------------------:|----------------------------------:|
|  1             |  Have player 1 score with ball |Ball should reset to middle and players sould reset to their initial positions and score board should increase by 1 for player 1|
|  2                  |wait for the end of game| the game over screen should pop up with a 1-0 score