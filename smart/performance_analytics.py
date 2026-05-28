import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Assuming 'student_performance.csv' exists
try:
    df = pd.read_csv("student_performance.csv")
    print(df.describe())
    scores = df[["Math", "Science", "English"]].to_numpy()
    print("Mean Scores:", np.mean(scores, axis=0))
    df.plot(x="Name", y=["Math", "Science", "English"], kind="bar")
    plt.show()
except Exception as e:
    print(e)