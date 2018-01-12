#!/usr/bin/env python

if __name__ == '__main__':
  with open('poker.txt', 'r') as f:
    lines = f.readlines()

  for line in lines:
    line = line.strip()
    cards = line.split()
    cards_player_1 = cards[:5]
    cards_player_2 = cards[5:]

    print '1: {0}, 2: {1}'.format(' '.join(cards_player_1), ' '.join(cards_player_2))
