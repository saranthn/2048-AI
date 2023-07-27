<a name="readme-top"></a>
# 2048 Game Solver - Artificial Intelligence

<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-game">About The Game</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
    </li>
    <li><a href="#heuristics">Heuristics</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Game

2048 is played on a 4x4 grid with numbered tiles which can slide up, down, left, or right. This game can be
modeled as a two player game, in which the computer AI generates a 2- or 4-tile placed randomly on the board,
and the player then selects a direction to move the tiles. Note that the tiles move until they either (1) collide with
another tile, or (2) collide with the edge of the grid. If two tiles of the same number collide in a move, they merge
into a single tile valued at the sum of the two originals. The resulting tile cannot merge with another tile again in
the same move.

Usually, each role in a two-player games has a similar set of moves to choose from, and similar objectives (e.g.
chess). In 2048 however, the player roles are inherently asymmetric, as the Computer AI places tiles and the
Player moves them.

I used adversial search techniques and **Expectiminimax** algorithm to develop this game.

![Game](https://github.com/saranthn/2048-AI/blob/main/2048.png)

<p align="right">(<a href="#readme-top">back to top</a>)</p>


### Built With

* ![Python]

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Getting Started

To run the game,

```
python3 GameManager.py
```

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Heuristics

I used alpha-beta pruning and the below heuristics to improve the quality of gameplay.

### Monotonicity
This heuristic tries to ensure that the values of the tiles are all either increasing or decreasing along both the left/right and up/down directions. This heuristic alone captures the intuition that many others have mentioned, that higher valued tiles should be clustered in a corner. It will typically prevent smaller valued tiles from getting orphaned and will keep the board very organized, with smaller tiles cascading in and filling up into the larger tiles.

### Smoothness
This heuristic alone tends to create structures in which adjacent tiles are decreasing in value, but of course in order to merge, adjacent tiles need to be the same value. Therefore, the smoothness heuristic just measures the value difference between neighboring tiles, trying to minimize this count.

A combination of the above heuristics are chosen with the weights being tuned to give the best results.

Reference: https://stackoverflow.com/questions/22342854/what-is-the-optimal-algorithm-for-the-game-2048

<p align="right">(<a href="#readme-top">back to top</a>)</p>

[Python]: https://img.shields.io/badge/Python-14354C?style=for-the-badge&logo=python&logoColor=white
