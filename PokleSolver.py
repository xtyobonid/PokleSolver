from Card import Card
from Hand import Hand
from itertools import combinations

possiblecards = [Card(1,1),  Card(1,2),  Card(1,3),  Card(1,4), 
                 Card(2,1),  Card(2,2),  Card(2,3),  Card(2,4), 
                 Card(3,1),  Card(3,2),  Card(3,3),  Card(3,4), 
                 Card(4,1),  Card(4,2),  Card(4,3),  Card(4,4), 
                 Card(5,1),  Card(5,2),  Card(5,3),  Card(5,4), 
                 Card(6,1),  Card(6,2),  Card(6,3),  Card(6,4), 
                 Card(7,1),  Card(7,2),  Card(7,3),  Card(7,4), 
                 Card(8,1),  Card(8,2),  Card(8,3),  Card(8,4), 
                 Card(9,1),  Card(9,2),  Card(9,3),  Card(9,4), 
                 Card(10,1), Card(10,2), Card(10,3), Card(10,4), 
                 Card(11,1), Card(11,2), Card(11,3), Card(11,4), 
                 Card(12,1), Card(12,2), Card(12,3), Card(12,4), 
                 Card(13,1), Card(13,2), Card(13,3), Card(13,4)]

player1 = [Card(7, 2), Card(8, 3)]
player1Rankings = [2, 3, 2]
player2 = [Card(9, 3), Card(10, 2)]
player2Rankings = [1, 1, 3]
player3 = [Card(11, 4), Card(13, 3)]
player3Rankings = [3, 2, 1]
playerHandsCombined = player1 + player2 + player3

remainingcards = [i for i in possiblecards if i not in playerHandsCombined]

validFlopCombinations = []

tempHand = Hand([Card(7, 3), Card(8, 4), Card(11, 2), Card(11, 3), Card(11, 1)])
#print(tempHand.eval())

#find all possible flops to poklegame
#https://stackoverflow.com/questions/41680388/how-do-i-iterate-through-combinations-of-a-list
for combo in combinations(remainingcards, 3):
    answerCards = list(combo)

    p1hand = Hand(player1 + answerCards)
    p2hand = Hand(player2 + answerCards)
    p3hand = Hand(player3 + answerCards)

    p1eval = p1hand.eval()
    p2eval = p2hand.eval()
    p3eval = p3hand.eval()


    if (p1eval > p2eval and p2eval > p3eval and player1Rankings[0] == 1 and player2Rankings[0] == 2):
        #print(answerCards)
        validFlopCombinations.append(answerCards)
    elif (p1eval > p3eval and p3eval > p2eval and player1Rankings[0] == 1 and player3Rankings[0] == 2):
        #print(answerCards)
        validFlopCombinations.append(answerCards)
    elif (p2eval > p1eval and p1eval > p3eval and player2Rankings[0] == 1 and player1Rankings[0] == 2):
        #print(answerCards)
        validFlopCombinations.append(answerCards)
    elif (p2eval > p3eval and p3eval > p1eval and player2Rankings[0] == 1 and player3Rankings[0] == 2):
        #print(answerCards)
        validFlopCombinations.append(answerCards)
    elif (p3eval > p1eval and p1eval > p2eval and player3Rankings[0] == 1 and player1Rankings[0] == 2):
        #print(answerCards)
        validFlopCombinations.append(answerCards)
    elif (p3eval > p2eval and p2eval > p1eval and player3Rankings[0] == 1 and player2Rankings[0] == 2):
        #print(answerCards)
        validFlopCombinations.append(answerCards)

with open('flopoutput.txt', 'w') as f:
    for combo in validFlopCombinations:
        f.write(f"{str(combo)}\n")



validTurnCombinations = []

#look at all possible flops
for flop in validFlopCombinations:
    tempRemaining = [i for i in remainingcards if i not in flop]

    #look at all possible turn cards
    for card in tempRemaining:
        tempCombo = flop.copy()
        tempCombo.append(card)

        tempCombo1 = tempCombo + player1
        tempCombo2 = tempCombo + player2
        tempCombo3 = tempCombo + player3

        p1maxhand = Hand([Card(2,1), Card(3,2), Card(4,3), Card(5,4), Card(7,1)])
        p2maxhand = Hand([Card(2,1), Card(3,2), Card(4,3), Card(5,4), Card(7,1)])
        p3maxhand = Hand([Card(2,1), Card(3,2), Card(4,3), Card(5,4), Card(7,1)])

        #for this flop + turn, find each players best combo of four
        for combo in combinations(tempCombo1, 5):
            answerCards = list(combo)

            p1hand = Hand(answerCards)

            if p1hand.eval() > p1maxhand.eval():
                p1maxhand = p1hand
        
        #for this flop + turn + river, find each players best combo of four
        for combo in combinations(tempCombo2, 5):
            answerCards = list(combo)

            p2hand = Hand(answerCards)

            if p2hand.eval() > p2maxhand.eval():
                p2maxhand = p2hand

        #for this flop + turn + river, find each players best combo of four
        for combo in combinations(tempCombo3, 5):
            answerCards = list(combo)

            p3hand = Hand(answerCards)

            if p3hand.eval() > p3maxhand.eval():
                p3maxhand = p3hand
        
        #determine if these optimal player hands match rankings after turn
        p1eval = p1maxhand.eval()
        p2eval = p2maxhand.eval()
        p3eval = p3maxhand.eval()

        if (p1eval > p2eval and p2eval > p3eval and player1Rankings[1] == 1 and player2Rankings[1] == 2):
            #print(tempCombo)
            validTurnCombinations.append(tempCombo)
        elif (p1eval > p3eval and p3eval > p2eval and player1Rankings[1] == 1 and player3Rankings[1] == 2):
            #print(tempCombo)
            validTurnCombinations.append(tempCombo)
        elif (p2eval > p1eval and p1eval > p3eval and player2Rankings[1] == 1 and player1Rankings[1] == 2):
            #print(tempCombo)
            validTurnCombinations.append(tempCombo)
        elif (p2eval > p3eval and p3eval > p1eval and player2Rankings[1] == 1 and player3Rankings[1] == 2):
            #print(tempCombo)
            validTurnCombinations.append(tempCombo)
        elif (p3eval > p1eval and p1eval > p2eval and player3Rankings[1] == 1 and player1Rankings[1] == 2):
            #print(tempCombo)
            validTurnCombinations.append(tempCombo)
        elif (p3eval > p2eval and p2eval > p1eval and player3Rankings[1] == 1 and player2Rankings[1] == 2):
            #print(tempCombo)
            validTurnCombinations.append(tempCombo)

with open('turnoutput.txt', 'w') as f:
    for combo in validTurnCombinations:
        f.write(f"{str(combo)}\n")





validRiverCombinations = []

#look at all possible turns
for turn in validTurnCombinations:
    tempRemaining = [i for i in remainingcards if i not in turn]

    tempturn = [Card(7, 3), Card(8, 4), Card(11, 2), Card(11, 3)]
    #if turn == tempturn:
        #print(tempRemaining)

    #print(tempRemaining)

    tempcard = Card(11, 1)

    #look at all possible river cards
    for card in tempRemaining:
        tempCombo = turn.copy()
        tempCombo.append(card)

        tempCombo1 = tempCombo + player1
        tempCombo2 = tempCombo + player2
        tempCombo3 = tempCombo + player3

        p1maxhand = Hand([Card(2,1), Card(3,2), Card(4,3), Card(5,4), Card(7,1)])
        p2maxhand = Hand([Card(2,1), Card(3,2), Card(4,3), Card(5,4), Card(7,1)])
        p3maxhand = Hand([Card(2,1), Card(3,2), Card(4,3), Card(5,4), Card(7,1)])

        #for this flop + turn + river, find each players best combo of three
        for combo in combinations(tempCombo1, 5):
            answerCards = list(combo)

            p1hand = Hand(answerCards)

            if p1hand.eval() > p1maxhand.eval():
                p1maxhand = p1hand
        
        #for this flop + turn + river, find each players best combo of three
        for combo in combinations(tempCombo2, 5):
            answerCards = list(combo)

            p2hand = Hand(answerCards)

            if p2hand.eval() > p2maxhand.eval():
                p2maxhand = p2hand

        #for this flop + turn + river, find each players best combo of three
        for combo in combinations(tempCombo3, 5):
            answerCards = list(combo)

            p3hand = Hand(answerCards)

            if p3hand.eval() > p3maxhand.eval():
                p3maxhand = p3hand
        
        #determine if these optimal player hands match rankings after turn
        p1eval = p1maxhand.eval()
        p2eval = p2maxhand.eval()
        p3eval = p3maxhand.eval()

        if (p1eval > p2eval and p2eval > p3eval and player1Rankings[2] == 1 and player2Rankings[2] == 2):
            #print(tempCombo)
            validRiverCombinations.append(tempCombo)
        elif (p1eval > p3eval and p3eval > p2eval and player1Rankings[2] == 1 and player3Rankings[2] == 2):
            #print(tempCombo)
            validRiverCombinations.append(tempCombo)
        elif (p2eval > p1eval and p1eval > p3eval and player2Rankings[2] == 1 and player1Rankings[2] == 2):
            #print(tempCombo)
            validRiverCombinations.append(tempCombo)
        elif (p2eval > p3eval and p3eval > p1eval and player2Rankings[2] == 1 and player3Rankings[2] == 2):
            #print(tempCombo)
            validRiverCombinations.append(tempCombo)
        elif (p3eval > p1eval and p1eval > p2eval and player3Rankings[2] == 1 and player1Rankings[2] == 2):
            #print(tempCombo)
            validRiverCombinations.append(tempCombo)
        elif (p3eval > p2eval and p2eval > p1eval and player3Rankings[2] == 1 and player2Rankings[2] == 2):
            #print(tempCombo)
            validRiverCombinations.append(tempCombo)

with open('riveroutput.txt', 'w') as f:
    for combo in validRiverCombinations:
        f.write(f"{str(combo)}\n")
    

#print(remainingcards)

#cards = [Card(5,2), Card(5,3), Card(8,2), Card(8,1), Card(8,3)]
#hand = Hand(cards)

#print(hand.eval())