import numpy as np

#getting 10 random
inp = np.random.randint(0, 20, size=10)

print("Vector list:", inp)

print("Most frequent item in the vector list is:",np.bincount(inp).argmax())