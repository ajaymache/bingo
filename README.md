### What is traditional Bingo?
In the United States, Bingo is a game of chance in which each player matches numbers pre-printed in different arrangements on 5×5 cards with the numbers the game host draws at random, marking the selected numbers with tiles. When a player finds the selected numbers are arranged on their card in a row, they call out "Bingo!" to alert all participants to a winning card, which prompts the game host (or an associate assisting the host) to examine the card for verification of the win. Players compete against one another to be the first to have a winning arrangement for the prize or jackpot. After a winner is declared, the players clear their number cards of the tiles and the game host begins a new round of play. (Source - [Wikipedia](https://en.wikipedia.org/wiki/Bingo_(U.S.)))
### Lets define custom Bingo :smiley:
Here we are going to define bingo in a bit different way. We will play bingo as follows:
- Every player who is playing bingo comes up with a 3 X 3 matrix of his own choice ranging from numbers 1 to 20 (both inclusive). You may use the same integer more than once.
- We will mark one square on your bingo board if you have at least one unmarked square that is a multiple of the total rolled (if more than one unmarked square is a multiple of the total, we will pick one at random).
- We will take turns until at least one board has bingo (3 marks in a row, horizontal, vertical, or diagonal).
- Each player whose board has bingo gets a share of the win (if n players get bingo, then each gets 1/n wins).
- We will simulate 10,000 games using all the bingo boards submitted. The goal is to get the most wins out of all contestants.
    													
													
													

Submit your answer as an integer vector of length 9 - where the first element is placed in the top left box on the bingo board and then reading left to right across the top row and then left to right across the middle row and then left to right across the bottom row. Also submit a very brief description of how you arrived at your answer and why you think your board will win.  We are interested in your thought process and how you considered different angles to the game as much as how well your submission does compared with other contestants.													
													
													
