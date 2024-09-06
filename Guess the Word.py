words_list = [
    "Abbreviations",
    "Confectionery",
    "Procrastinate",
    "Misunderstand",
    "Extraordinary",
    "Hypothetical",
    "Overexposure",
    "Misalignment",
    "Rehabilitation",
    "Circumference",
    "Discontinue"
]

# User selects what word they wish to get started going on
number = int(input("Chose a number 0-10"))

word = words_list[number]
print(word) # test to make sure word is picked 
x = list(word)
turns = 12 # How many turns the user gets 

# While loop to finding the letter 
while turns > 0: 
    myletter = input("Enter a letter!")
    if myletter not in x: 
        print("-")
        turns -= 1 
    elif myletter in x: 
        print(myletter)
