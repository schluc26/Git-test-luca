#Programe interactif
#Luca sommative
print("what is your name")
x = input()
print("hello "+ x)


print("do you want to play a game")#starting the program with conversation
y = input()# input makes you write something from your keyboard
yes = "good"
no =  "bad"
if y == "yes":
  print("great lets start")
elif y == "no":
  print("ok bye ") 


if y == "yes":# the quiz will start now
 print("question 1 of 3")
print("what is the penguins real name a)andrew stone b)jack white c)oswald coblepott")
answer = input().lower()# it picks how one of the variables is right and how the others are wrong using lower case letters
if answer == "a":
    print(" wrong")
elif answer == "b":
    print(" ha no")
elif answer == "c":
    print(" correct")


if answer == "c":# seconde question
  print("question 2 of 3")
print("what is the best movie a) joker b) avengers endgame c) anything else")
answer = input().lower()
if answer == "a":
    print(" correct correct correct")
elif answer == "b":
    print(" nice joke buddy")
elif answer == "c":
    print(" wrong!!")


if answer == "a":#third question
  print("question 3 of 3")
print("when did batman arkham origins take place a) june 5 b) december 24 to 25 c) october 31")
answer = input().lower()
if answer == "a":
    print(" do you even know what arkham origins is")
elif answer == "b":
    print(" good job ")
elif answer == "c":
    print(" no no no")


if answer == "b":# end of quiz and programe
  print("you won, thanks for playing")