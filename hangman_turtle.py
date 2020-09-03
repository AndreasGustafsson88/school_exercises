import random
from turtle import *


words = ["ulricehamn", "frisbee", "långben", "rönnbärsmal", "skidbacken"]
life_count = 8


def main():
    writer_turtle = Turtle()
    writer_turtle.hideturtle()
    writer_turtle.penup()
    writer_turtle.goto(-420, 0)
    writer_turtle.pendown()
    writer_turtle.pencolor("green")

    input_turtle = Turtle()
    input_turtle.hideturtle()
    screen = input_turtle.getscreen()

    used_turtle = Turtle()
    used_turtle.hideturtle()
    used_turtle.penup()
    used_turtle.goto(-420, -50)
    used_turtle.pencolor("blue")
    used_turtle.pendown()

    lifes_turtle = Turtle()
    lifes_turtle.hideturtle()
    lifes_turtle.penup()
    lifes_turtle.goto(-420, -100)
    lifes_turtle.pendown()
    lifes_turtle.pencolor("red")

    global life_count
    word = random.choice(words)
    hidden_word = "_ " * len(word)
    used_letters = ""

    while life_count > 0:

        writer_turtle.write(f"{hidden_word}", font=("Arial", 38, "normal"))
        used_turtle.clear()
        used_turtle.write(f"Used letters: {used_letters}", font=("Arial", 16, "normal"))
        guess = screen.textinput("Guess", 'Guess a letter: ')
        used_letters += guess + " "

        new_hidden = ""
        lose_life = True
        for i, letter in enumerate(word):
            if guess.lower() == letter:
                new_hidden += letter + " "
                lose_life = False
            else:
                new_hidden = new_hidden + hidden_word[i*2] + " "

        if lose_life:
            life_count -= 1
            if life_count == 7:
                hangman_turtle = Turtle()
                hangman_turtle.hideturtle()
                hangman_turtle.pensize(10)
                hangman_turtle.penup()
                hangman_turtle.goto(50, -250)
                hangman_turtle.pendown()
                hangman_turtle.left(90)
                hangman_turtle.forward(500)
            elif life_count == 6:
                hangman_turtle.right(90)
                hangman_turtle.forward(300)
            elif life_count == 5:
                hangman_turtle.right(90)
                hangman_turtle.forward(50)
                hangman_turtle.right(90)
                hangman_turtle.circle(50)
            elif life_count == 4:
                hangman_turtle.left(90)
                hangman_turtle.penup()
                hangman_turtle.goto(350, 100)
                hangman_turtle.pendown()
                hangman_turtle.forward(200)
            elif life_count == 3:
                hangman_turtle.right(45)
                hangman_turtle.forward(75)
            elif life_count == 2:
                hangman_turtle.goto(350, -100)
                hangman_turtle.left(90)
                hangman_turtle.forward(75)
            elif life_count == 1:
                hangman_turtle.penup()
                hangman_turtle.goto(350, 20)
                hangman_turtle.pendown()
                hangman_turtle.right(180)
                hangman_turtle.forward(75)
            elif life_count == 0:
                hangman_turtle.goto(350, 20)
                hangman_turtle.right(90)
                hangman_turtle.forward(75)

        hidden_word = new_hidden
        lifes_turtle.clear()
        lifes_turtle.write(f"Lives: {life_count}", font=("Arial", 20, "normal"))

        if "_" not in hidden_word:
            lifes_turtle.clear()
            lifes_turtle.write(f"You did it, with {life_count} lives left!", font=("Arial", 20, "normal"))
            life_count = 0

        writer_turtle.clear()
        writer_turtle.write(hidden_word, font=("Arial", 38, "normal"))

    done()


if __name__ == "__main__":
    main()
