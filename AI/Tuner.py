import random as random
import math as math
from Game import controller

def randomInteger(min, max):
    return math.floor(random.random() * (max - min ) + min)

def normalizeCandidate(candidate):
    norm = math.sqrt(sum([x**2 for x in candidate]))
    candidate.heightWeight /= norm
    candidate.linesWeight /= norm
    candidate.holesWeight /= norm
    candidate.bumpinessWeight /= norm

def generateRandomCandidate():
    heightWeight = random.random() - 0.5
    linesWeight = random.random() - 0.5
    holesWeight = random.random() - 0.5
    bumpinessWeight = random.random() - 0.5
    candidate = [heightWeight, linesWeight, holesWeight, bumpinessWeight]
    normalizeCandidate(candidate)
    return candidate

def sortCandidates(candidates):
    return sorted(candidates, key = lambda x: x.fitness, reverse = True)

def computeFitness(candidates,number_of_games,maxNumberOfMoves):
    for i in range(len(candidates)):
        candidate = candidates[i]
        ai = AI(candidate)
        totalScore = 0 
        for j in range(number_of_games):
            controller = controller()
            gameState = controller.gameState
            playingPieces = [gameState.getRandomPiece() for _ in range(2)]
            playingPiece = playingPieces[0]
            score = 0
            numberOfMoves= 0
            while numberOfMoves < maxNumberOfMoves and not controller.isGameOver():
                numberOfMoves += 1
                workingPiece = AI.best(controller, playingPieces)
                score += controller.step(workingPiece)


                
                    
                
                

                



            

            
