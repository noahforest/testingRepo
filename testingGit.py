import random, time, copy

'''
noah forest
Black Jack 
5/15/17
'''


class engine(object):
	def __init__(self, startScene): #takes in startscene which is the first scene it opens
		self.startScene = startScene
	def play(self):
		currentScene = self.startScene
		while currentScene != "quit":
			currentScene = currentScene.enter()
			
'''
Engine Class Ended.
'''

class scene(object):
	def __init__(self):
		pass
	def enter(self):
		print("test")

'''
Scene Class Ended.
'''

class exitScene(scene):
	def enter(self):
		print("Quitting...")
		return "quit"

'''
Exiting Scene Class Ended.
'''

#class other(object):
	#def clear():          commented out for now
		#print("\n"*75)

class settings(object):
	def __init__(self): #initializes settings
		self.file = open("/Users/nforest/Desktop/settings.txt", "r")
		self.settings = eval(self.file.read())
		self.file.close()
	def save(self):
		self.file = open("/Users/nforest/Desktop/settings.txt", "w")
		self.file.write(str(self.settings))
		self.file.close()

'''
Settings Class Ended.
'''

class settingsScene(scene):
	def __init__(self):
		pass
	def enter(self):
		settings.save()
		print("\n"*75)
		print("Current Settings")
		print("Type in the number to change the setting.")
		print("1. Currency: %s" % settings.settings["currency"])
		print("2. Number of Decks: %s" % settings.settings["deckSize"])
		print("3. Return to Main Menu")
		while True:
			action = input("Enter the number >> ")
			if action in [str(i) for i in range(1,4)]:
				print('\n'*75)
				if action == "1":
					settings.settings["currency"] = input("What would you like the currency name to be >> ")
					return settingsScene()
				elif action == "2":
					settings.settings["deckSize"] = input("How many decks would you like to use >> ")
					return settingsScene()
				elif action == "3":
					return mainMenu()
		
'''
Settings Scene Class Ended.
'''
	
class mainMenu(scene):
	def __init__(self):
		pass
	def enter(self):
		print('\n'*75)
		print(" _     _            _    _            _     ")
		print("| |   | |          | |  (_)          | |    ")
		print("| |__ | | __ _  ___| | ___  __ _  ___| | __ ")
		print("| '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ / ")
		print("| |_) | | (_| | (__|   <| | (_| | (__|   <  ")
		print("|_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\ ")
		print("                       _/ |                 ")
		print("                      |__/                \n")
		print("1. Start Game")
		print("2. Settings")
		print("3. Rules")
		print("4. Exit")
		while True:
			action = input("Please enter the number of the action >> ")
			if action in [str(i) for i in range(1,5)]: #used a for loop because input takes string and i dont want to add extra code to check if its an int
				print('\n'*75)
				if action == "1":
				  startGame()
				  game()
				elif action == "2":
					return settingsScene()
				elif action == "3":
					return rules()
				elif action == "4":
					return exitScene()
				break
			else:
				print("That is not a valid choice.")

'''
Main Menu Class Ended.
'''

class rules(scene):
	def __init__(self):
		self.houseRules = ["Dealer/House Rules", "    Hits when hand is under 17.","    Hits on soft 17 (When dealer has 6 and Ace).","    If dealer's hand is over 21, dealer busts and players win their bets.","    With a tie (push), players get their bets back."]
		self.playerRules = ["Player Rules","    Hit: Take another card.","    Stand: Stop taking cards.","    Double down: Double bet and hit once.","    Split: Double bet and separate hand into two equal hands.","    Surrender: Allows player to forfeit their hand. Must be done at the start."]
	def enter(self):
		print('\n'*75)
		print("RULES CATEGORIES:")
		print("1. Dealer/House Rules")
		print("2. Player Rules")
		print("3. Exit to main menu")
		while True:
			action = input("Please enter the category number >> ")
			if action in [str(i) for i in range(1,3)]: 
				getRule = {"1":self.houseRules,"2":self.playerRules}[action]
				print('\n'*75)
				print("\n".join(getRule))
				filler = input("Press enter to go back.")
				return rules()
			elif action == "3":
				return mainMenu()

class decoration:
  FLASH = '\033[37;5m' # white
  FLASHR = '\033[36;5m' # red
  END = '\033[0m' #resets format
  BOLD = '\033[1m' #universal
  ITALICIZE = '\033[3m' #universal
  BLUE = "\033[1;34m"
  RED = "\033[1;31m"

cardNumb = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]

cardValues = {"A" : 1, "2" : 2, "3" : 3, "4" : 4, "5" : 5, "6" : 6, "7" : 7, "8" : 8, "9" : 9, "10" : 10, "J": 10, "Q" : 10, "K" : 10}

cardSuits = ["♥", "♦", "♣", "♠"]

CARD_ASCII = '''┌─────────┐
│ {}       │
│         │
│         │
│    {}    │
│         │
│         │
│       {} │
└─────────┘'''
CARD_ASCII = '''\
┌─────┐
│ {}  │
│  {}  │
│  {} │
└─────┘'''

HIDDEN_CARD = """\
┌─────┐
│░░░░░│
│░░░░░│
│░░░░░│
└─────┘
"""

hand = []

def print_slow(str):
    for letter in str:
        print(letter, end='')
        time.sleep(.05)

def print_slower(str):
    for letter in str:
        print(letter, end='')
        if letter != " ":
          time.sleep(1)
        
def clear():
  print('\n'*50)
  
def clearLess():
  print('\n'*5)

def beginGame():
  begin = input("Are you ready to begin? (y/n) : ").lower()
  started = False
  if input == 'y':
    started = True
  elif begin == 'n':
    beginGame()
  else: 
    while begin != 'y' and begin != 'n':
      print ("Please input either y or n")
      beginGame()

def fidgetspin(cardList):
  for index in range(0, 5):
    print("| ", end="")
    for cardGroups in cardList:
      for card in cardGroups:
        print(card.cardText.split('\n')[index], end="")
      print(" | ", end="")
    print("")

def singleListPrintCards(cardList):
  for index in range(0, 5):
    for card in cardList:
      print(card.cardText.split('\n')[index], end="")
    print("")

def printAllBets(bets):
  print("|  ", end="")
  cardsList = []
  for better in bets:
    for betObj in bets[better]:
      print( (" "*(len(betObj.cards)*7)).replace(" "*len(better + "'s bet"), better + "'s bet", 1), end="|  ")
      cardsList.append(betObj.cards)
  print("")
  
  fidgetspin(cardsList)
  
  print("|  ", end="")
  for better in bets:
    for betObj in bets[better]:
      print( (" "*(len(betObj.cards)*7)).replace(" "*len("Total : " + str(cardSum(betObj.cards))), "Total : " + str(cardSum(betObj.cards)), 1), end="|  ")
  print("")
  
  print("|  ", end="")
  for better in bets:
    for betObj in bets[better]:
      print( (" "*(len(betObj.cards)*7)).replace(" "*len(str(betObj.amount) + " " + settings.settings["currency"]), str(betObj.amount) + " " + settings.settings["currency"], 1), end="|  ")
  print("")

def isNumber(numb): #checking to see if the parameter is a number
  try:
    int(numb)
    return True
  except ValueError:
    return False

def cardSum(cardsList):
  cardSum = 0
  for card in cardsList:
    cardSum += clamp(card.value, 1, 11)
  return cardSum

def clamp(numb, mini, maxi):
  return max(min(numb, maxi), mini)

def getOptions(bet):
  cardsList = bet.cards
  sumOfCards = cardSum(cardsList)
  listOfOptions = []
  if sumOfCards == 21:
    listOfOptions.append("21")
  elif sumOfCards > 21:
    listOfOptions.append("Bust")
  else:
    listOfOptions.append("Stand")
    listOfOptions.append("Hit")
  if bet.amount <= bet.player.dongs and len(cardsList) == 2 and clamp(cardsList[0].number, 0, 10) == clamp(cardsList[1].number, 0, 10):
    listOfOptions.append("Split")
  for card in cardsList:
    if card.number == 0 and cardSum(cardsList) + 10 <= 21:
      listOfOptions.append("Ace to 11")
      break
  return listOfOptions

class player:
  def __init__(self, name, dongs):
    self.name = name
    self.dongs = dongs
    self.player = player

class suits:
	Hearts = "♥"
	Diamonds = "♦"
	Clubs = "♣"
	Spades = "♠"

class card:
  def __init__(self, numb, suit=""):
    if numb == -1: #hidden card
      self.number = -1
      self.cardText = HIDDEN_CARD
    else:
      self.number = numb
      self.value = cardValues[cardNumb[self.number]]
      self.suit = suit
      if self.number == 9:
        self.cardText = CARD_ASCII.format(cardNumb[self.number], self.suit, cardNumb[self.number])
      else:
       self.cardText = CARD_ASCII.format(cardNumb[self.number] + " ", self.suit, " " + cardNumb[self.number])
  def __str__(self):
    return self.cardText

class bet:
  def __init__(self, amount, cards=[], player=""):
    self.amount = amount
    self.cards = cards
    self.player = player
  def hit(self, deck):
    self.cards.append(deck.draw(True) )
  def __str__(self):
    print(self.player.name + "'s cards : \n")
    singleListPrintCards(self.cards)
    return "\n" + self.player.name + "'s bet : " + str(self.amount) + " " + settings.settings["currency"]

class deck:
  def __init__(self):
    self.cards = []
    for number in range(0, 13):
      for suit in cardSuits:
        self.cards.append(card(number, suit))
				
  def remake(self):
    self.cards = []
    for suit in cardSuits:
      for number in range(0, 13):
        self.cards.append(card(number, suit))
	
  def draw(self, remove=False):
    card = copy.copy(self.cards[0])
    if remove:
      self.cards.remove(self.cards[0])
    return card
	
  def shuffle(self):
    random.shuffle(self.cards)

def startGame():
  clear()
  beginGame()
  clear()
  print("ENJOY THE GAME!")
  time.sleep(2)
  clear()
  print_slow("Game is about to begin. "); print_slower(". . . . .\n")
  clear()
  print_slow("Shuffling cards. "); print_slower(". . . . .\n")
  clear()
  print("Shuffling cards. "); print_slower(". . . . .\n")
  clear()
  print("Shuffling cards. "); print_slower(". . . . .\n")
  clear()

clear()

print_slow("Welcome to . . . . .\n")

time.sleep(2)

print(" _     _            _    _            _\n"   
                          "| |   | |          | |  (_)          | |    \n"
                          "| |__ | | __ _  ___| | ___  __ _  ___| | __ \n"
                          "| '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ / \n"
                          "| |_) | | (_| | (__|   <| | (_| | (__|   <  \n"
                          "|_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\ \n"
                          "                       _/ |                 \n"
                          "                      |__/                  " )
print(                    "=============================================\n")

print_slow("\nThe second most famous, fast-paced card game, featured in every single casino around the country!\n")

time.sleep(3)

clearLess()

input("\nPress enter to continue >> ")


def startBetting(player):
  betAmount = ""
  
  while not isNumber(betAmount):
    betAmount = input("{}, what do you want to bet this round. You have {} dongs :".format(player.name, player.dongs))
    if not isNumber(betAmount):
      print(betAmount + " is an invalid number")
    elif int(betAmount) < 0:
      print("Bet cannot be 0 or negative")
      betAmount = "" #just so it keeps looping
    elif int(betAmount) > player.dongs: #change with users chips
      print("Cannot bet more dongs than you own")
      betAmount = ""
    elif int(betAmount) == 0:
      print("You are unable to bet. You lose!")
  player.dongs = player.dongs - int(betAmount)
  bets[player.name] = [ bet(int(betAmount), [deck.draw(True), deck.draw(True)], player) ]

def processBet(betObj):
  print("Dealer's Cards : ")
  singleListPrintCards(dealerCards)
  print("\n")
  print(betObj)
  print("\nSum of " + betObj.player.name + "'s cards : " + str(cardSum(betObj.cards)))
  print("\n")
  options = getOptions(betObj)
  if options[0] == "Bust":
    input("You bust this hand!\nPress enter to continue")
    clear()
  elif options[0] == "21":
    input("You have blackjack on hand.\nPress enter to Stand")
    clear()
  else:
    print("Your options are :\n")
    
    for index, option in enumerate(options):
      print(str(index) + ". " + option)
      
    selection = -1
    
    while not isNumber(selection) or int(selection) < 0 or int(selection) > len(options) - 1:
      selection = input("What do you want to do?")
      if not isNumber(selection) or int(selection) < 0 or int(selection) > len(options) - 1:
        print("Invalid selection, please try again")
        
    selection = options[int(selection)]
    
    if selection == "Hit":
      betObj.hit(deck)
      clear()
      processBet(betObj)
    elif selection == "Stand":
      clear()
    elif selection == "Split":
      betObj.player.dongs -= betObj.amount
      splitBet = bet(betObj.amount, [betObj.cards[1], deck.draw(True)], betObj.player)
      bets[betObj.player.name].append(splitBet)
      betObj.cards[1] = deck.draw(True)
      clear()
      print("Hand was split")
      processBet(betObj)
    elif selection == "Ace to 11":
      for card in betObj.cards:
        if card.number == 0:
          card.value = 11
          break
      clear()
      print("One ace is now 11")
      processBet(betObj)

def automaticProcess(cards):
  if cardSum(cards) > 21:
    return "Bust"
  elif cardSum(cards) == 21:
    return "21"
  else:
    for card in cards:
      if card.number == 0 and cardSum(cards) + 10 <= 21:
        card.value = 11
        break
    if cardSum(cards) < 17:
      return "Draw"
    elif cardSum(cards) >= 17:
      return "Stand"

player1 = player("Player1", 2500)
player2 = player("Player2", 2500)




deck = deck()
dealerCards = []
bets = {}

def game():
  deck.remake()
  deck.shuffle()
  
  bets.clear()
  dealerCards.clear()
  
  startBetting(player1)
  startBetting(player2)
  
  dealerCards.append(card(-1))
  dealerCards.append(deck.draw(True))
  
  for player in bets:
    clear()
    for betObj in bets[player]:
      processBet(betObj)
  
  
  clear()
  print("Dealer's Cards : ")
  singleListPrintCards(dealerCards)
  print("\n")
  printAllBets(bets)
  print("\n")
  print("Showing dealer's card in 3 seconds")
  print_slower(". . . . . .")
  dealerCards[0] = deck.draw(True)
  clear()
  
  dealerSum = cardSum(dealerCards)
  while dealerSum < 17:
    print("Dealer's Cards : ")
    singleListPrintCards(dealerCards)
    print("Dealer's Total : " + str(cardSum(dealerCards)))
    print("\n")
    printAllBets(bets)
    print("\n")
    
    process = automaticProcess(dealerCards)
    if process == "Draw":
      dealerCards.append(deck.draw(True))
      print("Dealer is drawing")
      print_slower(".......")
    elif process == "Bust":
      print("Dealer went bust")
      print_slower(".......")
    elif process == "Stand":
      print("Dealer stands")
      print_slower(".......")
    elif process == "21":
      dealerSum = 21
      print("Dealer has blackjack")
      print_slower(".......")
    clear()
    dealerSum = cardSum(dealerCards)
  
  print("Dealer's Cards : ")
  singleListPrintCards(dealerCards)
  print("Dealer's Total : " + str(cardSum(dealerCards)))
  print("\n")
  printAllBets(bets)
  print("\n")
  
  playerWinLoseAmounts = {}
  
  if dealerSum == 21:
    print("Dealer has blackjack, processing bets")
    for player in bets:
      playerWinLoseAmounts[player] = 0
      for betObj in bets[player]:
        if cardSum(betObj.cards) == 21:
          betObj.player.dongs += betObj.amount
        else:
          playerWinLoseAmounts[player] -= betObj.amount
  elif dealerSum > 21:
    print("Dealer bust")
    for player in bets:
      playerWinLoseAmounts[player] = 0
      for betObj in bets[player]:
        if cardSum(betObj.cards) > 21:
          playerWinLoseAmounts[player] -= betObj.amount
        elif cardSum(betObj.cards) == 21:
          playerWinLoseAmounts[player] += int(betObj.amount*1.5)
          betObj.player.dongs += int(betObj.amount*1.5)
        else:
          playerWinLoseAmounts[player] += betObj.amount
          betObj.player.dongs += betObj.amount*2
  else:
    print("Dealer has {}, processing bets\n".format(dealerSum))
    print_slower(".......\n")
    for player in bets:
      playerWinLoseAmounts[player] = 0
      for betObj in bets[player]:
        if cardSum(betObj.cards) == dealerSum:
          #print(betObj.player.name + " got back " + str(betObj.amount) + " dongs")
          #playerWinLoseAmounts[player] += betObj.amount
          betObj.player.dongs += betObj.amount
        elif cardSum(betObj.cards) == 21:
          #print(betObj.player.name + " won " + str(betObj.amount) + " dongs")
          playerWinLoseAmounts[player] += int(betObj.amount*1.5)
          betObj.player.dongs += int(betObj.amount*1.5)
        elif cardSum(betObj.cards) < dealerSum or cardSum(betObj.cards) > 21:
          #print(betObj.player.name + " lost " + str(betObj.amount) + " dongs")
          playerWinLoseAmounts[player] -= betObj.amount
        elif cardSum(betObj.cards) > dealerSum or dealerSum > 21:
          #print(betObj.player.name + " won " + str(betObj.amount) + " dongs")
          playerWinLoseAmounts[player] += betObj.amount
          betObj.player.dongs += betObj.amount*2
  
  for player in playerWinLoseAmounts:
    if playerWinLoseAmounts[player] < 0:
      print(player + " lost " + str(abs(playerWinLoseAmounts[player])) + " " + settings.settings["currency"])
    elif playerWinLoseAmounts[player] > 0:
      print(player + " won " + str(playerWinLoseAmounts[player]) + " " + settings.settings["currency"])
    elif playerWinLoseAmounts[player] == 0:
      print(player + " lost no dongs")
  
  input("Press enter to continue")
  clear()
  game()


gameEngine = engine(mainMenu()) #initializes an engine named gameEngine with mainMenu as the starting scene
settings = settings() #initializes settings
gameEngine.play() #starts the engine
