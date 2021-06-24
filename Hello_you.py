#ask user for name

name = input ( "what is your name?:" )

#ask user for age
age =  input( " What is your age?: " )

#ask for city
City =  input ( " What is your city?: ")


#ask about their enjoyments
love = input (" what is your fav city?: ")


#create output texts

string = " Your name is {} and you are {} years old. You come from {} city and you love {} "
output = string.format(name, age, City, love)
#print outputs
print(output)


