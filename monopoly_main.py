#import libraries
from colorama import Fore
import sys,time
import random
from splay_tree import *


# typing speed functions for animation
def sprint(str):
   for c in str + '\n':
     sys.stdout.write(c)
     sys.stdout.flush()
     time.sleep(3/ 0.9)

def typewrite(str):
  for letter in str:
    sys.stdout.write(letter)
    sys.stdout.flush()
    time.sleep(0.04)

def rolling(str):
  for letter in str:
    sys.stdout.write(letter)
    sys.stdout.flush()
    time.sleep(0.09)

# function for deleting the rolling dice text animation
def delete_last_line():
  sys.stdout.write('\x1b[1A')
  sys.stdout.write('\x1b[2K')

# title + credit animation 
# typewrite("Welcome to " + Fore.LIGHTGREEN_EX+"Monopoly\n" + Fore.WHITE+"This game was created by " + Fore.BLUE+"haris-hk\n\n")

# list where players are added
players=[]
bankrupt_players = []

win = False

# retrieving all players information and assigning them a color
while not win:
  try:
    numOfPlayers=int(input(Fore.WHITE+"\nHow many players will be playing Dymonopoly today?: "))
    if numOfPlayers>=2 and numOfPlayers<=8:
      if numOfPlayers >=2:
        p1=input(Fore.WHITE+"\nPlayer 1: "+Fore.LIGHTYELLOW_EX)
        players.append(Fore.LIGHTYELLOW_EX+p1)
        p2=input(Fore.WHITE+"\nPlayer 2: "+Fore.CYAN)
        players.append(Fore.CYAN+p2)
      if numOfPlayers >=3:
        p3=input(Fore.WHITE+"\nPlayer 3: "+Fore.RED)
        players.append(Fore.RED+p3)
      if numOfPlayers >=4:
        p4=input(Fore.WHITE+"\nPlayer 4: "+Fore.GREEN)
        players.append(Fore.GREEN+p4)
      if numOfPlayers >=5:
        p5=input(Fore.WHITE+"\nPlayer 5: "+Fore.MAGENTA)
        players.append(Fore.MAGENTA+p5)
      if numOfPlayers >=6:
        p6=input(Fore.WHITE+"\nPlayer 6: "+Fore.WHITE)
        players.append(Fore.WHITE+p6)
      if numOfPlayers >=7:
        p7=input(Fore.WHITE+"\nPlayer 7: "+Fore.BLACK)
        players.append(Fore.BLACK+p7)
      if numOfPlayers ==8:
        p8=input(Fore.WHITE+"\nPlayer 8: "+Fore.YELLOW)
        players.append(Fore.YELLOW+p8)
      break

    # error message for less than 2 players
    elif numOfPlayers < 2:
      print(Fore.RED+"Error occured. You must have atleast two players.")

    # error message for more than 8 players
    else:
      print(Fore.RED+"Error occured. You cannot have than 8 players. ")

  # error message for alternater unintended input
  except:
    print(Fore.RED+"Error occured. Please try again.")

  # 2D board list 
board=[["GO","no"],["Shoreline Pass",60],["Community Chest","cc"],["Trailhawk Lane",60],["Income Tax","no"],["Queens Crown Station",200],["Creighton Plaza",100],["CHANCE","ch"],["Tuscan Road",100],["Dreamville Lane",120],["Just Visiting","no"],["Grand View Mall",140],["Electric Company",150],["Pismo Court",140],["Swanson Avenue",160],["Kanto Station",200],["Morales Street",180],["COMMUNITY CHEST","cc"],["Palace Vinyard",180],["Cynthia Street",200],["Free Parking","no"],["Strand",220],["CHANCE","ch"],["Trojan Road",220],["Tralfamadore Square",240],["Spain Street Station",200],["John London Square",260],["Curry Street",260],["Water Works",150],["Tilted Towers",280],["Go To Jail","no"],["Berkeley Lane",300],["Lombard Street",300],["Community Chest","cc"],["Telegraph Avenue Station",200],["CHANCE","ch"],["Rocky Reels",350],["Super Tax","no"],["Palm Springs",400]]


# showing what is available
available=["GO","Shoreline Pass","Community Chest","Trailhawk Lane","Palm Springs","Income Tax","Queens Crown Station","Creighton Plaza","CHANCE","Tuscan Road","Dreamville Lane","Just Visiting","Grand View Mall","Electric Company","Pismo Court","Swanson Avenue","Kanto Station","Morales Street","COMMUNITY CHEST","Palace Vinyard","Cynthia Street","Free Parking","Strand","CHANCE","Trojan Road","Tralfamadore Square","Spain Street Station","John London Square","Curry Street","Water Works","Tilted Towers","Go To Jail","Berkeley Lane","Lombard Street","Telegraph Avenue Station","Rocky Reels", "CHANCE"]

# each players starting board position 
bPos=[0,0,0,0,0,0,0,0]

# each players portfolio
own=[[],[],[],[],[],[],[],[]]

# balance of each player
money=[1500,1500,1500,1500,1500,1500,1500,1500]


iterations = 0
# starting dice roll and sending current player to their rolled position
while not win:
  jail = False
  # iterations += 1

  if iterations % numOfPlayers == 0 and iterations != 0 :
    print(Fore.WHITE+"\nPrice Update: \n")
    print(Fore.GREEN+"Increase in property value for the following: \n")
    tree.increase_visited()
    print(Fore.LIGHTRED_EX+"\nDecrease in property value for the following: \n")
    tree.decrease_visited()
  for x in range(numOfPlayers):
    if x in bankrupt_players:
      continue
    
    # os.system("clear")
    input(Fore.WHITE+"\nClick <ENTER> to begin your go... ")
    if jail == False:
      bPos[x]=random.randint(1,6)+random.randint(1,6)+bPos[x]
    else:
      bPos[x] = bPos[x]
    if bPos[x] >= 39:
      bPos[x]=bPos[x]-39
    # os.system("clear")

      
    # rolling dice animation text
    rolling("Rolling Dice...")
    time.sleep(1)
    delete_last_line()
    print()
    
  #resetting color so that "Player:" will match players color
    print(players[x])
    time.sleep(0)
    delete_last_line()

    # header stats (player , balance, board position)
    # print("\nPlayer" + ":",players[x])
    # print("Balance: $",money[x])
    # print("You landed on",board[bPos[x]][0])
    
    jail_time = 0
      # if player lands on a space with board position index[1] == "no" (go to jail, free parking, etc)
    if board[bPos[x]][0]=="Income Tax":
      print("\nPlayer" + ":",players[x], "landed on",board[bPos[x]][0])
      money[x]=money[x]-200
      print("\nYou paid $200 in income tax.\nYour new balance is $" + str(money[x]))
    elif board[bPos[x]][0]=="Super Tax":
      print("\nPlayer" + ":",players[x], "landed on",board[bPos[x]][0])
      money[x]=money[x]-400 
      print("\nYou paid $400 in Super tax.\nYour new balance is $" + str(money[x]))
    elif board[bPos[x]][0]=="GO":
      print("You passed GO! Collect $200!")
      money[x]=money[x]+200
      print("\nYour new balance is $" + str(money[x]))
    elif board[bPos[x]][0]=="Go To Jail" and "Get out of Jail Free Card" not in own[x]:
      jail = True
      print("\nYou have been sent to jail!")
      while jail_time < 4:
        print("\nYou are in jail for " + str(3 - jail_time) + " turns.")
        print("\nYou can either pay $100 to get out of jail or wait for your turn.")
        print("\nWhat would you like to do?\n(1)Pay $100\n(2)Wait")
        jail_choice = int(input(">> "))
        if jail_choice == 1:
          money[x] = money[x] - 100
          print("\nYou paid $100 to get out of jail.\nYour new balance is $" + str(money[x]))
          jail = False
          break
        elif jail_time == 3:
          print("You have served your time in jail. You are free to go.")
          jail = False
          break
        elif jail_choice == 2 and jail_time < 2:
          jail_time += 1
          print("\nYou are still in jail.")
          jail = True
          break


      # checks to see if the property the player landed on is available, and then to see if that player owns it. If they don't rent is subtracted fromt that players balance.
    if board[bPos[x]][0] not in available: 
      if board[bPos[x]][0] not in own[x]:
        rent_owed = tree.search(board[bPos[x]][0]).value 
        if rent_owed not in ["cc", "no", "ch", None]:
          money[x] = money[x] - rent_owed
        for i in range(len(own)):
          if board[bPos[x]][0] in own[i]:
            money[i] = money[i] + rent_owed
        print("\nUnfortunately",board[bPos[x]][0] + " is owned by another player. You paid $" + str(rent_owed) + " in rent.\nYour new balance is $" + str(money[x]))
      else: 
         print("\nYou own this property!")

    # outcomes for landing on community chest
    elif board[bPos[x]][1]=="cc":
      print("\nPlayer" + ":",players[x], "landed on",board[bPos[x]][0])
      cc_spin = random.randint(1,5)
      
      if cc_spin == 1:
        money[x]=money[x] + 100
        print("\n You won $100 from the community sweepstakes! Maybe sometimes these do work...\n Your new balance is $" + str(money[x]))
        
      elif cc_spin == 2:
        money[x]=money[x] + 200
        print("\nYou received $200 for your birthday! Your grandma tells you not to spend it on alcohol.\n Your new balance is $" + str(money[x]))
        
      elif cc_spin == 3:
        print("\n You received Get Out of Jail Free Card! You can use this card to get out of jail for free.")
        own[x].append("Get out of Jail Free Card")
          
      elif cc_spin == 4:
        money[x]=money[x] + 500
        print("\n You won the national hot dog eating contest and won $500! Hope that'll cover your toilet repairs...\n Your new balance is $" + str(money[x]))
        
      elif cc_spin == 5:
        money[x]=money[x] + 50
        print("\n You won Thursday bingo and were awarded $50. In other news the senior citizens have been plotting your kidnapping.\n Your new balance is $ " + str(money[x]))
        

    # outcomes for landing on chance
    elif board[bPos[x]][1]=="ch":
      print("\n Player" + ":",players[x], "landed on",board[bPos[x]][0])
      ch_spin = random.randint(1,5)

      if ch_spin == 1:
        money[x]=money[x] - 35
        print("\n You were fined $35 dollars for speeding. Wait till your insurance hears about this.\nYour new balance is $" + str(money[x]))

      if ch_spin == 2:
        money[x]=money[x] - 150
        print("\nYou lost $150 gambling in Vegas. This better be a one time thing...\nYour new balance is $" + str(money[x]))

      if ch_spin == 3:
        money[x] = money[x] - 100
        print("You just sent $100 to the Prince of Nigeria. I can't believe you fell for that.\nYour new balance is $" + str(money[x]))

      if ch_spin == 4:
        money[x] = money[x] + 100
        print("You discovered BitCoin mining! You mined 0.000023 BTC which is worth about $100!\nYour new balance is $" + str(money[x]))

      if ch_spin == 5:
        ch_lottery = random.randint(1,1000) 
        if ch_lottery < 1:
          lottery = 0

        money[x] = money[x] + ch_lottery
        print("\nYou just won $" + str(ch_lottery) + " playing blackjack. This is improbable, I can't believe it..\nYour new balance is $" + str(money[x]))
        
      # print("\nwhat would you like to do?\n(1)Buying is unavailable here!\n(2)Morgage(CURRENTLY UNAVAILABLE)\n(3)Check properties\n(4)End turn")

    # landing on an unowned property 
    else:
      pass
      # player inputs what they want to do during their turn
     
    choice = 0
    iterations += 1  
        
    while choice != 4:   
      print("\nPlayer" + ":",players[x])
      print("Balance: $",money[x])
      print("You landed on",tree.search(board[bPos[x]][0]).key)
      time.sleep(1)
      if board[bPos[x]][1]=="no":
                print("\nwhat would you like to do?\n(1)Buying is unavailable here!\n(2)Sell for $\n(3)Check properties\n(4)End turn")
      elif board[bPos[x]][1]=="cc":
                print("\nwhat would you like to do?\n(1)Buying is unavailable here!\n(2)Sell for $\n(3)Check properties\n(4)End turn")
      elif board[bPos[x]][1]=="ch":
                print("\nwhat would you like to do?\n(1)Buying is unavailable here!\n(2)Sell for $\n(3)Check properties\n(4)End turn")
      elif board[bPos[x]][0] not in available:
                print("\nwhat would you like to do?\n(1)Buying is unavailable here!\n(2)Sell for $\n(3)Check properties\n(4)End turn")         
      else :
                print("\nwhat would you like to do?\n(1)Buy for $",tree.search(board[bPos[x]][0]).value,"\n(2)Sell for $\n(3)Check properties\n(4)End turn")
      while True:
        try:
          wyd=int(input(">> "))
          break
        # if input is invalid
        except:
          print("\nERROR! TRY AGAIN")
   
      # message for trying to buy a position that isn't a property 
      if wyd==1:
        if board[bPos[x]][1] == "no":
          print("\nThis cannot be bought!")

        # message for trying to buy another players property
        elif board[bPos[x]][0] not in available:
          print()
          print("\nThis property is currently owned by another player!")

        # if the property is unowned and less than your balance, player can purchase the property
        else:
          if money[x] >= tree.search(board[bPos[x]][0]).value:
            money[x]=money[x]-tree.search(board[bPos[x]][0]).value
            own[x].append(board[bPos[x]][0])
            available.remove(board[bPos[x]][0])
            print("\nCongratulations! You bought",board[bPos[x]][0])
          # message for if players balance is less than the property cost
          else:
            print("\nUh oh! You can't afford this!")

      # mortgage option for a property (not yet operational)
      elif wyd==2:
      # implementing Sell for $ option
        if len(own[x]) == 0:
          print("\nYou don't have any properties to sell.")
          continue
        else:
          print("\nKindly select the number of the property you would like to sell? ")
          for i in range (len(own[x])):
            if own[x][i] != "Get out of Jail Free Card":
              print(str([i+1]) , str(own[x][i]), str(tree.search(own[x][i]).value)) #TODO: Traverse to find value instead of searching
            else:
              continue
          if "Get out of Jail Free Card" in own[x]:
            print(str([len(own[x])]), "Get out of Jail Free Card" , str(200))
          
          print(str([-1]), "Exit")
          property_index = int(input(">> "))

          if property_index == -1:
            continue
          elif property_index == len(own[x]):
            money[x] = money[x] + 200
            own[x].remove("Get out of Jail Free Card")
            print("You have successfully sold Get out of Jail Free Card for $200")
            continue
          else:
            property_index = abs(property_index - 1)


        # if the property is not in the players portfolio
          while own[x][property_index] not in own[x]:
            print("\nThis property is not in your portfolio. Please select a property from your portfolio.")
            property_index = int(input(">> "))
          property_to_be_sold = own[x][property_index]
        # if the property is in the players portfolio
        # Selling the property and adding the money to the players balance
          for j in range(len(board)):
            if property_to_be_sold == board[j][0]:
              money[x] = money[x] + board[j][1]
              own[x].remove(property_to_be_sold)
              available.append(property_to_be_sold)
              # printing a statement to confirm the sale of the property
              print("You have successfully sold", property_to_be_sold, "for $", board[j][1])
              break
             
        
        


      # checking real estate portfolio option 
      elif wyd==3:
        print("\nYou real estate portfolio includes: ",own[x])

      # function for ending turn
      else:
        choice = 4
        print("\nEnding turn...")
        break
          
        
    if money[x] < 1:
      bankrupt_players.append(x)
      print()
      print(str(players[x]) + Fore.RED +  " has gone bankrupt! You lose.")
      if numOfPlayers - len(bankrupt_players) == 1:
        find = [player for player in range(numOfPlayers) if player not in bankrupt_players]
        find = find[0]
        print()
        print(str(players[find]) + Fore.MAGENTA+ " Has won the game! Congratulations!!!")
        print()
        print(Fore.WHITE+"Thank you for playing Dymonopoly!")
        print()
        win = True
  # checks for if a players balance is less than $1. If it is, then the other player is awarded the win

      # continuing a turn after an action
      # else:
      
      #   print("Unavailable!")
      # input("<ENTER> to continue...")
      # if os.system('clear'):
      #   break
          

