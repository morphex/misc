#!/usr/bin/python3

__doc__ = """

Small utility script to find the right places to put
to poles that will support a roof, so that it is possible
to extend it to a whole length with an extra pole.

"""

# Metres
whole = 7.0
partial = 4.5

for x in range(50,150,5):
  x = x / 100.0
  print(x)
  partial_ = partial - (x*2)
  whole_ = whole - (x*2)
  print(str(partial_) + " " + str(whole_))
  print(str(partial_) + " " + str(whole_ / 2))

