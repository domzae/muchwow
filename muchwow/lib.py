from numpy import random
import webbrowser

def try_me():
    inp = abs(int(input("Give me a number ;) : ")))
    webbrowser.open(f'https://www.memedroid.com/memes/random/{inp}', new=2)
    
if __name__ == "__main__":
    try_me()