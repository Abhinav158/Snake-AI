# Snake-AI

This is my very first Reinforcement Learning Project. <br>
To create a model using Q Learning, one of the well known techniques under Reinforcement Learning, that would play the popular "Snake Game" and ultimately, complete the game.
<br> <h2> How to play the Game: </h2> 
1. The Snake needs to be directed towards the food (depicted by a red dot) which spawns randomly on the game board. <br>
2. Everytime you eat the food, another one is spawned in a random location and the size of the snake increases. The score is also incremented by 1. <br>
3. The next objective is to direct the snake to eat the food spawned at the new location <br>
4. The game comes to an end when 
 <ul>
  <li> The snake hits any of the borders of the game window  </li>
  <li> The snake encounters itself </li>
 </ul>
  
5. The game is "completed" when there are no free grids left on the game board. <br> 

<h2> Features </h2>
<ul>
 <li> This project implements the use of Python 3.9</li>
 <li> PyTorch is used to implement our neural network </li> 
 <li> We have also plotted the score obtained against the number of games played using matplotlib pyplot library </li>
 </ul>
 
 <h2> Visual Aid </h2>
 ![image](https://user-images.githubusercontent.com/93826081/171136062-87d4e5b5-a7aa-4c02-8487-83117310fbbe.png)
 
 <h2> Stats of the initial training plot </h2> 
 ![image](https://user-images.githubusercontent.com/93826081/171136241-88cdf68a-84a0-4a64-9fa2-a091766f6e86.png)



<br>The same method of learning used in the above project can be used for various other applications like autonomous car driving or an engine for a game like chess. 
