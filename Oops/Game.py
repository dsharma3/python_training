##Build a game project - Who wants to be a millionare.

##Player
    # Player can chose answers
    # Get the winning amount
#Host
    #Start the game
    #End the game
    #Display next question
#Computer
    #Calculate score
    #Start the game
    #Display next question

class Computer():    
    
    def __init__(self):
        self.questions =["Who is the president of USA?"
               ,"What is the capital of India?"
               ]
        self.options =[
                    ["Barack Obama", "Joe Biden", "Donal Trump", "Xyz"]
                    ,["Delhi", "Kolkata","Mumbai","Chennai"]
                ]
        self.answers = [1,0]
        self.winningAmount = [1000,2000]
        self.currentQuestion = 0

    def startGame(self):
        print("############################################")        
        print("#                                          #")
        print("#                                          #")
        print("#             Welcome to KBC               #")
        print("#                                          #")
        print("#                                          #")
        print("############################################")

        print("\nPress enter to start the game")
        
    def getNextQuestion(self):
        question = self.questions[self.currentQuestion]
        print(question)
        self.displayOptions()
        return question
    
    def displayOptions(self):
        for item in range(0, len(self.options[self.currentQuestion])):
            print("{}.{}".format(item+1, self.options[self.currentQuestion][item]))

    def checkAnswer(self, answer):
        if int(answer)-1 == self.answers[self.currentQuestion]:
            self.currentQuestion+=1
            return True
        else:
            return False
    
    
    def getWinningAmount(self):    
        return self.winningAmount[self.currentQuestion-1]
    
        
class Player():
    def __init__(self, name):
        self.name = name

    def answerQuestion(self, question):
        answer = input()
        print("{} has given {} as answer for question {}".format(self.name, answer, question))
        return answer


print("Please enter your name:\n")
playerName = input()
player = Player(playerName)
computer = Computer()
computer.startGame()


input()
while(True):
    question = computer.getNextQuestion()

    answer = player.answerQuestion(question)
    isCorrectAnswer = computer.checkAnswer(answer)

    if isCorrectAnswer:
        amount = computer.getWinningAmount()
        print("{} has won {}".format(playerName, str(amount)))
    else:
        print("Wrong answer!!")
        break


print("{} has won {}$",str(amount))

    


