
# coding: utf-8

# In[76]:

# importing the required libraries
import numpy as np
import random


# In[84]:

# function to get the sum of the dices assuming the dices are fair and unbaised
def roll_dices():
    '''
     returns : sum of the two dices which are rolled.
    '''
    dice1 = np.random.randint(1,7)
    dice2 = np.random.randint(1,7)
    return dice1 + dice2


# In[83]:

# function to initialize the players with their choice of bingo boxes also facilitating 
# to add random number of players and number of games to be played.

def initialize_array(players_dic,random_player_size=3,game_size=1):
    
    '''
        arguments : players_dic         ===> dictionary of players of choice with key and value pairs
                
                    random_player_size  ===> number of random players to be added
                
                    game_size           ===> number of games to be played
                
          returns : dic                 ===> python dictionary containing all the players in the game 
    '''
    
    random_players = np.random.randint(2,21,(random_player_size,3,3))
    dic = {}
    for num in range(random_player_size):
        dic['Player '+ str(num)] = {'Box' : random_players[num],  
                                    'Bingo Value' : np.zeros(game_size)}
        
    for player in players_dic:
        dic[player] = {'Box' : players_dic[player], 
                       'Bingo Value' : np.zeros(game_size)}
    
    return dic


# In[85]:

# function to obtain which box should be marked in the case there are multiples

def get_box_to_be_marked(sum_of_dices,my_array):
    
    '''
        arguments : sum_of_dices       ===> sum of dices returned from the roll_dices() function
    
                    my_array           ===> bingo box which is being currently marked
                 
          returns : index_to_be_marked ===> location of the index to be marked or -1
       
                    True, False        ===> status indicator if index to be marked exists
    '''
    
    array_of_multiples = np.asarray(np.where(my_array%sum_of_dices == 0)).T
    if len(array_of_multiples) > 0:
        index_to_be_marked = random.choice(array_of_multiples)
        return index_to_be_marked,True
    else:
        return -1,False


# In[86]:

# function to mark the box

def mark_box(my_array,index_to_be_marked):
    
    '''
        arguments : my_array           ===> bingo box to be marked
        
                    index_to_be_marked ===> location of the index to be marked
                    
          returns : my_array           ===> bingo box after being marked
    '''
    
    my_array[index_to_be_marked[0],index_to_be_marked[1]] = -1
    return my_array


# In[87]:

# function that simulates a single game

def start_game(players_dic,game_no):
    
    '''
        arguments : players_dic ===> dictionary containing all the players in the game
        
                    game_no     ===> number of game being played
                    
          returns : players_dic ===> dictionary containing all the players in the game with modified variables
          
    '''
    
    temp_player_box = {player : players_dic[player]['Box'].copy() for player in players_dic}
    flag = True
    count = 0
    no_of_winners = 0
    while flag:
        count+=1
        sum_of_dices = roll_dices()
        for player in temp_player_box:
            index_to_be_marked, boolean = get_box_to_be_marked(sum_of_dices,temp_player_box[player])
            if boolean:
                box = mark_box(temp_player_box[player],index_to_be_marked)
                if count > 2:
                    if bingo(box):
                        no_of_winners+=1
                        players_dic[player]['Bingo Value'][game_no] = 1
                        flag = False
                        
    distribute_wins(players_dic,game_no,no_of_winners)
    return players_dic


# In[89]:

# function to normalize wins among all the winners in a single bingo game

def distribute_wins(players_dic,game_no,no_of_winners):
    
    '''
        arguments : players_dic   ===> dictionary containing all the players in the game
        
                    game_no       ===> number of game being played
                    
                    no_of_winners ===> number of winners in the game being played
    '''
    
    for player in players_dic:
        players_dic[player]["Bingo Value"][game_no] = players_dic[player]["Bingo Value"][game_no]/no_of_winners


# In[90]:

# function to determine the winner

def winner(players_dic):
    
    '''
        arguments : players_dic   ===> dictionary containing all the players in the game
        
          returns : winner_dic    ===> dictionary of the winner with the number of wins
    '''
    
    max_wins = 0
    winner_dic = {}
    for player in players_dic:
        bingo_value = players_dic[player]["Bingo Value"].sum()
        if max_wins < bingo_value:
            max_wins = bingo_value
            winner_dic["max_wins"] = max_wins
            winner_dic["Winner"]   = {player : players_dic[player]}
            
    return winner_dic


# In[92]:

# function to determine if its a bingo

def bingo(my_array):
    
    '''
        arguments : my_array    ===> bingo box to be determine if its a bingo
        
          returns : True, False ===> boolean stating if its a bingo
    '''
    
    secondary_diagonal = my_array[[2,1,0],[0,1,2]].sum()
    if secondary_diagonal == -3:
        return True
    elif my_array.diagonal().sum() == -3:
        return True
    else:
        for i in range(3):
            if my_array[i,:].sum() == -3:
                return True
            elif my_array[:,i].sum() == -3:
                return True
    return False


# In[93]:

# function to simulate game with the given number of times with custom players

def simulate_game(players_dic,random_player_size=3,game_size=1):
    
    '''
        arguments : players_dic         ===> dictionary of players of choice with key and value pairs
                
                    random_player_size  ===> number of random players to be added, by default players = 3
                
                    game_size           ===> number of games to be played, by default size = 1
                    
          returns : players_dic         ===> dictionary of all players in the game with their scores
          
                    winner              ===> dictionary of the winner with total wins
    '''
    
    players_dic = initialize_array(players_dic,random_player_size,game_size)
    for i in range(game_size):
        players_dic = start_game(players_dic,i)
    
    return players_dic, winner(players_dic)


# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:



