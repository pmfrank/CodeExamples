import os

answer = input("Would you like to enter the game? yes/no ")

# Let's declare some variables to include
gp = 100 # The amount of cash the character is carrying
hp = 20 # The characters current health points
max_hp = 20 # The characters maximum health points
inventory = ['sword','shield','armor','health potion','dead rat'] # A list of all the items the player is carrying

if answer.lower().strip() == 'yes':

    answer = input("""
    You are in the middle of town 1.
    What would you like to do?
    Go to the shop, type s
    Go to home/hotel, type h
    continue on your jorney, type c

    """)

    answer = answer.lower().strip()

    if answer == 's':
        answer = input("""
        Welcome to the shop!
        To buy snacks, type s
        To by cell membrane, type m
        
        """)
    elif answer == 'h':
        answer == inpute("""
        You enter your house.
        What would you like to do?
        To go upstairs, type u

        """)
    elif answer == 'c':
        print('Continuing')
    # Lets add in some answers to make use of those variables
    elif answer == 'stats':
        print(f"""
        Your current hp: {hp}
        Your maximum hp: {max_hp}
        """)
    elif answer == 'inventory':
        print('You are carrying:')
        for item in inventory:
            print(item)
    else:
        print('Your answer makes no sense and the universe imploded. Good job!')
else:
    print('Oh well... cya!')