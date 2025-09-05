import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

arr = np.array([1, 2, 3])
print("numpy array:", arr)

df = pd.DataFrame({"col1": [1, 2, 3], "col2": [4, 5, 6]})
print("pandas dataframe:\n", df)

plt.plot(df["col1"], df["col2"])
plt.title("Practice Plot")
plt.savefig("plot.png")

