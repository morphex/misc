class crude_calculator:
  """Simple class that provides iteration over digits in a division operation,
     will automatically stop if a repeating pattern is found."""

  def __init__(self, numerator, denominator):
    self.numerator = numerator
    self.denominator = denominator
    self.digits = ""

  def __iter__(self):
    return self

  def __next__(self):
    if self.numerator == 0:
      raise StopIteration
    next = self.numerator
    new = 0
    while self.numerator > 1 and self.denominator <= self.numerator:
      new = self.numerator / self.denominator
      self.numerator = self.numerator % self.denominator
    self.numerator *= 10
    self.digits += str(new)
    return int(new)

#enum = crude_calculator(355, 113)
#enum = crude_calculator(7, 22)
enum = crude_calculator(1, 3)

for d in enum:
    print(d,end='')

