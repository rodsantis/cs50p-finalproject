from colorama import init as colorama_init
from colorama import Fore, Style

colorama_init()

def game_instructions():
    """
        This function returns the game instructions for the game for the player
    """

    return f"""
    {Fore.RED}>>>>>{Style.RESET_ALL}{Fore.GREEN}
        Welcome to this Movie Guessing Game 
    
    You will have 3 (three) tries to guess the right movie, you are free to google it.
    You will start the game with 1 hint and in every wrong guess you will
    gain 1 more tip.
    
    Try to get it right, if you don't, don't worry it might be a new Title for you to watch! {Style.RESET_ALL}
    {Fore.RED}<<<<<{Style.RESET_ALL}
    """


def first_tip():
    return f"{Fore.BLUE}FIRST TIP:{Style.RESET_ALL}"


def second_tip():
    return f"{Fore.BLUE}SECOND TIP:{Style.RESET_ALL}"


def third_tip():
    return f"{Fore.BLUE}FINAL TIP:{Style.RESET_ALL}"


def first_wrong():
    return f"{Fore.RED}Not there yet, lets try it again.{Style.RESET_ALL}"


def second_wrong():
    return f"{Fore.RED}One last try, check for the year also it may help you.{Style.RESET_ALL}"


def third_wrong():
    return f"{Fore.RED}Oooh No! You run out of tries! But don't worry this might be a new title for you to watch, so the movie was:{Style.RESET_ALL}"


def thank_you():
    return f"{Fore.GREEN}Thank you for playing!{Style.RESET_ALL} {Fore.YELLOW}:){Style.RESET_ALL}"

if __name__ == "__main__":
    main()