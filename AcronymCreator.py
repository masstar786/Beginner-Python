#ask for user input
user_input = str(input("Enter a phrase: "))

#splitting the user input
text = user_input.split()
acr = " "

for i in text:
    acr = acr+str(i[0]).upper()

print(acr)
