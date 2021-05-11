# minicasino

This program is a terminal based casino game.

### Commands

* The program must be run as follows:
  ```
  ./minicasino.py
  ```
* Quit the game with command CTRL + C

### Description

* The program uses a json list to save the players' profiles.
  Lastname.Firstname
  gender = player's gender
  lang = default language
  money = current total amount of money
  rec_money = record total amount of money
  rec_start_money = start money when rec_money was reached
  time = total amount of time the player has played
  visits = number of times the player has played
* The "Mini.Casino" player represents the casino itself. When it loses/wins the game it does not change the amount of its money.
* The player interacts with the Croupier during the whole game.

### Errors

* Entering unwanted data multiple times can lead to an expulsion by the Croupier.

<p align="center">
  <img src="/screenshots/board.png" width="60%" />
  <img src="/screenshots/results.png" width="60%" />
  <img src="/screenshots/json.png" width="40%" />
</p>
