from numpy import random
import webbrowser

def try_me():
    while True:
        try:
            inp = input("Give me a number ;) : ")
            inp = abs(int(float(inp)))
            break
        except:
            print('Not a number!')

    if inp > 200:
        inp = random.randint(0,200)
    webbrowser.open(f'https://www.memedroid.com/memes/random/{inp}', new=2)
    
if __name__ == "__main__":
    try_me()