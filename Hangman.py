import random
random_word= [ "safanh","Magic", "Macintosh", "world","hello", "test"]
Secret = random.choice(random_word).lower()
guesses = []

print("Welocome to HangMan! \nthe word you are guessing contain " + str(len(Secret)) + " letters\n")
check_win = False


def guess_loop(guess):
    global check_win
    Displayed_guess= ''
    win = 0

    for letter in Secret:
        if letter in guess:
            Displayed_guess += letter
        else:
            Displayed_guess+= ' - '
            win +=1

    if win == 0:
        check_win = True

    return Displayed_guess


def main():

    correct = False

    if len(Secret) >= 9:
        tries = 15
    else:
        tries = 10

    while not correct and len(guesses)<= 10:
        word_check= False
        while word_check == False:
            user = input("enter only one letter \n").lower()
            if len(user) > 1:
                print("only one character. Try again \n")
            else:
                break

        guesses.append(user)
        final_word = guess_loop(guesses)
        print(final_word)
        print("Tries left : "+str(tries))
        tries-=1

        if int(tries) == 0:
            correct = True
            print("out of tries, you lost :(")
        if check_win == True:
                print("you win !")
                break



main()
