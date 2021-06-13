#!/usr/bin/python3

# Small utility script, to find the sweet spot for placing two poles, and
# making it look natural when adding a third pole.
#
#
# Rough sketch (Outer Margin):
#
# Partial
#
# -----------------------
# OM    *        *     OM
#
# Whole
#
# -------------------------------
# OM    *        *        *    OM
#

whole = 7.1 # metres
partial = 4.38 # metres

# Both sides, metres
margin = 0.1
max_margin = 1.75

numbers = []

while True:
    whole_ = (whole - margin) / 2
    partial_ = (partial - margin) / 1
    numbers.append(((whole_ - partial_), whole_, partial_, margin))
    margin += 0.01
    if margin > max_margin: break

best_match = min(numbers, key=lambda x: abs(x[0]))
print("Best match, margin of error: %f" % best_match[0])
print("Space between poles for whole: %f" % best_match[1])
print("Space between poles for partial: %f" % best_match[2])
print("Outer margin: %f" % best_match[3])
