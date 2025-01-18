import threading
import time
from Shared_Util.Gamestate import GameState

class Controller:

    def runTetrisGame():
        while True:
            print("Running Tetris Game")
            time.sleep(1)
    def getAIInput():
        while True:
            user_input = input("Enter something: ")
            print(f"Received input: {user_input}")

    if __name__ == "__main__":
        tetris_thread = threading.Thread(target=runTetrisGame)
        AI_thread = threading.Thread(target=getAIInput)

        tetris_thread.start()
        AI_thread.start()

        tetris_thread.join()
        AI_thread.join()