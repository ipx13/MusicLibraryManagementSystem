import os

print("Welcome to LibRandomizer 1.0! Dear music nerds, are you tired of scrolling through your gi-normous library, looking for something to listen to? Add a folder containing your music library, and we'll fetch a random personalized recommendation for you!\n")

def menu():
    print("Menu: ")
    print("1 - Get started")
    print("2 - Recommend me something!")
    print("3 - Exit")

while True:
    menu()
    while True:
        try:
            menu_choice = int(input("What would you like to do? "))
        except:
            print("Please enter an integer between 1-3!")
        else:
            break
