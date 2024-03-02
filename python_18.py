import itertools
set = {-12, -3, -6, 7, 2, -2, 6, 3, 9, -7, -5, -8, 1, 11, -9, -4}

subsets = []
LowLim=int(input("Enter the lowerLimit"))
UppLim=int(input("Enter the upperLimit"))
for size in range(LowLim,UppLim):
  for subset in itertools.combinations(set, size):
    if sum(subset) == 0:
      subsets.append(subset)

for subset in subsets:
  print(subset)