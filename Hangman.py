'''
Description:
        You must create a Hangman game that allows the user to play and guess a secret word.  
        See the assignment description for details.
    
@author: Patrick Lee   pyl7
'''

import random

def handleUserInputDifficulty():
    ''' 
    This function asks the user if they would like to play the game in (h)ard or (e)asy mode, then returns the 
    corresponding number of misses allowed for the game. 
    '''
    
    print("How many misses do you want? Hard has 8 and Easy has 12")
    letterChosen = input('(h)ard or (e)asy> ')
    if letterChosen == 'h':
        return 8
    elif letterChosen == 'e':
        return 12

def getWord(words, length):
    '''
    Selects the secret word that the user must guess. 
    This is done by randomly selecting a word from words that is of length length.
    '''
    newList = []
    for word in words:
        word = word[:-1]
        if len(word) == length:
            newList.append(word)
    randomPosition = random.randrange(0, len(newList), 1)
    print(length)
    print(newList[randomPosition])
    return newList[randomPosition]

def createDisplayString(lettersGuessed, misses, hangmanWord):
    '''
    Creates the string that will be displayed to the user, using the information in the parameters.
    '''
    lettersGuessed.sort()
    lettersGuessedValue = ""
    for char in lettersGuessed:
        lettersGuessedValue = lettersGuessedValue + char + " "
    lettersGuessedValue = lettersGuessedValue.rstrip()
    hangmanWordValue = ""
    for char in hangmanWord:
        hangmanWordValue = hangmanWordValue + char + " "
    hangmanWordValue = hangmanWordValue.rstrip()
    message = "letters you've guessed:  "
    message2 = "misses remaining = "
    return message + lettersGuessedValue + "\n" + message2 + str(misses) + "\n" + hangmanWordValue

def handleUserInputLetterGuess(lettersGuessed, displayString):
    '''
    Prints displayString, then asks the user to input a letter to guess.
    This function handles the user input of the new letter guessed and checks if it is a repeated letter.
    '''
    
    something = False
    while not something:
        print(displayString)
        inputValue = input("letter> ")
        if inputValue not in lettersGuessed:
            something = True
            return inputValue
        elif inputValue in lettersGuessed:
            print("you already guessed that")

def updateHangmanWord(guessedLetter, secretWord, hangmanWord):
    '''
    Updates hangmanWord according to whether guessedLetter is in secretWord and where in secretWord guessedLetter is in.
    '''
    
    positionsList = []
    if guessedLetter in secretWord:
        for x in range(len(secretWord)):
            if guessedLetter == secretWord[x]:
                positionsList.append(x)
    elif guessedLetter not in secretWord:
        return hangmanWord
    
    for number in positionsList:
        hangmanWord[number] = guessedLetter
    
    return hangmanWord

def processUserGuess(guessedLetter, secretWord, hangmanWord, misses):
    '''
    Uses the information in the parameters to update the user's progress in the hangman game.
    '''
    
    newList = [updateHangmanWord(guessedLetter, secretWord, hangmanWord), misses, True]    
    return newList

def runGame(filename):
    '''
    This function sets up the game, runs each round, and prints a final message on whether or not the user won.
    True is returned if the user won the game. If the user lost the game, False is returned.
    '''
    
    file = open(filename, "r")
    lengthOfSecretWord = random.randrange(5, 11)
    listOfWords = file.readlines()
    file.close()
    missesRemaining = handleUserInputDifficulty()
    numberOfMisses = missesRemaining
    hangmanWord = getWord(listOfWords, lengthOfSecretWord)
    
    currentHangmanWord = []

    for x in range(len(hangmanWord)):
        currentHangmanWord.append('_')

    lettersGuessed = []

    while '_' in currentHangmanWord:             
        guessedLetterNotAlreadyGuessed = handleUserInputLetterGuess(lettersGuessed, createDisplayString(lettersGuessed, missesRemaining, currentHangmanWord))
        lettersGuessed.append(guessedLetterNotAlreadyGuessed)
        processUserGuess(guessedLetterNotAlreadyGuessed, hangmanWord, currentHangmanWord, missesRemaining)
        
        if guessedLetterNotAlreadyGuessed not in hangmanWord:
            print("you missed: " + guessedLetterNotAlreadyGuessed + " not in word")
            missesRemaining = missesRemaining - 1

        if missesRemaining == 0:
            print("you're hung!!" + "\n" + "word is " + hangmanWord + "\n" + "you made " + str(len(lettersGuessed)) + " guesses with " + str(numberOfMisses - missesRemaining) + " misses")
            return False

    if '_' not in currentHangmanWord:
        print("you guessed the word: " + hangmanWord + "\n" + "you made " + str(len(lettersGuessed)) + " guesses with " + str(numberOfMisses - missesRemaining) + " misses" )
        return True

if __name__ == "__main__":
    '''
    Running Hangman.py should start the game, which is done by calling runGame, therefore, we have provided you this code below.
    '''
    runGame("lowerwords.txt")
