def intro():
    print("You wake up in a dark forest. You can go left or right.")
    choice = input("Which direction do you choose? (left/right/center): ").strip().lower()
    if choice == "left":
        left_path()
    elif choice == "right":
        right_path()
    elif choice == "center":
        center_path()
    else:
        print("You stand still, unsure what to do. The forest swallows you.")

def left_path():
    print("You walk left and find a mysterious glowing sword stuck in a stone.")

def right_path():
    print("You walk right and encounter a talking squirrel who challenges you to a duel.")
    print("You decide to slay the squirrel, but after you defeat it you sell its fur for money, and you start becoming greedy")
    print("You like the money you made so you start a business where you hunt innocent squirrels and sell their fur")

def center_path():
    print("You have chosen the center path")

if __name__ == "__main__":
    intro()
