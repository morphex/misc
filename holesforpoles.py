#!/usr/bin/python3

__doc__ = """

Small utility script to find the right places to put
two poles that will support a roof, so that it is possible
to extend it to a whole length with an extra pole.

"""

# Metres
whole = 7.0
partial = 4.5

# Centimetres
start = 50
stop = 150
step = 5

# Acceptable difference, centimetres
imprecision = 10

for x in range(start,stop,step):
  x = x / 100.0
  imprecision = imprecision / 100.0
  partial_ = partial - (x*2)
  whole_ = whole - (x*2)
  whole__ = whole_ / 2
  difference = partial_ - whole__
  if abs(difference) <= imprecision:
    print("End space: " + str(x))
    #print(str(partial_) + " " + str(whole_))
    print("Imprecision: " + str(abs(difference)))
    print("Pole space: " + str(partial_) + "-" + str(whole__))

