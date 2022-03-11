import pandas as pd

df = pd.read_csv('test.csv', delimiter=';', header=0)

df = df.area.value_counts()

df.to_csv("results.csv")
