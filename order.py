import numpy as np

np.random.seed(101)

team_idx = np.random.permutation(10)

print("presentation order:")
for t in team_idx:
    print("team-", t+1)

