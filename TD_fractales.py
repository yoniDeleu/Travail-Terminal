import turtle
#Exerice 1
# Q1)
turtle.speed(500)

def dessine(n):
    if n > 0:
        turtle.forward(n)
        turtle.right(90)        
        dessine(n-2)
print(dessine(50))

# Q4)

def dessine(n):
    if n < 0:
        turtle.penup
    else :
        turtle.forward(n)
        turtle.right(90)
        dessine(n-2)
print(dessine(500))

#Q5.a)

def dessineIteratif(n):
    while n > 0:
        turtle.pendown
        turtle.forward(n)
        turtle.right(90)
        n = n-2
print(dessineIteratif(500))

#Exercice 2
