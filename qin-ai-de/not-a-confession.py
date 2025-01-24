#Just some normal code

def ask_for_names(*args):
    names = input("Your names please: ")
    check_names(names)

def the_end(*args):
    pass

def check_names(name_entry):
    if name_entry.lower().split() == ['khalondi', 'vanessa']:
        print(f"\nThank you {name_entry.title().split()[1]}.")
        normal_function()
    elif name_entry.lower().split() == ['vanessa', 'khalondi']:
        print(f"\nThank you {name_entry.title().split()[0]}.")
        normal_function()
    elif name_entry.lower().split() == ['aturinda', 'vanessa']:
        print("\nIf you want to marry me that much, just say so. I want it too.\n\tMaybe ^-^")
        print("For now just play along and enter your actual names.\n")
        ask_for_names()
    else:
        print("\nAre those really your names??? \nPerhaps you mispelt something?")
        print("Why don't you give it another go?")
        ask_for_names()


def normal_function(*args):
    print("\nYou're probably wondering what the folder name means...")
    print("You should probably look it up you tease >~<")
    print("\nThis doesn't mean that I wasn't smiling stupidly the whole time.")
    print("And we both know the reason why, that's why this program isn't a confession.\n\t(You probably still want me to say it, don't you?)")
    answer = input("\nWell then... do you want me to spell it out for you? (y/n) ")
    if answer.lower() == 'y':
        reply = "\nI LOVE YOU VANESSA!"
        for letter in reply:
            print(letter)
        print(f"\nBasically, {reply.replace('!','.',1)}")
        print("My feelings haven't changed one bit. I didn't show but, when you used our names together, I ...\nIn other words, I won't forget it.")
        print("I will have my revenge. 😊")
    elif answer.lower() == 'n':
        print("\nAn interesting choice. Oh well, how I feel about you is not about to change.")
        print("I'll tell you when you're ready.\nHope you enjoyed this program😊 ")
        print("\nI sure hope you meant all you typed in our date.\n\t(Yes, I treated it as one...hehehe💀)")
        print("Until next time, adios.\n")
    the_end()


print("\nHey! Welcome to this normal python program.")
print("Before we can continue, I need to know your names.\nDon't worry, I'm totally safe. I was made by David afterall.")
ask_for_names()