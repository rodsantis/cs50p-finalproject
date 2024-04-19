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
    
    If you guess it right you will receive a special award, if you don't, try it again! {Style.RESET_ALL}
    {Fore.RED}<<<<<{Style.RESET_ALL}
    """

if __name__ == "__main__":
    main()