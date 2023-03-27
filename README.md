<a name="readme-top"></a>

[![Contributors][contributors-shield]][]
[![LinkedIn][linkedin-shield]][https://github.com/6abriel1chiro/teeko-intelligent-game/graphs/contributors]

<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/6abriel1chiro/teeko-intelligent-game">
    <img src="./images/logo.jpg" alt="Logo" width="80" height="80">
  </a>

<h3 align="center">teeko intelligent game</h3>

  <p align="center">
    project_description
    <br />
    <a href="https://github.com/6abriel1chiro/teeko-intelligent-game"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/6abriel1chiro/teeko-intelligent-game/issues">Report Bug</a>
    ·
    <a href="https://github.com/6abriel1chiro/teeko-intelligent-game/issues">Request Feature</a>
  </p>
</div>

<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#installation">Installation guide</a></li>
      </ul>
    </li>
    <li><a href="#"></a></li>
  </ol>
</details>

<!-- ABOUT THE PROJECT -->

## About The Project

- The board starts with all the pieces positioned as shown in figure 1.
  • Black always start playing.
  •Each tile can be moved in 8 directions horizontally, vertically or diagonally (N,S,E,W, NE, NO,
  SE,SO) when possible and there is no obstruction. Always move the maximum number of places
  free that you have in that direction.
  • The player who arranges his four chips horizontally, vertically, forming a square or
  positioning their chips in the four corners

- In order for the program to make an "intelligent" decision of where to put its token next it must
  do the following:
  •Define a heuristic that determines the utility value of a state. Explain what is the logic behind
  of your heuristic.
  • Define a maximum height to expand the game tree that will decide how far said game tree should be explored.
  tree. Experiment with different heights and select the one whose average response time is
  < 10s.
  •Implement the algorithm MinMax + α −βpruning and MinMaxWithDepth(cut −off)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

### Built With

Python

<p align="right">(<a href="#readme-top">back to top</a>)</p>
Installation

1. Clone the repository

   ```sh
   git clone https://github.com/6abriel1chiro/teeko-intelligent-game
   ```

2. Install requirements
   ```py
   pip install -r requirements.txt
   ```

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- USAGE EXAMPLES -->

<!-- ROADMAP -->

## Roadmap

- PROBLEM SOLUTION

To program Teeko smart game, we follow the following steps:

- Create the structure of the Teeko board and define the rules of the game, as explained in the statement.
- Create a function that allows the user to choose the color of the tiles they want to play.
- Create a function for the human's turn, where the program will receive the position of the token that the user wants to move and the direction in which they want to move it. This function should also check if the move is valid and, if not, print an error message.
- Create a function for the computer's turn, where the program must decide which token to move and in which direction. To do this, we must implement a search algorithm that allows us to find the best possible move in a game tree.
- Implement a heuristic that determines the utility value of a state. The heuristics must take into account factors such as the position of the pieces on the board and their proximity to the corners and square formation. The logic behind the heuristic should be to maximize the probability of winning the game.
- Define a maximum height to expand the game tree and experiment with different ones until you find the height that allows the program to make decisions in less than 10 seconds.
- Implement the algorithm MinMax + α −β pruning and MinMaxWithDepth(cut −off) to find the best possible move in the game tree.

# define a heuristic that allows us to evaluate the value of a state. To do this, we can consider the following factors:

Corner Distance – Tiles that are closer to the corners have a better chance of forming a square. Therefore, we can assign a higher value to the tiles that are closer to the corners.

Tiles in a Line: If there are three tiles in a line in one direction, the next tile placed there will form a square. Therefore, we can assign a higher value to tiles that are in line with other tiles.

Adjacent Tiles – Tiles that are close together have a better chance of forming a square. Therefore, we can assign a higher value to tiles that are adjacent to other tiles.

Blocked Tokens: If a token is blocked and cannot move in any direction, it is less valuable than a token that can move in multiple directions. Therefore, we can assign a lower value to the locked tokens.

- EXPERIMENTS
- CONCLUSION

<p align="right">(<a href="#readme-top">back to top</a>)</p>
<!-- CONTACT -->

## Contact

Name - [@6abriel1chiro](https://twitter.com/6abriel1chiro) - gabriel.balderrama@ucb.edu.bo

Project Link: [https://github.com/6abriel1chiro/teeko-intelligent-game](https://github.com/6abriel1chiro/teeko-intelligent-game)

<p align="right">(<a href="#readme-top">back to top</a>)</p>
