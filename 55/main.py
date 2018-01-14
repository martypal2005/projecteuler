#!/usr/bin/env python

import sys

def palindrome(number):
  s = str(number)
  l = len(s)
  for i in xrange(l):
    if s[i] != s[l-i-1]:
      return False
  return True

def reversed_number(number):
  s = str(number)
  r = s[::-1]
  return int(r)

def lychrel(number):
  print '------'
  print 'Number:', number
  num1 = number
  for i in xrange(50):
    num2 = reversed_number(num1)
    sum = num1 + num2
    str = '[{0}] {1} + {2} = {3}'.format(i+1, num1, num2, sum)
    if palindrome(sum):
      str += ' <---- PALINDROME'
      print str
      return False
    print str
    num1 = sum
  print '{0} is a lychrel number'.format(number)
  return True


if __name__ == '__main__':
  count = 0
  for i in xrange(1, 10000):
    if lychrel(i):
      count += 1
      # sys.stdin.read(1)
      
  print '=============='
  print 'Count:', count