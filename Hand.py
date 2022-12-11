class Hand:
    def __init__(self, cards):
        self.cards = cards
        self.cards.sort(key=lambda x: x.rank)
    
    def __str__(self):
        retstr = "{"
        for card in self.cards:
            retstr += str(card) + ", "
        return retstr + "}"
    
    # Hand strengths are as follows:
    # Straight Flush  |  9
    # Four of a Kind  |  8
    # Full House      |  7
    # Flush           |  6
    # Straight        |  5
    # Three of a Kind |  4
    # Two Pair        |  3
    # Pair            |  2
    # High Card       |  1
    def eval(self):
        counts = [None]*13

        #get number of occurances of each rank in hand
        for i in range(13):
            count = 0
            for card in self.cards:
                if card.rank - 1 == i:
                    count += 1
            counts[i] = count
        
        #check for straight flush
        #-----------------------------
        aceHigh = False
        straight = True
        for i in range(len(self.cards) - 1):
            diff = self.cards[i + 1].rank - self.cards[i].rank
            if diff != 1:
                straight = False
                break
        if not straight and counts[0] == 1:
            if counts[9] == 1 and counts[10] == 1 and counts[11] == 1 and counts[12]:
                aceHigh = True
                straight = True
        
        flush = True
        for i in range(len(self.cards) - 1):
            if self.cards[i].suit != self.cards[i + 1].suit:
                flush = False
        
        if straight and flush:
            if aceHigh:
                return "9" + self.getSingleChar(14)
            else:
                return "9" + self.getSingleChar(self.cards[-1].rank)
        #-----------------------------


        #check for four of a kind
        #-----------------------------
        hasThree = False
        pairCount = 0
        threeType = -1
        pairTypes = []
        for i in range(len(counts)):
            if counts[i] == 4:
                if i+1 == 1:
                    return "8" + self.getSingleChar(14)
                else:
                    return "8" + self.getSingleChar(i+1)
            if counts[i] == 3:
                hasThree = True
                threeType = i+1
            if counts[i] == 2:
                pairCount += 1
                pairTypes.append(i+1)
        #-----------------------------


        #check for a full house
        #-----------------------------
        if hasThree and pairCount == 1:
            if threeType == 1:
                threeType = 14
            if pairTypes[0] == 1:
                pairTypes[0] = 14
            return "7" + self.getSingleChar(threeType) + self.getSingleChar(pairTypes[0])
        #-----------------------------
        
        
        #check for a flush
        #-----------------------------
        if flush:
            return "6"
        #-----------------------------


        #check for a straight
        #-----------------------------
        if straight:
            if aceHigh:
                return "5" + self.getSingleChar(14)
            else:
                return "5" + self.getSingleChar(self.cards[-1].rank)
        #-----------------------------


        #check for three of a kind
        #-----------------------------
        if hasThree:
            if threeType == 1:
                return "4" + self.getSingleChar(14)
            else:
                return "4" + self.getSingleChar(threeType)
        #-----------------------------


        #check for two pair
        #-----------------------------
        if pairCount == 2:
            if (pairTypes[0] == 1):
                return "3" + self.getSingleChar(pairTypes[1]) + self.getSingleChar(14)
            else:
                return "3" + self.getSingleChar(pairTypes[1]) + self.getSingleChar(pairTypes[0])
        #-----------------------------


        #check for pair
        #-----------------------------
        if pairCount == 1:
            if (pairTypes[0] == 1):
                return "2" + self.getSingleChar(14)
            else:
                return "2" + self.getSingleChar(pairTypes[0])
        #-----------------------------

        #high card
        return "1"

    def getSingleChar(self, rank):
        if rank >= 2 and rank <= 9:
            return str(rank)
        elif rank == 10:
            return 'A'
        elif rank == 11:
            return 'B'
        elif rank == 12:
            return 'C'
        elif rank == 13:
            return 'D'
        elif rank == 14:
            return 'E'
        else:
            print('getSingleChar error: rank doesn\'t match known ranks')
        
