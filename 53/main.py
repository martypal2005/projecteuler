#!/usr/bin/env python

from math import factorial as f

if __name__ == '__main__':
  count = 0
  for r in range(101):
    for n in range(r, 101):
      if f(n) / (f(r) * f(n-r)) > 1000000:
        count += 1
  print count
