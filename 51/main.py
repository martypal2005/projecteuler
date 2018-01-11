#!/usr/bin/env python

import sympy
import itertools


def generator():
  n = 2
  while True:
    yield n
    n += 1

def replace_templates(length, count, original):
  string = '_' * count + 'x' * (length - count)
  permutations = set()
  for permutation in itertools.permutations(string):
    permutations.add(permutation)

  templates = set()
  for template in permutations:
    t = ''
    for i in xrange(len(template)):
      if template[i] == 'x':
        t += original[i]
      else:
        t += '_'
    templates.add(t)
  return templates
  
def replace_char(string, index, letter):
  if len(string) == 0:
    return 'x'
  return string[:index] + 'x' + string[index+1:]

if __name__ == '__main__':
  max_count = 0
  for p in generator():
    string_prime = str(p)
    for i in xrange(1, len(string_prime)):
      for template in replace_templates(len(string_prime), i, string_prime):
        count = 0
        replaced_primes = []
        for j in xrange(10):
          number = template.replace('_', str(j))
          if number[0] == '0':
            continue
          if sympy.isprime(number):
            replaced_primes.append(number)
            count += 1
        if count > max_count:
          max_count = count
          print '-----------'
          print p, count
          print template
          print '-'
          for number in replaced_primes:
            print number
          if count >= 8:
            exit(0)
