<p align="center"><img src ="images/traditional-bingo.png" /></p>

### What is traditional Bingo?
In the United States, Bingo is a game of chance in which each player matches numbers pre-printed in different arrangements on 5×5 cards with the numbers the game host draws at random, marking the selected numbers with tiles. When a player finds the selected numbers are arranged on their card in a row, they call out "Bingo!" to alert all participants to a winning card, which prompts the game host (or an associate assisting the host) to examine the card for verification of the win. Players compete against one another to be the first to have a winning arrangement for the prize or jackpot. After a winner is declared, the players clear their number cards of the tiles and the game host begins a new round of play. (Source - [Wikipedia](https://en.wikipedia.org/wiki/Bingo_(U.S.)))
### Lets define custom Bingo :smiley:
Here we are going to define bingo in a bit different way. We will play bingo as follows:
- Every player who is playing bingo comes up with a **3 x 3 matrix** of his own choice ranging from numbers **1 to 20** (both inclusive). You may use the same integer **more than once**.
- We will mark one square on your bingo board if you have **at least one unmarked square** that is a multiple of the total rolled (if more than one unmarked square is a multiple of the total, we will pick one at random).
- We will take turns until at least one board has bingo (3 marks in a row, horizontal, vertical, or diagonal).
- Each player whose board has bingo gets a share of the win (if n players get bingo, then each gets 1/n wins).
- We will simulate 10,000 games (you can select some other number of your choice) using all the bingo boards submitted. The goal is to get the **most wins out of all contestants**.

### Simulating the game
- You will find two folders in the bingo repository namely images and notebooks. The [images]() folder has images which are intermediately used in the explanation in one of the ipython notebooks. The notebooks folder contains two ipython notebooks namely bingo.ipynb, play_bingo.ipynb and a bingo.py python script.
- You shall notice that we are using the bingo.py file as module in play_bingo.ipynb. The bingo.py is a simple python script as opposed to the bingo.ipynb which is a jupyter notebook. We converted the file to simple python script so that we could use it as a module in the play_bingo.ipynb file.
- bingo.ipynb conatins all the neccessary helper functions needed to simulate the game. I highly encourage you to look at the source code to have an better understanding of how the game is coded.
- play_bingo.ipynb is the file which can directly simulate the game without knowing anything about the helper functions in the bingo.ipynb file. Please follow the instruction and read the description in the begining of the play_bingo.ipynb file to follow along.

    													
													
																								
													
													
