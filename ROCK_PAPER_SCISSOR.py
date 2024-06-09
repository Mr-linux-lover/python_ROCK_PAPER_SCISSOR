import random as rdm
import sys
def fun_exit():
    exit=input("Do you want to exit(Y/N)?: ").upper()
    if exit.upper() in ['Y', 'YES']:
        print("\t\t\tExit Successful.....")
        sys.exit()
    else:
        print("you can continue the game")
    
item = ['ROCK', 'PAPER', 'SCISSOR']
n=1
print("\t\t WELCOME TO THE ROCK PAPER SICSSOR GAME \n\t\t\t ENJOY THE GAME...")
while n>0:
    print(" PRESS 1 FOR [#]ROCK. \n PRESS 2 FOR [#]PAPER. \n PRESS 3 FOR [#]SCISSOR. \n Select One...")
    choise=(int(input(" :--> ")))
    random_select=rdm.randint(0,2)
    
    if random_select==0 and choise==1:
        print(item[random_select],"vs ROCK")
        print("Game is draw:")
        
    elif random_select==1 and choise==1:
        print(item[random_select],"vs ROCK")
        print("You lose the game")
        fun_exit()
      
    elif random_select==2 and choise==1:
        print(item[random_select],"vs ROCK")
        print("Congruts! You win the game")
        fun_exit()
        
    elif random_select==0 and choise==2:
        print(item[random_select],"vs PAPER")
        print("Congruts! You win the game: ")
        fun_exit()
        
    elif random_select==1 and choise==2:
        print(item[random_select],"vs PAPER")
        print("Game is draw:")
        
    elif random_select==2 and choise==2:
        print(item[random_select],"vs PAPER")
        print("You lose the Game:")
        fun_exit()
        
    elif random_select==0 and choise==3:
        print(item[random_select],"vs SCISSOR")
        print("You lose the game..")
        fun_exit()
        
    elif random_select==1 and choise==3:
        print(item[random_select],"vs SCISSOR")
        print("Congruts! You win the game")
        fun_exit()
        
    elif random_select==2 and choise==3:
        print(item[random_select],"vs SCISSOR")
        print("Game is Draw")
       
        
                
        


        
    
    
    
     