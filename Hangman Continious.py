import random


hangmanArts = ["" +
    "\n" +
    "\n" +
    "\n" +
    "\n" +
    "\n" +
    "\n         -----",
                   
    "\n           |" +
    "\n           |" +
    "\n           |" +
    "\n           |" +
    "\n           |" +
    "\n           | " +
    "\n         -----",

    "            " +
    "\n        \  |" +
    "\n         \ |" +
    "\n           |" +
    "\n           |" +
    "\n           | " +
    "\n         -----",

    "  ----------" +
    "\n        \  |" +
    "\n         \ |" +
    "\n           |" +
    "\n           |" +
    "\n           | " +
    "\n         -----",

    "  ----------" +
    "\n  0     \  |" +
    "\n         \ |" +
    "\n           |" +
    "\n           |" +
    "\n           | " +
    "\n         -----",

    "  ----------" +
    "\n  0     \  |" +
    "\n  |      \ |" +
    "\n  |        |" +
    "\n  |        |" +
    "\n           | " +
    "\n         -----",

    "  ----------" +
    "\n  0     \  |" +
    "\n  |      \ |" +
    "\n ---       |" +
    "\n  |        |" +
    "\n           | " +
    "\n         -----",
                   
    "  ----------" +
    "\n  0     \  |" +
    "\n  |      \ |" +
    "\n ---       |" +
    "\n  |        |" +
    "\n  \        | " +
    "\n         -----",
                   
    "  ----------" +
    "\n  0     \  |" +
    "\n  |      \ |" +
    "\n ---       |" +
    "\n  |        |" +
    "\n  /\       | " +
    "\n         -----"]

words = ["flowery", "repulsive", "wilderness", "male", "deep", "early", "system", "holistic", "lethal", "check", "truck", "accept", "brainy", "structure", "lettuce", "flag", "bells", "itch", "huge", "salt", "trick", "crow", "night", "amount", "grubby", "smart", "supply", "reply", "learned", "neat", "miniature", "picture", "bead", "describe", "meat", "man", "rot", "melted", "awesome", "ask", "ray", "toothbrush", "minute", "peel", "bury", "disagree", "wink", "wicked", "damp", "wind", "boorish", "chew", "lean", "alike", "crime", "damage", "brash", "drawer", "aunt", "giraffe", "toes", "bottle", "improve", "grateful", "dramatic", "shallow", "gullible", "accessible", "form", "disagree", "alarm", "cook", "tricky"]

games = 0
won = 0

def runGame():
    global games
    global won

    best = 100
    
    for a in range(52):
        print(" ")
    word = random.choice(words)



    knownLetters = []
    wrongLetters = []

    if games > 1:
        if len(wrongLetters) < best:
            print("This was your best game so far!")
    else:
        best = len(wrongLetters)

        
    if games != 0:
        print("You have won " + str(won) + " games out of " + str(games) + " " + str(round(won/games*100)) + "%")
        
    while len(wrongLetters) < len(hangmanArts):
        #print(word)

        ans = ""
        for l in range(len(word)):
            if(word[l] in knownLetters):
                ans = ans + word[l] + " "
            else:
                ans = ans + "_ "

        print(ans)

        print(" ")
        for letter in wrongLetters:
            print(letter, end=', ')
        print(" ")

               
        characterGuess = input("Enter your guess > ")
        characterGuess = characterGuess.lower()

        if (len(characterGuess) > 1):
            #Is a word
            if (characterGuess == word):
                print("\n\n\n\n\n")
                print("Correct!")

                won = won + 1
                break
            else:
                wrongLetters.append(characterGuess)

        else:
            #Character
            if (characterGuess in word):
                knownLetters.append(characterGuess)
                
            else:
                wrongLetters.append(characterGuess)
                print(characterGuess + " is not in the word or a character.")


        for j in range(52):
            print(" ")


        if(len(wrongLetters) > 0):
            print(hangmanArts[len(wrongLetters)-1])

        
    print("The word was " + word)


    input("Press Enter to continue...")
    games = games + 1
    runGame()


runGame()

