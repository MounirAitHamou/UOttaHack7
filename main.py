from TetrisGame.Controller import Controller
from AI.Tuner import tune

doTune = False

def main():
    if doTune:
        tune()
    else:
        Controller.startGame()

main()