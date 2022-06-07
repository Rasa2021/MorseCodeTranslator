from morse_code import to_morse_code
from art import logo
import os
from colorama import Fore, Style


def translation():
    choice = (input("\nType 'text' to translate text to morse code or 'morse'"
                   " to translate morse code to text: ").lower()).strip(" ")
    try:
        if choice == "text":
            message = input("\nType your message here: ")
            # Creates are list of characters from the message(input).
            character_list = [x.lower() for x in message]
            # Fetches morse code from morse_code.py and joins all the morse code segments to one string.
            code_list = []
            try:
                for character in character_list:
                    code = to_morse_code[character]
                    code_list.append(code)
            except KeyError:
                print(f"Cannot translate this character: {Fore.RED}{character}{Style.RESET_ALL}")
            else:
                print("\nYour morse code is:\n")
                print(" ".join(code_list))
        elif choice == "morse":
            message = input("\nType your message here: ")
            # Splits morse code into separate morse code segments where each of them represents a character
            morse_code_list = message.split()
            print(morse_code_list)
            print("\nYour text is:\n")
            # Turns morse code list into list of characters. Then prints the list as a string.
            character_list = []
            for code in morse_code_list:
                character = list(to_morse_code.keys())[list(to_morse_code.values()).index(code)].capitalize()
                character_list.append(character)
            print(''.join(character_list))
        else:
            raise Exception(f"{Fore.RED}Please input 'text' or 'morse'.\n{Style.RESET_ALL}")
    except Exception as error:
        print(error)
        translation()


print(logo)
print("\nWelcome to the Morse Code Translator!")
print("\nThis tool translates text to morse code and morse code to text depending on your choice. Enjoy! 😁")
translation()

to_continue = True

while to_continue:
    continue_translate = (input("\nWould you like to use Morse code translator again? "
                                "Type 'y' or 'n': ").lower()).strip(" ")
    try:
        if continue_translate == "n":
            # Exists the program
            print("\nBye. Till the next time!")
            to_continue = False
        elif continue_translate == "y":
            # Clears Run window and starts the program again as chosen by the user.
            # Only works if main.py is run in the Terminal and not in the Console!
            os.system('cls')
            translation()
        else:
            raise Exception(f"{Fore.RED}Please input 'y' for yes or 'n' for no.\n{Style.RESET_ALL}")

    except Exception as value_error:
        print(value_error)