# Snake-AI

This is my very first Reinforcement Learning Project. <br>
To create a model using Q Learning, one of the well known techniques under Reinforcement Learning, that learn how to play the popular "Snake Game" and ultimately, complete the game by occupying all availble grids on the gameboard.

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
 <li> This project makes use of Python 3.9</li>
 <li> We use PyGame to implement our gane design </li>
 <li> We use PyTorch to implement our neural network </li> 
 <li> We have also plotted the score obtained in each game against the number of games played using matplotlib library </li>
 </ul>
 
 
<h3> Brief Theory: </h3> 
Reinforcement learning develops control patterns by providing feedback on a model’s selected actions, which encourages the model to select better actions in the future. At each time step, given some state s, the model will select an action a, and then observe the new state s' and a reward r based on some optimality criterion.
We specifically used a method known as Q learning, which approximates the maximum expected return for performing an action at a given state using an action-value (Q) function. Specifically, return gives the sum of the rewards until the game terminates, where the reward is discounted by a factor of γ at each time step.

```
var add2 = function(number) {
  return number + 2;
}
```
<h3>How to set up the project on your local system </h3>
<ol>
 <li> Download Anaconda to set up virtual environment to install all required dependencies </li>
 <li> Once conda is set up (type `conda --version` to confirm), set up your virtual environment </li>
 `conda create -n pygame_env python=3.9` <br>
 `conda activate pygame_env` 
  <li> Install require packages </li>
 `pip install pygame` <br>
 `pip install matplotlib ipython` <br>
 Install pytorch based on your system requirements using 
 https://pytorch.org/get-started/locally/ to start locally  <br>
 Now you have everything you need to implement the project!
 
 <li>Download all files from github repository into your local system </li>
 
 <li> In your terminal, inside the virtual environment, type python agent.py</li>
 You are all set! Watch the AI learn how to play the Snake Game! 
  
<h3>Applications of Reinforcement Learning</h3> 
<ol> 
 <li>Robotics for Industrial Automation </li>
 <li>Text summarization engines</li> 
 <li> Autonomous Self Driving Cars </li>
 <li> AI Toolkits, Manufacturing, Automotive, Healthcare </li>
 <li>Aircraft Control and Robot Motion Control </li>
 <li> AI for Computer Games </li>
</ol>


 
