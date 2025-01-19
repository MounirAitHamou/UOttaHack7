import random as random
import math as math
from AI.AI import AI
from TetrisGame.Trainer import Trainer
def randomInteger(min, max):
    return math.floor(random.random() * (max - min ) + min)

def normalizeCandidate(candidate):
    norm = math.sqrt(candidate["heightWeight"] ** 2 + candidate["linesWeight"] ** 2 + candidate["holesWeight"] ** 2 + candidate["bumpinessWeight"] ** 2)
    candidate["heightWeight"] /= norm
    candidate["linesWeight"] /= norm
    candidate["holesWeight"] /= norm
    candidate["bumpinessWeight"] /= norm

def generateRandomCandidate():
    heightWeight = random.random() - 0.5
    linesWeight = random.random() - 0.5
    holesWeight = random.random() - 0.5
    bumpinessWeight = random.random() - 0.5
    candidate = {
        "heightWeight": heightWeight,
        "linesWeight": linesWeight,
        "holesWeight": holesWeight,
        "bumpinessWeight": bumpinessWeight
    }
    normalizeCandidate(candidate)
    return candidate

def sortCandidates(candidates):
    return sorted(candidates, key = lambda x: x["fitness"], reverse = True)

def computeFitnesses(candidates, number_of_games, maxNumberOfMoves):
    for i in range(len(candidates)):
        if i % (math.ceil(len(candidates) / 100)) == 0:
            print((i / len(candidates)) * 100, "%")
        candidate = candidates[i]
        ai = AI(candidate)
        totalScore = 0
        for j in range(number_of_games):
            trainer = Trainer()
            playingPieces = [trainer.getRandomPiece() for _ in range(2)]
            playingPiece = playingPieces[0]
            score = 0
            numberOfMoves= 0
            while numberOfMoves < maxNumberOfMoves and not trainer.isGameOver():
                numberOfMoves += 1
                playingPiece = ai.best(trainer.game.grid, playingPieces)[0]
                if playingPiece is None:
                    break
                score += trainer.step(playingPiece)
                playingPieces[:-1] = playingPieces[1:]
                playingPieces[-1] = trainer.getRandomPiece()
                playingPiece = playingPieces[0]

            totalScore += score
        candidate["fitness"] = totalScore

def tournamentSelectPair(candidates, ways):
    indices = []
    for i in range(len(candidates)):
        indices.append(i)
    
    fittestCandidateIndex1 = None
    fittestCandidateIndex2 = None
    for i in range(ways):
        selected_index = indices.pop(random.randint(0, len(indices) - 1))
        if fittestCandidateIndex1 == None or selected_index < fittestCandidateIndex1:
            fittestCandidateIndex2 = fittestCandidateIndex1
            fittestCandidateIndex1 = selected_index
        elif fittestCandidateIndex2 == None or selected_index < fittestCandidateIndex2:
            fittestCandidateIndex2 = selected_index
    return [candidates[fittestCandidateIndex1], candidates[fittestCandidateIndex2]]

def crossOver(candidate1, candidate2):
    candidate = {
        "heightWeight": candidate1["fitness"] * candidate1["heightWeight"] + candidate2["fitness"] * candidate2["heightWeight"],
        "linesWeight": candidate1["fitness"] * candidate1["linesWeight"] + candidate2["fitness"] * candidate2["linesWeight"],
        "holesWeight": candidate1["fitness"] * candidate1["holesWeight"] + candidate2["fitness"] * candidate2["holesWeight"],
        "bumpinessWeight": candidate1["fitness"] * candidate1["bumpinessWeight"] + candidate2["fitness"] * candidate2["bumpinessWeight"]
    }
    normalizeCandidate(candidate)
    return candidate

def mutateCandidate(candidate):
    quantity = random.random() * 0.4 - 0.2
    mutatedGene = random.randint(0, 3)
    match mutatedGene:
        case 0:
            candidate["heightWeight"] += quantity
        case 1:
            candidate["linesWeight"] += quantity
        case 2:
            candidate["holesWeight"] += quantity
        case 3:
            candidate["bumpinessWeight"] += quantity

def deleteNLastReplacement(candidates: list, newCandidates):
    candidates = candidates[:-len(newCandidates)]
    candidates.extend(newCandidates)
    sortCandidates(candidates)

def tune(population = 100, rounds = 5, moves = 200, selection = 10,mutationRate = 0.05):
    candidates = []
    candidates.extend([generateRandomCandidate() for _ in range(population)])
    computeFitnesses(candidates,rounds,moves)
    sortCandidates(candidates)
    count = 0
    while True:
        
        newCandidates = []
        for _ in range(30):
            pair = tournamentSelectPair(candidates,selection)
            candidate = crossOver(pair[0],pair[1])
            if random.random() < mutationRate:
                mutateCandidate(candidate)
            normalizeCandidate(candidate)
            print(candidate)
            newCandidates.append(candidate)
        computeFitnesses(newCandidates,rounds,moves)
        deleteNLastReplacement(candidates,newCandidates)
        totalFitness = 0
        for candidate in candidates:
            totalFitness += candidate["fitness"]
        
        highestCandidate = candidates[0]
        print(f"Generation: {count}, Best Fitness: {candidates[0]["fitness"]}, Average Fitness: {totalFitness / len(candidates)}")
        #save candidate to file
        print(f"Height Weight: {highestCandidate["heightWeights"]}, Lines Weight: {highestCandidate["linesWeight"]}, Holes Weight: {highestCandidate["holesWeight"]}, Bumpiness Weight: {highestCandidate["bumpinessWeight"]}")
        count+=1