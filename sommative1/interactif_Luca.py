#Programe interactif
#Luca sommative
print("what is your name")
x = input()
print("hello "+ x)
print("do you want to play a game")
y = input()
yes = "good"
no =  "bad"
if y == "yes":
  print("great lets start")
elif y == "no":
  print("ok bye ") 
if y == "yes":
 print("question 1 of 3")
print("what is the penguins real name a)andrew stone b)jack white c)oswald coblepott")
answer = input().lower()
if answer == "a":
    print(" wrong")
elif answer == "b":
    print(" ha no")
elif answer == "c":
    print(" correct")
if answer == "c":
  print("question 2 of 3")
print("what is the best movie a) joker b) avengers endgame c) anything else")
answer = input().lower()
if answer == "a":
    print(" correct correct correct")
elif answer == "b":
    print(" nice joke buddy")
elif answer == "c":
    print(" wrong!!")
if answer == "a":
  print("question 3 of 3")
print("when did batman arkham origins take place a) june 5 b) december 24 to 25 c) october 31")
answer = input().lower()
if answer == "a":
    print(" do you even know what arkham origins is")
elif answer == "b":
    print(" good job ")
elif answer == "c":
    print(" no no no")
if answer == "b":
  print("you won, thanks for playing")