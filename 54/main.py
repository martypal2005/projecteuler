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

class Score:
  def __init__(self, score, value):
    self.score = score
    self.value = value
  def __str__(self):
    return str(score)
  def __repr__(self):
    return str(score)
  def __lt__(self, other):
    if self.score < other.score:
      return True
    elif self.score == other.score and self.value < other.value:
      return True
    return False
  def __eq__(self, other):
    if self.score == other.score and self.value == other.value:
      return True
    return False
  def __gt__(self, other):
    if self.score > other.score:
      return True
    elif self.score == other.score and self.value > other.value:
      return True
    return False

class ScoreList:
  def __init__(self):
    self.scores = []
  def add(self, score, value):
    self.scores.append(Score(score, value))
    self.scores.sort()
    self.scores.reverse()

  def __str__(self):
    string = ''
    for score in self.scores:
      string += '{0}: {1}, '.format(score.score, score.value)
    return string

  def __lt__(self, other):
    max_length = min(len(self.scores), len(other.scores))
    for i in xrange(max_length):
      if self.scores[i] < other.scores[i]:
        return True
      elif self.scores[i] == other.scores[i]:
        continue
      else:
        return False
    return False

  def __eq__(self, other):
    max_length = min(len(self.scores), len(other.scores)) 
    for i in xrange(max_length):
      if self.scores[i] != other.scores[i]:
        return False
    return True
    
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
  score_list = ScoreList()

  values = {}
  suits = {}
  for i in xrange(len(hand)):
    add(values, get_value(hand[i][0]))
    add(suits, hand[i][1])

  suits_length = len(suits)
  
  
  ONE_PAIR = False
  TWO_PAIR = False
  THREE_OF_A_KIND = False
  STRAIGHT = True
  FULL_HOUSE = False
  FOUR_OF_A_KIND = False

  last_card = 0

  values_list = []
  for value in values:
    values_list.append(value)

    if value > last_card:
      last_card = value

    if values[value] == 1:
      score_list.add(0, value)

    if values[value] == 2:
      if ONE_PAIR:
        TWO_PAIR = True
        score_list.add(2, value)
      else:
        ONE_PAIR = True
        score_list.add(1, value)
    elif values[value] == 3:
      if ONE_PAIR:
        FULL_HOUSE = True
        score_list.add(6, value)
      else:
        THREE_OF_A_KIND = True
        score_list.add(3, value)
    elif values[value] == 4:
      FOUR_OF_A_KIND = True
      score_list.add(7, value)
      
  values_list.sort()
  previous_value = 0

  # print hand
  if len(values_list) == 5:
    for value in values_list:
      if previous_value:
        if value != previous_value + 1:
          STRAIGHT = False
      previous_value = value
  else:
    STRAIGHT = False

  if STRAIGHT:
    score_list = ScoreList()
    score_list.add(4, last_card)

  if suits_length == 1:
    if STRAIGHT:
      if highest_card == 14:
        score_list.add(9, last_card)
      else:
        score_list.add(8, last_card)
    else:
      score_list.add(5, last_card)

  return score_list


if __name__ == '__main__':
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
    s1 = score(cards_player_1)

    print cards_player_2
    s2 = score(cards_player_2)

    print s1
    print s2

    if s1 < s2:
      two_wins += 1
      print 'two wins'
    elif s1 == s2:
      print 'noone wins'
    else:
      one_wins += 1
      print 'one wins'

  print 'One wins:', one_wins
  print 'Two wins:', two_wins
