For every number n:
1: Generate a replace template

Example: 
A five digit number '12345' will have replace templates:
  - ['_2345', '1_345', ', '12_45', ...]
  - ['__345', ... every unique permutation] 
  - ...
  - ['____5', ...]

2: Use python string replace method and replace the '_' with a number j (0-9 in a for loop)
3: Count how many are primes
4: Repeat until we have 8

This turned out to be pretty inefficient. Probably because all the string work. (I love strings)

~2 minutes