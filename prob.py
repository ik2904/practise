import numpy as np

results = np.random.choice(
    ["Head", "Tail"],
    size=1000
)

heads = np.sum(results == "Head")

probability = heads / 1000

print(probability)