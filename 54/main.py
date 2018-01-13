#!/usr/bin/env python

import os
import sys


# 0 High Card: Highest value card.
# 1 One Pair: Two cards of the same value.
# 2 Two Pairs: Two different pairs.
# 3 Three of a Kind: Three cards of the same value.
# 4 Straight: All cards are consecutive values.
# 6 Full House: Three of a kind and a pair.
# 7 Four of a Kind: Four cards of the same value.

# 5 Flush: All cards of the same suit.
# 8 Straight Flush: All cards are consecutive values of same suit.
# 9 Royal Flush: Ten, Jack, Queen, King, Ace, in same suit.

def add(obj, key):
  if key in obj:
    obj[key] += 1
  else:
    obj[key] = 1

def update(old_score, new_score, old_high, new_high):
  if new_score > old_score:
    return new_score, new_high
  return old_score, old_high

#2, 3, 4, 5, 6, 7, 8, 9, 10, Jack, Queen, King, Ace.
def get_value(value):
  if value == 'T':
    return 10
  if value == 'J':
    return 11
  elif value == 'Q':
    return 12
  elif value == 'K':
    return 13
  elif value == 'A':
    return 14
  return int(value)

def score(hand):
  values = {}
  suits = {}
  for i in xrange(len(hand)):
    add(values, get_value(hand[i][0]))
    add(suits, hand[i][0])

  score = 0
  
  ONE_PAIR = False
  TWO_PAIR = False
  THREE_OF_A_KIND = False
  STRAIGHT = True
  FULL_HOUSE = False
  FOUR_OF_A_KIND = False

  values_sorted = []

  highest_card = 0
  previous_value = 0
  last_card = 0
  for value in values:
    values_sorted.append(value)
    print 'value:', value, 'count:', values[value]
    if value > last_card:
      last_card = value
    if values[value] == 2:
      if ONE_PAIR:
        TWO_PAIR = True
        score, highest_card = update(score, 2, highest_card, value)
      else:
        ONE_PAIR = True
        score, highest_card = update(score, 1, highest_card, value)
    elif values[value] == 3:
      if ONE_PAIR:
        FULL_HOUSE = True
        score, highest_card = update(score, 6, highest_card, value)
      else:
        THREE_OF_A_KIND = True
        score, highest_card = update(score, 3, highest_card, value)
    elif values[value] == 4:
      FOUR_OF_A_KIND = True
      score, highest_card = update(score, 7, highest_card, value)
      
    previous_value = value

  values_sorted = sorted(values_sorted)

  for value in values_sorted:
    if previous_value:
      if value != previous_value + 1:
        STRAIGHT = False

  if STRAIGHT:
    score = 4
    highest_card = last_card

  print 'Suits:', len(suits)



  if len(suits) == 1:
    if STRAIGHT:
      if highest_card == 14:
        score, highest_card = update(score, 9, 0, last_card)
      else:
        score, highest_card = update(score, 8, 0, last_card)
    else:
      score, highest_card = update(score, 5, 0, last_card)

  if score == 0:
    highest_card = last_card

  return score, highest_card


if __name__ == '__main__':
  # path = os.path.dirname(__file__) + '/poker.txt'
  path = 'poker.txt'
  with open(path, 'r') as f:
    lines = f.readlines()

  one_wins = 0
  two_wins = 0

  for line in lines:
    line = line.strip()
    cards = line.split()
    cards_player_1 = cards[:5]
    cards_player_2 = cards[5:]

    print cards_player_1
    s1, h1 = score(cards_player_1)
    print s1
    print h1
    print '---'

    # if s > 3:
    #   sys.stdin.read(1)

    print cards_player_2
    s2, h2 = score(cards_player_2)
    print s2
    print h2
    print '---'

    if s1 == s2:
      if h1 > h2:
        one_wins += 1
      else:
        two_wins += 1
    else:
      if s1 > s1:
        one_wins += 1
      else:
        two_wins += 1

  print 'One wins:', one_wins
  print 'Two wins:', two_wins



    # if s > 3:
    #   sys.stdin.read(1)

    # print '1: {0}, 2: {1}'.format(' '.join(cards_player_1), ' '.join(cards_player_2))
