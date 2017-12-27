import random
import numpy as np
from collections import defaultdict

def FirstShuffle(num_of_players):
    full_deck = FullDeck()
    players = []
    cards_per_player = 54 / num_of_players
    for i in range(num_of_players):
        new_player = Player()
        for j in range(cards_per_player):
            index = random.randint(0, len(full_deck.cards)-1)
            # print index
            new_player.addCard(full_deck.cards.pop(index))
        players.append(new_player)
    return players


def oneTurn(players):
    this_turn_cards = []
    this_turn_numbers = []
    for player in players:
        player_card = player.drawCard()
        if player_card != -2:
            # print player_card
            this_turn_cards.append(player_card)
            this_turn_numbers.append(player_card.getNum())
        else:
            this_turn_numbers.append(0)
    print 'The numbers in this turn are: {}'.format(this_turn_numbers)

    # drawed should be the indices of the players that are tied
    hist = np.histogram(this_turn_numbers, bins=range(1, 16))
    drawed = []
    hist = hist[0]
    for i in range(len(this_turn_numbers)):
        if hist[this_turn_numbers[i]-1] > 1:
            drawed.append(i)

    while(len(drawed)>0):
        player_indices = [x + 1 for x in drawed]
        print "there's a draw between players number: {}".format(player_indices)
        for i in drawed:
            player_card = players[i].drawCard()
            # print player_card
            if player_card == -1: # out of cards
                print 'player {} has no cards left!'.format(i+1)
            elif player_card == -2: # already lost
                this_turn_numbers[i] = 0
            else:
                this_turn_cards.append(player_card)
                this_turn_numbers[i] = player_card.getNum()
        print 'Now the numbers are: {}'.format(this_turn_numbers)
        hist = np.histogram(this_turn_numbers, bins=range(1, 16))
        drawed = []
        hist = hist[0]
        for i in range(len(this_turn_numbers)):
            if hist[this_turn_numbers[i] - 1] > 1:
                drawed.append(i)

    max_value = max(this_turn_numbers)
    max_index = this_turn_numbers.index(max_value)
    print 'player number {} won !\n' .format(max_index+1)
    players[max_index].score += 1
    for won_card in this_turn_cards:
        players[max_index].addCard(won_card)

    losers = []
    for j in range(len(players)):
        # print players[j].drawCard()
        if players[j].lost == 1:
            losers.append(j + 1)
        if players[j].drawCard() == -1:
            losers.append(j + 1)
            players[j].lost = 1
            print 'CHANGE'

    if len(losers) > 0:
        print 'players {} lost :('.format(losers)
    if len(losers) == len(players)-1:
        print 'Game Over !!!'
        return [players, 1]

    return [players, 0]


def game(num_of_players):
    players = FirstShuffle(num_of_players)
    keep_playing = raw_input('Are you ready to the next turn? [Y]es / [N]o\n')
    game_over = 0
    while keep_playing == 'Y' or keep_playing == 'y' and game_over == 0:
        [players, game_over] = oneTurn(players)
        keep_playing = raw_input('Are you ready to the next turn? [Y]es / [N]o\n')
    return players


class FullDeck(object):
    def __init__(self):
        DECK_SIZE = 54
        self.cards = []
        for i in range(DECK_SIZE):
            num = random.randint(1, 14)
            if num == 14:
                sign = random.randint(1, 2)
            else:
                sign = random.randint(1, 4)
            card = Card(num, sign)
            self.cards.append(card)

class Player(object):
    def __init__(self):
        self.score = 0
        self.cards = []
        self.lost = 0

    def addCard(self, card):
        self.cards.append(card)

    def drawCard(self):
        if self.lost == 1:
            return -2
        cards_amount = len(self.cards)
        if cards_amount == 0:
            return -1
        card_index = random.randint(0, cards_amount-1)
        card = self.cards.pop(card_index)
        return card

class Card(object):
    def __init__(self, num, sign):
        self.num = num
        self.sign = sign

    def getNum(self):
        return self.num


def main():
    num_of_players = eval(raw_input('Hey!\nHow many players are you?\n'))
    players = game(num_of_players)
    for i in range(len(players)):
        print('The final score of player {} is: {} .').format(i+1, players[i].score)
    print '\nGoodbye and see you next time!'


if __name__ == "__main__":
    main()
    # players = FirstShuffle(2)
    # x = players[0].cards
    # y = []
    # z = []
    # for i in range(len(x)):
    #     y.append(x[i].getNum())
    #     z.append(x[i].sign)
    # print(y)
    # print(z)
    # hist = np.histogram(y, bins=range(1, 16))
    # print hist[0]
    # tied_indices = hist[0] >= 2
    # drawed = [i+1 for i in range(0,14) if hist[0][i] > 1]
    # print drawed
    # print "///////////////////////"
    # for i in hist[0][drawed]:
    #     print i

    # print(np.histogram(y, bins=range(1,16)))
