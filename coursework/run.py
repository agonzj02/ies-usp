#!/usr/bin/env python3
import os

# Number of executions
NOE = 10

# Problems
problems = [
  # 'onemax', 'trap5', 'invtrap5',
  'sphere', 'rosen',
  # 'multibi', 'multirn'
]

# Problem sizes
problem_sizes = [10, 20, 40, 80, 160]

# Population sizes
population_sizes = [10, 20, 40, 80, 160]

# Run algorithms
for posz in population_sizes:
  for prsz in problem_sizes:
    for pr in problems:
      args = pr + ' ' + str(prsz) + ' ' + str(posz) + ' ' + str(NOE)
      os.system('python main.py ' + args)
    print()
  print()