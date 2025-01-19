from Game.Controller import Controller
from AI.Tuner import tune

doTune = False

def main():
    if doTune:
        tune()
    else:
        Controller.startGame()

if __name__ == "__main__":
    main()