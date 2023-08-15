import random
randNumber = random.randint(1,100)
print(randNumber)
userGuess =None
gusses = 0
while (userGuess! = randomNumber)

userGuess = int(input["enter your guess"])
if(userGuess**randnumber):
    print("You guessed it right!")
    
else:
    if(userGuess>randNumber)
    print("You guessed it wrong! Enter a smaller number")
else:
 print ("You guessed it wrong ! enter a Larger number")
 guesses +=1
    
print("You guessed the number in{gusses} gusses")
with open("hiscore.txt","f")
hiscore = int(f.read())
if(guesses<hiscore):
    print ("you have just broken the high score")
with open("hiscore.txt","w")as f:
    f.write(str(guesses))