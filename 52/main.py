#!/usr/bin/env python

def numbers():
  n = 1
  while True:
    yield n
    n += 1

def get_letter_count(string):
  letters = {}
  for i in xrange(len(string)):
    if string[i] in letters:
      letters[string[i]] = letters[string[i]] + 1
    else:
      letters[string[i]] = 1
  return letters

def is_permutation(number, product):
  string_number = str(number)
  string_product = str(product)
  letters_number = get_letter_count(string_number)
  letters_product = get_letter_count(string_product)
  if len(letters_number) != len(letters_product):
    return False
  for key in letters_number:
    if key not in letters_product:
      return False
    elif letters_number[key] != letters_product[key]:
      return False
  return True

if __name__ == '__main__':
  max_length = 0
  for number in numbers():
    answer = True
    products = []
    for multiplier in xrange(2, 7):
      product = number * multiplier
      products.append('{0}x: {1}'.format(multiplier, product))
      if not is_permutation(number, product):
        answer = False
        break
    length = len(products) + 1
    if answer and length > max_length:
      max_length = length
      print '************************************'
      print number
      print '({0})'.format(length)
      print '---'
      for product in products:
        print product
      print '************************************'
      if length >= 5:
        break
