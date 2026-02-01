import random      #Used to generate random numbers

#Welcome
print ("WELCOME TO")
print ("          B")
print ("          U")
print ("          N")
print ("          C")
print ("          O")


#Displaying rules of the game
rules=input('\n Do you wish to view the rules of the game?(y/n) : ')
if rules=='y':
    print ("\n(01).\t The maximum number of players are 6")
    print ("(02).\t All players have been assigned with an unique player number")
    print ("(03).\t Each player can roll the dice 6 times")
    print ("(04).\t To obtain a point a player should roll the dice and get the same number corresponding to his player number")
    print ("\n .....................An Example is provided below...................")
    print ("\nPlayer 2 should roll the dice and obtain number 2 to score a point")
    print ("The first player to obtain the highest score wins the game")
    print ("\n ....................G O O D  L U C K....................")

elif rules=="n":
    print ("\n Lets play the game!")
    print ("\n ....................G O O D  L U C K....................")

#Obtaining the player count and defining variables
def players ():
    valid_no_of_players = "V" #Variable to store the player information
    while valid_no_of_players == "V": #For looping
        no_of_players = int(input("\n Enter the number of players (Max:6) : "))

        if no_of_players < 2 or no_of_players > 6: #Restricting players between 1 and 6
            print ("\n Please enter the number of players between 2 and 6 ") #Error message displayed for invalid player input
            valid_no_of_players = "V" #Looping again
        else:
            valid_no_of_players= "W" #Getting out of the loop
    return no_of_players
    

#Rolling the dice for each player
def initial_score ():
    for player in range (0,no_of_players+1): #Adding each players score into score list
        score.append(0) #Default scores for each player is 0

#Rolling the dice
def dice_roll ():
    for player in range (0,no_of_players):
        print('\n Player ', str(player+1), "'s turn")

        count = 1
        for number in range(1, 7):    
            random_number = random.randint(1,6)
            print('For dice rolling ', str(count), ' you got: ', str(random_number))
            count +=1

            if random_number == player+1:
                score[player] = score[player] +1
        print ("The score is",score)
          

# to reroll dice (if player wants).
        def rerolling_the_dice():
            reroll = input("\n\tDo you want to reroll the dices. Enter 'Y' for YES or 'N' for NO: ")# Letting the player decide whether to reroll the dice or not.

            if reroll.upper() == 'Y': 
                number2 = int(input('\tEnter how many dice you want to reroll(max = 5): '))

                if number2 > 5 or number2 < 1: #Checking the validity of the input     
                    print('Invalid input. You can roll a maximum of 5 die and minimum of 1 dice only.') 
                    recall=rerolling_the_dice() #recalling the initial function again
                # else the condition is true    
                else: 
                    count = 1
                    for number in range(0, number2): 
                        random_number2 = random.randint(1,6) #random_number2 stores the random number generated 
                        print('For dice rolling ', str(count), ' you got: ', str(random_number2)) 
                        count+=1

                        #Adding points to their score list
                        if random_number2 == player+1:
                            score[player] = score[player] + 1

                    
        rerolling_the_dice()
        print('Your (', 'Player ', str(player+1), ') score is: ', str(score[player])) #Displaying individual scores after rolling the dice
        print('\nThe total score is: ',score) #Displaying new score
        
#Determining the winner

def round_winner(score):
    winner = score.index(max(score)) 
    
    if score[winner] == 0: 
        return [] 
        
    else:
        return winner 
    
#Central Program
    
play = 'Y' #Creating a variable as play

while play.upper() == 'Y': # while play = 'Y' below functions are executed.
    no_of_players = players() 
    score=[] #Score list
    initial_score() 
    dice_roll() 
    winner = round_winner(score) # make a variable as winner and call find_winner function inside it to store.
    if winner == []: 
        print('\nNo WINNER in this round') # displaying no winner message if winner list is empty.
        
        
    else:
        print('\nCONGRATULATIONS!!!') 
        print('Player ',str(winner+1), ' reached the highest score first!!' ) #Displaying winner
        print('Therefore, player ',str(winner+1), ' is the WINNER of this round' )  

    play=input('\nDO YOU WISH TO PLAY AGAIN? (Enter "Y" for Yes and "N" for No) : ') #Option for players to replay or not

    if play.upper() == 'N':
        play = 'N'
        print('\nThank you for playing Bunco! Hope to see you again!') #Ending note

#Saving the results into a text file         
file=open('scores.txt', 'a+')
winner=round_winner(score)
file.write("The winner is : Player "+str(winner+1)+"\n")
file.close()

  






    
