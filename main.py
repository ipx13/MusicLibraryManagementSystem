import os
from random import choice

print("\n------- Welcome to LibRandomizer 1.0! -------"
      "\n\nDear music nerds, are you tired of scrolling through your gi-normous library, "
      "\nlooking for something to listen to? Add a folder containing your music library"
      "\nand we'll fetch a random personalized recommendation for you!")

def menu():
    print("\n------- Main Menu -------")
    print("1 - Get started")
    print("2 - Recommend me something!")
    print("3 - Exit")
    print("-------------------------")

perm_path = ""

while True:
    while True:
        try:
            menu()
            menu_choice = int(input("\nWhat would you like to do? "))
        except:
            print("Please enter an integer between 1-3!")
        else:
            if menu_choice in [1, 2, 3]:
                if menu_choice == 1:
                    print("\n------- Setting up -------")
                    print("\nPlease add the path of your folder"
                          "\nNOTE: Use E:\[folder]\[subfolder] formatting")

                    while True:
                        mainpath = input("\nPath: ")

                        if os.path.exists(mainpath):
                            print("\nDisplaying folder contents:")
                            print("> {}".format(mainpath))
                            for i in os.listdir(mainpath):
                                print(">> {}".format(i))

                            print("\nBased on the displayed contents, have you reached your artist folders yet?"
                                  "\n1 - Yes"
                                  "\n2 - No")

                            while True:
                                try:
                                    ch1_conf = int(input("\nAnswer: "))
                                except:
                                    print("Please enter an integer!")
                                    continue
                                else:
                                    if ch1_conf in [1, 2]:
                                        if ch1_conf == 1:
                                            permpath = mainpath
                                            perm_path = permpath
                                            print("\nSuccessfully saved {} as the main directory for randomization!".format(permpath))
                                            break

                                        elif ch1_conf == 2:
                                            while True:
                                                print("\nChoose a subfolder to set as the main folder:")
                                                for i in os.listdir(mainpath):
                                                    print("> {}".format(i))
                                                print("\nType the folder name")
                                                explore_fldr = input("Set as main folder: ")
                                                permpath = mainpath + "\{}".format(explore_fldr)
                                                try:
                                                    if os.path.exists(permpath):
                                                        print("\nDisplaying folder contents:")
                                                        print("> {}".format(permpath))
                                                        for i in os.listdir(permpath):
                                                            print(">> {}".format(i))
                                                    else:
                                                        print("Path not found! Please check your input.")
                                                        continue
                                                except:
                                                    print("\nERROR: Make sure you have entered a folder, not a file.")
                                                    continue
                                                else:
                                                    print("\nNote: This program can only ask to search deeper ONCE. Please make sure that your artist folders are already accessible.")

                                                    perm_path = permpath
                                                    print("\nSuccessfully saved {} as the main directory for randomization!".format(
                                                            permpath))
                                                    break
                                            break
                                    else:
                                        print("Please enter either 1 or 2!")
                                        continue
                            break
                        else:
                            print("Path not found! Please check your input.")
                            continue
                elif menu_choice == 2:
                    list_artists = []
                    list_artist_albums = []

                    while True:
                        print("\n------- Randomization Menu -------")
                        print("\nWhat would you like to randomize?"
                              "\n1 - Artists"
                              "\n2 - Albums")

                        while True:
                            try:
                                ch2_rand = int(input("\nI'd like to randomize: "))
                            except:
                                print("Please enter and integer!")
                                continue
                            else:
                                if ch2_rand in [1, 2]:
                                    if ch2_rand == 1:
                                        for artists in os.listdir(perm_path):
                                            list_artists.append(artists)
                                        print("\nWhy don't you try out listening something from {}?".format(
                                            choice(list_artists)))
                                        break
                                    elif ch2_rand == 2:
                                        for artists in os.listdir(perm_path):
                                            list_artists.append(artists)
                                        rand_art = choice(list_artists)
                                        mod_path = perm_path + "\{}".format(rand_art)

                                        for albums in os.listdir(mod_path):
                                            list_artist_albums.append(albums)

                                        print("\nFor a random album, we got", choice(list_artist_albums), "from",
                                              rand_art + "!")
                                        break
                                    else:
                                        print("Please enter either 1 or 2!")
                                        continue
                                    break
                        break
                elif menu_choice == 3:
                    print("\n------- Exiting the program -------")
                    print("\nThanks for using this program!")
                    break
            else:
                print("Please an integer between the range 1-3!")
                continue
        continue
    break

