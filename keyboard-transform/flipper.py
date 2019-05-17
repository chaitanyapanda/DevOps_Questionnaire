#!/usr/bin/env python
import numpy as np
from optparse import OptionParser


parser = OptionParser()
parser.add_option("-w", "--word", dest="given_word",
                  help="Word to perform the transformation")

options, remainder = parser.parse_args()

transforms = ['H','V',-1]
keyboard_data = [[1,2,3,4,5,6,7,8,9,0],['q','w','e','r','t','y','u','i','o','p'],['a','s','d','f','g','h','j','k','l',';'],['z','x','c','v','b','n','m',',','.','/']]

np_array = np.array(keyboard_data)

# First get the indices for the given word
given_word = options.given_word
given_list = list(given_word)
orig_index_array = []
for val in given_list:
   # convert list string to integer
   if val.isdigit():
      val = int(val)
   for index, row in enumerate(keyboard_data):
      if val in row:
        orig_index_array.append((index, row.index(val)))

for eachtransform in transforms:
    if eachtransform == 'H':
      np_array = np.fliplr(np_array)
    if eachtransform == 'V':
      np_array = np.flipud(np_array)
    if isinstance(eachtransform, int):
      np_array = np.roll(np_array, eachtransform, axis=1)
    print(np_array)

modified_string = []
for eachindex in orig_index_array:
    modified_string.append(np_array[eachindex])

print("transformed string for " + given_word + " is " + ''.join(modified_string))
