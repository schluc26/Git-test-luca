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
questionanswer = input().lower()
if questionanswer == "a":
    print(" wrong")
elif questionanswer == "b":
    print(" ha no")
elif questionanswer == "c":
    print(" correct")
if questionanswer == "c":
  print("question 2 of 3")
