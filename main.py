import os

print("Welcome to LibRandomizer 1.0! Dear music nerds, are you tired of scrolling through your gi-normous library, looking for something to listen to? Add a folder containing your music library, and we'll fetch a random personalized recommendation for you!")

def menu():
    print("\nMenu: ")
    print("1 - Get started")
    print("2 - Recommend me something!")
    print("3 - Exit")

while True:
    menu()
    while True:
        try:
            menu_choice = int(input("\nWhat would you like to do? "))
        except:
            print("Please enter an integer between 1-3!")
        else:
            if menu_choice in [1, 2, 3]:
                if menu_choice == 1:
                    print("\n------- Setting up -------")
                    print("\nPlease add the path of your folder"
                          "\nNOTE: Use E:\[folder]\[subfolder] formatting")
                    mainpath = input("\nPath: ")
                break
            else:
                print("Please an integer between the range 1-3!")
                continue

