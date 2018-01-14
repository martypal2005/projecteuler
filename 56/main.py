#!/usr/bin/env python

def digital_sum(number):
  s = str(number)
  sum = 0
  for i in xrange(len(s)):
    sum += int(s[i])
  return sum

def pow(a, b):
  num = a
  for i in xrange(b):
    a *= num
  return a

if __name__ == '__main__':
  max = 0
  for a in xrange(1, 100):
    for b in xrange(1, 100):
      sum = digital_sum(pow(a, b))
      if sum > max:
        max = sum
  print max