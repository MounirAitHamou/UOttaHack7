from Game.Controller import Controller
from AI.Tuner import *

tune = False

def main():
    if tune:
        # Tuner.tune()
        pass
    else:
        Controller.startGame()

if __name__ == "__main__":
    main()