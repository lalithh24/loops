import random

health = 50

difficult = 3

potion_health = int(random.randint(25,50) / difficult)

health = health + potion_health 

print(health)
