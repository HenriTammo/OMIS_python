import turtle
import random

player1 = turtle.Turtle()
player2 = turtle.Turtle()

player1.color("green")
player2.color("pink")
player1.penup()
player2.penup()

player1.goto(300, 60)
player1.pendown()
player1.circle(40)
player2.goto(300, -140)
player2.pendown()
player2.circle(40)

player1.penup()
player2.penup()

player1.goto(-200, 100)
player2.goto(-200, -100)

die = [1, 2, 3, 4, 5, 6]

game = True
while game == True:
    if player1.pos() >= (300,100):
        print ("player 1 wins")
        game == False
    elif player2.pos() >= (300, -100):
        print("player 2 wins")
        game == False
    else:
        veeretus = input("press Enter to roll dice")
        result = random.choice(die)
        print(result)
        player1.fd(10*result)
        veeretus = input("press Enter to roll dice")
        result = random.choice(die)
        print(result)
        player2.fd(10*result)